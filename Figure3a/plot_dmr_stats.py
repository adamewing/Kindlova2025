#!/usr/bin/env python

from collections import defaultdict as dd
from uuid import uuid4

import scipy.stats as ss
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

order = ['013', '023', '025', '044', '054', '103', '172', '190', 'NA19240']
files = [n+'.DMRs.txt' for n in order]
N=100

def main():
    data = dd(dict)

    for fn in files:
        logger.info('parsing %s' % fn)
        with open(fn) as f:
            for i, line in enumerate(f):
                if i >= N:
                    break

                line = line.strip()
                if line.endswith('areaStat'):
                    continue

                offset = 1

                if fn.startswith('NA19240'):
                    offset = 0

                chrom, start, end, length, nCG, meanMethy1, meanMethy2, diffMethy, areaStat = line.split()[offset:]

                loc = '%s:%s-%s' % (chrom, start, end)
                nCG = int(nCG)
                areaStat = float(areaStat)
                diffMethy = float(diffMethy)

                data[loc]['Sample'] = fn.split('.')[0]
                data[loc]['diffMethyl'] = diffMethy

                if diffMethy > 0:
                    data[loc]['Bias'] = 'Mother'
                
                if diffMethy < 0:
                    data[loc]['Bias'] = 'Father'

    data = pd.DataFrame.from_dict(data).T
    data = pd.DataFrame(data.to_dict())

    colours = {'Mother':'#ff7f0e', 'Father':'#1f77b4'}
    width = 2.5 + len(files)
    height=6

    fig = plt.figure()
    fig.set_size_inches(float(width), float(height))

    swarmplot = sns.swarmplot(x='Sample', y='diffMethyl', hue='Bias', data=data, palette=colours, order=order)
    swarmplot.set_ylim(-1.0,1.0)

    fig.savefig('dmr_source.png', bbox_inches='tight')
    fig.savefig('dmr_source.svg', bbox_inches='tight')

if __name__ == '__main__':
    main()

                

