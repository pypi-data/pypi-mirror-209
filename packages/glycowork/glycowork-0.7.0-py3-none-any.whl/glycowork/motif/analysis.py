import os
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('default')
from collections import Counter
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
from sklearn.manifold import TSNE

from glycowork.glycan_data.loader import lib, df_species, unwrap, motif_list
from glycowork.motif.processing import cohen_d
from glycowork.motif.annotate import annotate_dataset, link_find
from glycowork.motif.graph import subgraph_isomorphism

def get_pvals_motifs(df, glycan_col_name = 'glycan', label_col_name = 'target',
                     thresh = 1.645, sorting = True,
                     feature_set = ['exhaustive'], extra = 'termini',
                     wildcard_list = [], multiple_samples = False,
                     motifs = None, estimate_speedup = False):
    """returns enriched motifs based on label data or predicted data\n
    | Arguments:
    | :-
    | df (dataframe): dataframe containing glycan sequences and labels
    | glycan_col_name (string): column name for glycan sequences; arbitrary if multiple_samples = True; default:'glycan'
    | label_col_name (string): column name for labels; arbitrary if multiple_samples = True; default:'target'
    | thresh (float): threshold value to separate positive/negative; default is 1.645 for Z-scores
    | sorting (bool): whether p-value dataframe should be sorted ascendingly; default: True
    | feature_set (list): which feature set to use for annotations, add more to list to expand; default is 'exhaustive'; options are: 'known' (hand-crafted glycan features), 'graph' (structural graph features of glycans), 'exhaustive' (all mono- and disaccharide features), 'terminal' (non-reducing end motifs), and 'chemical' (molecular properties of glycan)
    | extra (string): 'ignore' skips this, 'wildcards' allows for wildcard matching', and 'termini' allows for positional matching; default:'termini'
    | wildcard_list (list): list of wildcard names (such as '?1-?', 'Hex', 'HexNAc', 'Sia')
    | multiple_samples (bool): set to True if you have multiple samples (rows) with glycan information (columns); default:False
    | motifs (dataframe): can be used to pass a modified motif_list to the function; default:None
    | estimate_speedup (bool): if True, pre-selects motifs for those which are present in glycans, not 100% exact; default:False\n
    | Returns:
    | :-
    | Returns dataframe with p-values and corrected p-values for every glycan motif
    """
    #reformat to allow for proper annotation in all samples
    if multiple_samples:
        if 'target' in df.columns:
          df.drop(['target'], axis = 1, inplace = True)
        df = df.T
        samples = df.shape[1]
        df = df.reset_index()
        df.columns = [glycan_col_name] + df.columns.values.tolist()[1:]
    #annotate glycan motifs in dataset
    df_motif = annotate_dataset(df[glycan_col_name].values.tolist(),
                                motifs = motifs, feature_set = feature_set,
                               extra = extra, wildcard_list = wildcard_list,
                                estimate_speedup = estimate_speedup)
    #broadcast the dataframe to the correct size given the number of samples
    if multiple_samples:
        df.set_index(glycan_col_name, inplace = True)
        df.columns = [label_col_name]*len(df.columns)
        df_motif = pd.concat([pd.concat([df.iloc[:,k],
                                   df_motif],axis = 1).dropna() for k in range(len(df.columns))], axis = 0)
        cols = df_motif.columns.values.tolist()[1:] + [df_motif.columns.values.tolist()[0]]
        df_motif = df_motif[cols]
    else:
        df_motif[label_col_name] = df[label_col_name].values.tolist()
    #throw away any motifs that are always zero
    df_motif = df_motif.loc[:, (df_motif != 0).any(axis = 0)]
    #divide into motifs with expression above threshold & below
    df_pos = df_motif[df_motif[label_col_name] > thresh]
    df_neg = df_motif[df_motif[label_col_name] <= thresh]
    #test statistical enrichment for motifs in above vs below
    ttests = [ttest_ind(df_pos.iloc[:,k].values.tolist()+[1],
                        df_neg.iloc[:,k].values.tolist()+[1],
                        equal_var = False)[1]/2 if np.mean(df_pos.iloc[:,k])>np.mean(df_neg.iloc[:,k]) else 1.0 for k in range(0,
                                                                                                                               df_motif.shape[1]-1)]
    ttests_corr = multipletests(ttests, method = 'hs')[1].tolist()
    out = pd.DataFrame(list(zip(df_motif.columns.tolist()[:-1], ttests, ttests_corr)))
    out.columns = ['motif', 'pval', 'corr_pval']
    if sorting:
        return out.sort_values(by = ['corr_pval', 'pval'])
    else:
        return out

