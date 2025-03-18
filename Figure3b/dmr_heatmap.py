#!/usr/bin/env python

import pandas as pd

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


data = pd.read_csv('per_sample_dmrs_nonzero.txt', sep='\t', header=0, index_col=0)

fig = plt.figure()
clustermap = sns.clustermap(data, cmap='coolwarm')
clustermap.savefig('clustermap.svg', bbox_inches='tight')
clustermap.savefig('clustermap.png', bbox_inches='tight')
