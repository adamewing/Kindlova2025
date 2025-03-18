#!/usr/bin/env python

import pandas as pd
import numpy as np
from collections import defaultdict as dd

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

# Illustrator compatibility
new_rc_params = {'text.usetex': False, "svg.fonttype": 'none'}
matplotlib.rcParams.update(new_rc_params)

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.patches as mpatches
import seaborn as sns

import logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


data = pd.read_csv('CIBERSORTx_Adjusted.txt', sep='\t', header=0, index_col=0)
data = data.drop(['P-value', 'Correlation', 'RMSE'], axis=1)
df = data.loc[:, (data != 0).any(axis=0)]  # drop all-zero cols


colors = sns.color_palette("husl", n_colors=len(df.columns))
color_dict = dict(zip(df.columns, colors))

# Create the stacked bar chart
plt.figure(figsize=(15, 10))
ax = df.plot(kind='bar', stacked=True, figsize=(15, 10), color=[color_dict[col] for col in df.columns], edgecolor='black', linewidth=0.5, width=0.7)

# Customize the chart
plt.title('Cell Type Composition Across Placental Samples', fontsize=16)
plt.xlabel('Sample', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.xticks(rotation=45)


handles, labels = ax.get_legend_handles_labels()
plt.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1, 0.5), loc='center left', borderaxespad=0., fontsize=10)

# Adjust layout to make room for the legend
plt.subplots_adjust(right=0.75)

# Adjust layout to prevent cutoff
plt.tight_layout()


plt.savefig('ciberplot.svg', bbox_inches='tight')