def get_representative_substructures(enrichment_df, libr = None):
    """builds minimal glycans that contain enriched motifs from get_pvals_motifs\n
    | Arguments:
    | :-
    | enrichment_df (dataframe): output from get_pvals_motifs
    | libr (list): sorted list of unique glycoletters observed in the glycans of our dataset\n
    | Returns:
    | :-
    | Returns up to 10 minimal glycans in a list
    """
    if libr is None:
        libr = lib
    glycans = list(set(df_species.target))
    #only consider motifs that are significantly enriched
    filtered_df = enrichment_df[enrichment_df.corr_pval < 0.05].reset_index(drop = True)
    pvals = filtered_df.pval.values.tolist()
    weights = -np.log10(pvals) / max(-np.log10(pvals))
    motifs = filtered_df.motif.values.tolist()
    
    #pair glycoletters & disaccharides with their pvalue-based weight
    mono, mono_weights = list(zip(*[(motifs[k], weights[k]) for k in range(len(motifs)) if '(' not in motifs[k]]))
    di, di_weights = list(zip(*[(motifs[k], weights[k]) for k in range(len(motifs)) if '(' in motifs[k]]))
    mono_scores = [sum([mono_weights[j] for j in range(len(mono)) if mono[j] in k]) for k in glycans]
    di_scores = [sum([di_weights[j] for j in range(len(di)) if subgraph_isomorphism(k, di[j],
                                                                                    libr = libr)]) for k in glycans]
    #for each glycan, get their glycoletter & disaccharide scores, normalized by glycan length  
    motif_scores = [a + b for a, b in zip(mono_scores, di_scores)]
    length_scores = [len(k) for k in glycans]

    combined_scores = [motif_scores[k] / length_scores[k] for k in range(len(motif_scores))]
    df_score = pd.DataFrame(list(zip(glycans, motif_scores, length_scores, combined_scores)),
                        columns = ['glycan', 'motif_score', 'length_score', 'combined_score'])
    df_score = df_score.sort_values(by = 'combined_score',
                                    ascending = False)
    #take the 10 glycans with the highest score
    rep_motifs = df_score.glycan.values.tolist()[:10]
    rep_motifs.sort(key = len)

    clean_list = []
    #make sure that the list only contains the minimum number of representative glycans
    for k in rep_motifs:
        if sum([subgraph_isomorphism(j, k, libr = libr) for j in rep_motifs]) > 1:
            rep_motifs.remove(k)
        else:
            clean_list.append(k)
    return clean_list

def clean_up_heatmap(df):
  df.index = [k+' '*20 if k in motif_list.motif_name else k for k in df.index]
  # Group the DataFrame by identical rows
  grouped = df.groupby(list(df.columns))
  # Find the row with the longest string index within each group and return a new DataFrame
  result = pd.concat(
        [
            group.loc[group.index.to_series().str.len().idxmax()]
            for _, group in grouped
        ],
        axis = 1,
    ).T
  result.index = [k.strip() for k in result.index]
  return result

