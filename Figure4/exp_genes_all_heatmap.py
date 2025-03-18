#!/usr/bin/env python

import pandas as pd
import numpy as np

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

# Illustrator compatibility
new_rc_params = {'text.usetex': False, "svg.fonttype": 'none'}
matplotlib.rcParams.update(new_rc_params)

import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import ConnectionPatch
import seaborn as sns

import logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


expr = pd.read_csv('phased_symbol_logcpms.tsv', sep='\t', header=0, index_col=0).T

use_ensg = []

with open('phased.edger.lrt.symbol.tsv') as deg:
    for i, line in enumerate(deg):
        if i == 0:
            continue

        ensg,logFC,logCPM,LR,PValue,FDR = line.strip().split('\t')

        LR = float(LR)
        FDR = float(FDR)

        if abs(FDR) < 0.25:
        #if abs(LR) > 2:
            use_ensg.append(ensg)

expr = expr[use_ensg].T

lr_cols = []

for sample in expr.columns:
    if sample.split('.')[4] == 'mother':
        f_sample = sample.split('.')
        f_sample[4] = 'father'
        f_sample = '.'.join(f_sample)

        logratio = expr[sample] - expr[f_sample]

        lr_name = sample.split('.')[0] + '_LR'
        lr_cols.append(lr_name)
        expr[lr_name] = logratio
        
expr = expr[lr_cols].T

use_ensg = []

for gene in expr.columns:
    if np.mean(abs(expr[gene])) > 1:
        use_ensg.append(gene)

print('final gene count: %d' % len(use_ensg))

expr = expr[use_ensg].T


expr.to_csv('gene_expr_dmr.tsv', sep='\t')

fig = plt.figure()
clustermap = sns.clustermap(expr, cmap='vlag', vmin=-5, vmax=5, yticklabels=True, row_cluster=True, col_cluster=False)
clustermap.savefig('genes_fdr25_exprmap.svg', bbox_inches='tight')
clustermap.savefig('genes_fdr25_exprmap.png', bbox_inches='tight')

#violin = sns.violinplot(data=expr, palette='crest')
#violin.set_xticklabels(violin.get_xticklabels(), rotation=45)

#fig.savefig('genes_fdr25_dexprs_distrib.svg', bbox_inches='tight')

