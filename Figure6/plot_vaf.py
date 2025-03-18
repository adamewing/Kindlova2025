#!/usr/bin/env python

import sys
import argparse

from collections import defaultdict as dd
from cyvcf2 import VCF
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


def get_vafs(vcf_fn, sample):
    vafs = []

    vcf = VCF(vcf_fn)

    c_idx = None

    for i, s in enumerate(vcf.samples):
        if s == sample:
            c_idx = i
    
    if c_idx is None:
        sys.exit('sample %s not found in vcf %s' % (args.sample, args.vcf))

    for rec in vcf:
        if rec.FILTER:
            continue

        af = rec.INFO.get('AF')

        if af is None:
            af = 0.0

        if af > 1e-5:
            continue

        if rec.gt_depths[c_idx] < 10:
            continue

        vaf = rec.gt_alt_depths[c_idx] / rec.gt_depths[c_idx]
        p = ss.binom_test(x=rec.gt_alt_depths[c_idx], n=rec.gt_depths[c_idx], p=0.5, alternative='less')

        # if vaf > 0.25:
        #     continue

        vafs.append((vaf, p))
    
    return vafs


def main(args):
    vcfs = args.vcfs.split(',')
    samples = args.samples.split(',')

    assert len(vcfs) == len(samples)

    data = dd(dict)

    for vcf, sample in zip(vcfs, samples):
        vafs = get_vafs(vcf, sample)

        som_count = 0
        gml_count = 0

        for vaf,p in vafs:
            uuid = str(uuid4())

            category = "Germline"

            if p < 0.05 and vaf < 0.5:
                category = "Somatic"
                som_count += 1
            else:
                gml_count += 1

            data[uuid]['VAF'] = vaf
            data[uuid]['Category'] = category
            data[uuid]['Sample'] = sample.split('-')[0].rstrip('a')

        logger.info('%s: Germline: %d Somatic: %d' % (sample, gml_count, som_count))

    data = pd.DataFrame.from_dict(data).T
    data = pd.DataFrame(data.to_dict())

    colours = {'Germline':'#e6c8c5', 'Somatic':'#eb4034'}
    width = 2.5 + len(samples)
    height=6

    fig = plt.figure()
    fig.set_size_inches(float(width), float(height))

    swarmplot = sns.swarmplot(x='Sample', y='VAF', hue='Category', data=data, palette=colours)
    swarmplot.set_ylim(0.0,1.0)

    fig.savefig('vafs.svg', bbox_inches='tight')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='giant bucket')
    parser.add_argument('-v', '--vcfs', required=True, help='vcfs')
    parser.add_argument('-s', '--samples', required=True, help='samples')
    args = parser.parse_args()
    main(args)