def make_heatmap(df, mode = 'sequence', feature_set = ['known'],
                 extra = 'termini', wildcard_list = [], datatype = 'response',
                 rarity_filter = 0.05, filepath = '', index_col = 'target',
                 estimate_speedup = False, **kwargs):
  """clusters samples based on glycan data (for instance glycan binding etc.)\n
  | Arguments:
  | :-
  | df (dataframe): dataframe with glycan data, rows are samples and columns are glycans
  | mode (string): whether glycan 'sequence' or 'motif' should be used for clustering; default:sequence
  | feature_set (list): which feature set to use for annotations, add more to list to expand; default is 'exhaustive'; options are: 'known' (hand-crafted glycan features), 'graph' (structural graph features of glycans), 'exhaustive' (all mono- and disaccharide features), 'terminal' (non-reducing end motifs), and 'chemical' (molecular properties of glycan)
  | extra (string): 'ignore' skips this, 'wildcards' allows for wildcard matching', and 'termini' allows for positional matching; default:'termini'
  | wildcard_list (list): list of wildcard names (such as '?1-?', 'Hex', 'HexNAc', 'Sia')
  | datatype (string): whether df comes from a dataset with quantitative variable ('response') or from presence_to_matrix ('presence')
  | rarity_filter (float): proportion of samples that need to have a non-zero value for a variable to be included; default:0.05
  | filepath (string): absolute path including full filename allows for saving the plot
  | index_col (string): default column to convert to dataframe index; default:'target'
  | estimate_speedup (bool): if True, pre-selects motifs for those which are present in glycans, not 100% exact; default:False
  | **kwargs: keyword arguments that are directly passed on to seaborn clustermap\n                          
  | Returns:
  | :-
  | Prints clustermap                         
  """
  if index_col in df.columns:
      df.set_index(index_col, inplace = True)
  df.fillna(0, inplace = True)
  if mode == 'motif':
      #count glycan motifs and remove rare motifs from the result
      df_motif = annotate_dataset(df.columns.tolist(),
                              feature_set = feature_set,
                                  extra = extra, wildcard_list = wildcard_list,
                                  estimate_speedup = estimate_speedup)
      df_motif = df_motif.replace(0,np.nan).dropna(thresh = np.max([np.round(rarity_filter * df_motif.shape[0]), 1]), axis = 1)
      collect_dic = {}
      #distinguish the case where the motif abundance is paired to a quantitative value or a qualitative variable
      if datatype == 'response':
        for col in df_motif.columns:
          indices = [i for i, x in enumerate(df_motif[col]) if x >= 1]
          temp = df.iloc[:, indices].sum(axis = 1)
          collect_dic[col] = temp
        df = pd.DataFrame(collect_dic)
      elif datatype == 'presence':
        idx = df.index.tolist()
        collecty = [[np.sum(df.iloc[row, [i for i, x in enumerate(df_motif[col]) if x >= 1]])/df.iloc[row, :].values.sum() for col in df_motif.columns] for row in range(df.shape[0])]
        df = pd.DataFrame(collecty)
        df.columns = df_motif.columns
        df.index = idx
  df.dropna(axis = 1, inplace = True)
  df = clean_up_heatmap(df.T)
  #cluster the motif abundances
  sns.clustermap(df, **kwargs)
  plt.xlabel('Samples')
  if mode == 'sequence':
      plt.ylabel('Glycans')
  else:
      plt.ylabel('Motifs')
  plt.tight_layout()
  if len(filepath) > 1:
      plt.savefig(filepath, format = filepath.split('.')[-1], dpi = 300,
                  bbox_inches = 'tight')
  plt.show()

