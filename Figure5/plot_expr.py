#!/usr/bin/env python

import numpy as np
import pandas as pd

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

new_rc_params = {'text.usetex': False, "svg.fonttype": 'none'}
matplotlib.rcParams.update(new_rc_params)

import matplotlib.pyplot as plt

import seaborn as sns
sns.set_style('whitegrid')

from collections import defaultdict as dd

import sys

import logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


lookup_name = {}
lookup_ensg = {}
lookup_coord = {}

min_cpm = 0.0

with open('biomart_coords_genes_desc.txt') as _:
    for line in _:
        chrom, start, end, ensg, name, desc  = line.split('\t')

        if name == "":
            name = 'NA'

        if desc == "":
            desc = 'NA'

        lookup_name[ensg] = name
        lookup_coord[ensg] = [chrom, start, end]
        lookup_ensg[name] = ensg


if len(sys.argv) == 2:
    cpm = pd.read_csv('phased_ensg_logcpms.tsv', sep='\t', header=0, index_col=0)

    gene = sys.argv[1]

    if gene not in cpm.index and gene in lookup_ensg:
        gene = lookup_ensg[gene]
        logger.info(f'{gene}')

    expr = dd(dict)

    filtered = {}

    for sample in cpm.columns:
        if(cpm[sample].loc[gene]) <= min_cpm:
            filtered[sample.split('.')[0]] = True

    print(filtered)

    for sample in cpm.columns:
        if sample.split('.')[0] in filtered:
            continue

        expr[sample]['group'] = sample.split('.')[4] 
        expr[sample]['sample'] = sample.split('.')[0]
        expr[sample][gene] = cpm[sample].loc[gene]

    order = ['mother', 'father']

    expr = pd.DataFrame.from_dict(expr).T

    print(expr)

    #sns_plot = sns.swarmplot(x='group', y=gene, data=expr, order=order, hue='sample', size=10, palette='viridis')
    sns_plot = sns.pointplot(x='group', y=gene, data=expr, order=order, hue='sample', size=10, palette='viridis', dodge=0.15)
    sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=45, fontsize=12)

    for t in sns_plot.get_children():
        if str(type(t)) == "<class 'matplotlib.lines.Line2D'>":
            plt.setp(t, alpha=0.25)

    assert gene in lookup_coord

    chrom, start, end = lookup_coord[gene]
    coords = '%s:%s-%s' % (chrom, start, end)
    ylabel = '%s / %s / %s' % (coords, gene, lookup_name[gene])

    sns_plot.set_ylabel(ylabel, fontsize=12)

    fig = sns_plot.figure

    fig.set_size_inches(5,8)

    out_fn = 'expr.phased.%s.png' % lookup_name[gene]

    fig.savefig(out_fn, bbox_inches='tight')
    logger.info('plotted %s to %s' % (ylabel, out_fn)) 