def plot_embeddings(glycans, emb = None, label_list = None,
                    shape_feature = None, filepath = '', alpha = 0.8,
                    palette = 'colorblind',
                    **kwargs):
    """plots glycan representations for a list of glycans\n
    | Arguments:
    | :-
    | glycans (list): list of IUPAC-condensed glycan sequences as strings
    | emb (dictionary): stored glycan representations; default takes them from trained species-level SweetNet model
    | label_list (list): list of same length as glycans if coloring of the plot is desired
    | shape_feature (string): monosaccharide/bond used to display alternative shapes for dots on the plot
    | filepath (string): absolute path including full filename allows for saving the plot
    | alpha (float): transparency of points in plot; default:0.8
    | palette (string): color palette to color different classes; default:'colorblind'
    | **kwargs: keyword arguments that are directly passed on to matplotlib\n
    """
    idx = [k for k in range(len(glycans)) if '{' not in glycans[k]]
    glycans = [glycans[k] for k in idx]
    label_list = [label_list[k] for k in idx]
    #get all glycan embeddings
    if emb is None:
        this_dir, this_filename = os.path.split(__file__) 
        data_path = os.path.join(this_dir, 'glycan_representations.pkl')
        emb = pickle.load(open(data_path, 'rb'))
    #get the subset of embeddings corresponding to 'glycans'
    if isinstance(emb, pd.DataFrame):
        emb = {glycan[k]:emb.iloc[k,:] for k in range(len(glycans))}
    embs = np.array([emb[k] for k in glycans])
    #calculate t-SNE of embeddings
    embs = TSNE(random_state = 42,
                init = 'pca', learning_rate = 'auto').fit_transform(embs)
    #plot the t-SNE
    markers = None
    if shape_feature is not None:
        markers = {shape_feature: "X", "Absent": "o"}
        shape_feature = [shape_feature if shape_feature in k else 'Absent' for k in glycans]
    sns.scatterplot(x = embs[:,0], y = embs[:,1], hue = label_list,
                    palette = palette, style = shape_feature, markers = markers,
                    alpha = alpha, **kwargs)
    sns.despine(left = True, bottom = True)
    plt.xlabel('Dim1')
    plt.ylabel('Dim2')
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.)
    plt.tight_layout()
    if len(filepath) > 1:
      plt.savefig(filepath, format = filepath.split('.')[-1], dpi = 300,
                  bbox_inches = 'tight')
    plt.show()

def characterize_monosaccharide(sugar, df = None, mode = 'sugar', glycan_col_name = 'target',
                                rank = None, focus = None, modifications = False,
                                filepath = '', thresh = 10):
  """for a given monosaccharide/linkage, return typical neighboring linkage/monosaccharide\n
  | Arguments:
  | :-
  | sugar (string): monosaccharide or linkage
  | df (dataframe): dataframe to use for analysis; default:df_species
  | mode (string): either 'sugar' (connected monosaccharides), 'bond' (monosaccharides making a provided linkage), or 'sugarbond' (linkages that a provided monosaccharides makes); default:'sugar'
  | glycan_col_name (string): column name under which glycans can be found; default:'target'
  | rank (string): add column name as string if you want to filter for a group
  | focus (string): add row value as string if you want to filter for a group
  | modifications (bool): set to True if you want to consider modified versions of a monosaccharide; default:False
  | filepath (string): absolute path including full filename allows for saving the plot
  | thresh (int): threshold count of when to include motifs in plot; default:10 occurrences\n
  | Returns:
  | :-
  | Plots modification distribution and typical neighboring bond/monosaccharide
  """
  if df is None:
    df = df_species
  if rank is not None:
    df = df[df[rank] == focus]
  #get all disaccharides for linkage analysis
  pool_in = unwrap([link_find(k) for k in df[glycan_col_name].values.tolist()])
  pool_in = [k.replace('(', '*').replace(')', '*') for k in pool_in]

  if mode == 'bond':
    #get upstream monosaccharides for a specific linkage
    pool = [k.split('*')[0] for k in pool_in if k.split('*')[1] == sugar]
    lab = 'Observed Monosaccharides Making Linkage %s' % sugar
  elif mode == 'sugar':
    #get downstream monosaccharides for a specific monosaccharide
    if modifications:
      sugars = [k.split('*')[0] for k in pool_in if sugar in k.split('*')[0]]
      pool = [k.split('*')[2] for k in pool_in if sugar in k.split('*')[0]]
    else:
      pool = [k.split('*')[2] for k in pool_in if k.split('*')[0] == sugar]
    lab = 'Observed Monosaccharides Paired with %s' % sugar
  elif mode == 'sugarbond':
    #get downstream linkages for a specific monosaccharide
    if modifications:
      sugars = [k.split('*')[0] for k in pool_in if sugar in k.split('*')[0]]
      pool = [k.split('*')[1] for k in pool_in if sugar in k.split('*')[0]]
    else:
      pool = [k.split('*')[1] for k in pool_in if k.split('*')[0] == sugar]
    lab = 'Observed Linkages Made by %s' % sugar

  #count objects in pool, filter by rarity, and calculate proportion
  cou = Counter(pool).most_common()
  cou_k = [k[0] for k in cou if k[1] > thresh]
  cou_v_in = [k[1] for k in cou if k[1] > thresh]
  cou_v = [v / len(pool) for v in cou_v_in]

  #start plotting
  fig, (a0,a1) = plt.subplots(1, 2 , figsize = (8, 4), gridspec_kw = {'width_ratios': [1, 1]})
  if modifications:
      if mode == 'bond':
          print("Modifications currently only work in mode == 'sugar' and mode == 'sugarbond'.")
      #get counts and proportions for the input monosaccharide + its modifications
      cou2 = Counter(sugars).most_common()
      cou_k2 = [k[0] for k in cou2 if k[1] > thresh]
      cou_v2_in = [k[1] for k in cou2 if k[1] > thresh]
      cou_v2 = [v / len(sugars) for v in cou_v2_in]
      #map the input monosaccharide + its modifications to colors
      color_list =  plt.cm.get_cmap('tab20')
      color_map = {cou_k2[k]:color_list(k/len(cou_k2)) for k in range(len(cou_k2))}
      palette = [color_map[k] for k in cou_k2]
      #start linking downstream monosaccharides / linkages to the input monosaccharide + its modifications
      if mode == 'sugar':
          pool_in2 = [k for k in pool_in if k.split('*')[2] in cou_k]
      elif mode == 'sugarbond':
          pool_in2 = [k for k in pool_in if k.split('*')[1] in cou_k]
      cou_for_df = []
      for k in range(len(cou_k2)):
          if mode == 'sugar':
              idx = [j.split('*')[2] for j in pool_in2 if j.split('*')[0] == cou_k2[k]]
          elif mode == 'sugarbond':
              idx = [j.split('*')[1] for j in pool_in2 if j.split('*')[0] == cou_k2[k]]
          cou_t = Counter(idx).most_common()
          cou_v_t = {cou_t[j][0]:cou_t[j][1] for j in range(len(cou_t))}
          cou_v_t = [cou_v_t[j] if j in list(cou_v_t.keys()) else 0 for j in cou_k]
          if len(cou_k2) > 1:
              cou_for_df.append(pd.DataFrame({'monosaccharides':cou_k, 'counts':cou_v_t, 'colors':[cou_k2[k]]*len(cou_k)}))
          else:
              sns.barplot(x = cou_k, y = cou_v_t, ax = a1, color = "cornflowerblue")
      if len(cou_k2) > 1:
          cou_df = pd.concat(cou_for_df).reset_index(drop = True)
          sns.histplot(data = cou_df, x = 'monosaccharides', hue = 'colors', weights = 'counts',
                       multiple = 'stack', palette = palette, ax = a1, legend = False,
                   shrink = 0.8)
      a1.set_ylabel('Absolute Occurrence')
  else:
      sns.barplot(x = cou_k, y = cou_v, ax = a1, color = "cornflowerblue")
      a1.set_ylabel('Relative Proportion')
  sns.despine(left = True, bottom = True)
  a1.set_xlabel('')
  a1.set_title(str(sugar) + ' and variants are connected to')
  plt.setp(a0.get_xticklabels(), rotation = 'vertical')

  #confusingly, this second plot block refers to the *first* plot, depicting the input monosaccharide + its modifications
  if modifications:
    if len(cou_k2) > 1:
        cou_df2 = pd.DataFrame({'monosaccharides': cou_k2, 'counts': cou_v2})
        sns.histplot(data = cou_df2, x = 'monosaccharides', weights = 'counts',
                     hue = 'monosaccharides', shrink = 0.8, legend = False,
                     ax = a0, palette = palette, alpha = 0.75)
    else:
        sns.barplot(x = cou_k2, y = cou_v2, ax = a0, color = "cornflowerblue")
    sns.despine(left = True, bottom = True)
    a0.set_ylabel('Relative Proportion')
    a0.set_xlabel('')
    a0.set_title('Observed Modifications of ' + str(sugar))
    plt.setp(a1.get_xticklabels(), rotation = 'vertical')

  fig.suptitle('Characterizing ' + str(sugar))
  fig.tight_layout()
  if len(filepath) > 1:
      plt.savefig(filepath, format = filepath.split('.')[-1], dpi = 300,
                  bbox_inches = 'tight')
  plt.show()

def replace_zero_with_random_gaussian(x, mean = 0.01, std_dev = 0.01):
  if x == 0:
    return np.random.normal(loc = mean, scale = std_dev)
  else:
    return x

def get_differential_expression(df, group1, group2, normalized = True,
                                motifs = False, feature_set = ['exhaustive', 'known'], libr = None,
                                impute = False):
  """Calculates differentially expressed glycans or motifs from glycomics data\n
  | Arguments:
  | :-
  | df (dataframe): dataframe containing glycan sequences in first column and relative abundances in subsequent columns
  | group1 (list): list of column indices for the first group of samples, usually the control
  | group2 (list): list of column indices for the second group of samples
  | normalized (bool): whether the abundances are already normalized, if False, the data will be normalized by dividing by the total; default:True
  | motifs (bool): whether to analyze full sequences (False) or motifs (True); default:False
  | feature_set (list): which feature set to use for annotations, add more to list to expand; default is ['exhaustive','known']; options are: 'known' (hand-crafted glycan features), 'graph' (structural graph features of glycans), 'exhaustive' (all mono- and disaccharide features), 'terminal' (non-reducing end motifs), and 'chemical' (molecular properties of glycan)
  | libr (list): sorted list of unique glycoletters observed in the glycans of our dataset; default:uses glycowork-internal list
  | impute (bool): removes rows with too many missing values & replaces zeroes with draws from left-shifted distribution; default:False\n
  | Returns:
  | :-
  | Returns a dataframe with:
  | (i) Differentially expressed glycans/motifs
  | (ii) Log2-transformed fold change of group2 vs group1 (i.e., negative = lower in group2)
  | (iii) Corrected p-values (Welch's t-test with Holm-Sidak correction)
  | (iv) Effect size as Cohen's d
  """
  if libr is None:
    libr = lib
  if impute:
    thresh = int(round(len(group1+group2)/2))
    df = df[df.iloc[:,group1+group2].apply(lambda row: (row != 0).sum(), axis = 1) >= thresh]
    df = df.applymap(replace_zero_with_random_gaussian)
  if not normalized:
    for col in df.columns.tolist()[1:]:
      df[col] = [k/sum(df.loc[:,col])*100 for k in df.loc[:,col].values.tolist()]
  glycans = df.iloc[:,0].values.tolist()
  group1 = [df.columns.tolist()[k] for k in group1]
  group2 = [df.columns.tolist()[k] for k in group2]
  df = df.loc[:,[df.columns.tolist()[0]]+group1+group2]
  if motifs:
    df_motif = annotate_dataset(df.iloc[:,0].values.tolist(),
                                feature_set = feature_set,
                                condense = True)
    collect_dic = {}
    df = df.iloc[:,1:].T
    for col in df_motif.columns:
      indices = [i for i, x in enumerate(df_motif[col]) if x >= 1]
      temp = df.iloc[:, indices].sum(axis = 1)
      collect_dic[col] = temp
    df = pd.DataFrame(collect_dic)
    df = clean_up_heatmap(df.T)
    glycans = df.index.tolist()
  df_a = df.loc[:,group1]
  df_b = df.loc[:,group2]
  pvals = [ttest_ind(df_a.iloc[k,:], df_b.iloc[k,:], equal_var = False)[1] for k in range(len(df_a))]
  pvals = multipletests(pvals)[1]
  fc = np.log2(df_b.mean(axis = 1) / df_a.mean(axis = 1)).tolist()
  effect_sizes = [cohen_d(df_b.iloc[k,:], df_a.iloc[k,:]) for k in range(len(df_a))]
  out = [(glycans[k], fc[k], pvals[k], effect_sizes[k]) for k in range(len(glycans))]
  out = pd.DataFrame(out)
  out.columns = ['Glycan', 'Log2FC', 'corr p-val', 'Cohens d']
  out = out.dropna()
  return out.sort_values(by = 'corr p-val')

def make_volcano(df, group1, group2, normalized = True,
                                motifs = False, feature_set = ['exhaustive', 'known'], libr = None,
                                impute = False, filepath = '', y_thresh = 0.05, x_thresh = 1.0, 
                                label_changed = True, x_metric = 'Log2FC'):
  """Plots glycan differential expression results in a volcano plot\n
  | Arguments:
  | :-
  | df (dataframe): dataframe containing glycan sequences in first column and relative abundances in subsequent columns
  | group1 (list): list of column indices for the first group of samples, usually the control
  | group2 (list): list of column indices for the second group of samples
  | normalized (bool): whether the abundances are already normalized, if False, the data will be normalized by dividing by the total; default:True
  | motifs (bool): whether to analyze full sequences (False) or motifs (True); default:False
  | feature_set (list): which feature set to use for annotations, add more to list to expand; default is ['exhaustive','known']; options are: 'known' (hand-crafted glycan features), 'graph' (structural graph features of glycans), 'exhaustive' (all mono- and disaccharide features), 'terminal' (non-reducing end motifs), and 'chemical' (molecular properties of glycan)
  | libr (list): sorted list of unique glycoletters observed in the glycans of our dataset; default:uses glycowork-internal list
  | impute (bool): removes rows with too many missing values & replaces zeroes with draws from left-shifted distribution; default:False
  | filepath (string): absolute path including full filename allows for saving the plot
  | y_thresh (float): corr p threshhold for labeling datapoints; default:0.05
  | x_thresh (float): absolute x metric threshold for labeling datapoints; defualt:1.0
  | label_changed (bool): if True, add text labels to significantly up- and downregulated datapoints; default:True
  | x_metric (string): x-axis metric; default:'Log2FC'; options are 'Log2Fc', 'Cohens d'\n
  | Returns:
  | :-
  | Prints volcano plot
  """

  # get DE  
  de_res = get_differential_expression(df = df, group1 = group1, group2 = group2, normalized = normalized, motifs = motifs,
                                        feature_set = feature_set, libr = libr, impute = impute)
  de_res['log_p'] = -np.log10(de_res['corr p-val'].values.tolist())
  x = de_res[x_metric].values.tolist()
  y = de_res['log_p'].values.tolist()
  l = de_res['Glycan'].values.tolist()
  
  # make plot
  ax = sns.scatterplot(x = x_metric, y = 'log_p', data = de_res, color = '#3E3E3E', alpha = 0.8)
  ax.set(xlabel = x_metric, ylabel = '-log10(corr p-val)', title = '')
  plt.axhline(y = -np.log10(y_thresh), c = 'k', ls = ':', lw = 0.5, alpha = 0.3)
  plt.axvline(x = x_thresh, c = 'k', ls = ':', lw = 0.5, alpha = 0.3)
  plt.axvline(x = -x_thresh, c = 'k', ls = ':', lw = 0.5, alpha = 0.3)
  sns.despine(bottom = True, left = True)

  # text labels
  if label_changed == True:
    texts = [plt.text(x[i], y[i], l[i]) for i in range(len(x)) if y[i] > -np.log10(y_thresh) and abs(x[i]) > x_thresh]

  # save to file
  if len(filepath) > 1:
    plt.savefig(filepath, format = filepath.split('.')[-1], dpi = 300,
                    bbox_inches = 'tight')
  
  plt.show()
