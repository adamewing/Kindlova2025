### Supplemental Figure 1

```
awk '{print $1":1-"$2}' hg38.genome | xargs -n 1 -P 2 methylartist region -d placenta.tissues.data.colours.txt -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz -r Homo_sapiens_assembly38.fasta -p 32 -n CG --smoothalpha 0.6 --svg -i
```

### Supplemental Figure 2

```
awk '{print $1":1-"$2}' hg38.genome | xargs -n 1 -P 2 methylartist region -p 32 -r Homo_sapiens_assembly38.fasta -n CG -d PL054.PL103.ph.txt --smoothalpha 0.7 --svg --eff EMSEQ_054.m:0.904,EMSEQ_103.m:0.864 --segment_csv auto -i
```

### Supplemental Figure 3

```
awk '{print $1":1-"$2}' hg38.genome | xargs -n 1 -P 2 methylartist region -p 32 -r /home/data/ref/hg38/Homo_sapiens_assembly38.fasta -n CG -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --phased -d placenta.data.txt --color_by_hp --smoothalpha 0.6 --genepalette dark:salmon --svg -i 
```

### Supplemental Figure 4

```
ls -1 [01]*.data.txt | xargs -n 1 -P 8 methylartist region -p 16 -r /home/data/ref/hg38/Homo_sapiens_assembly38.fasta -n CG -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --phased --color_by_hp --smoothalpha 0.7 --genepalette dark:salmon --svg -i chrX:1-156040895 -d
```

### Supplemental Figure 5

```
methylartist/methylartist locus -i chrX:73,774,608-73,864,510 -l chrX:73850158-73852683 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette vi
ridis --highlightpalette cool --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --highlight_alpha 0.15 --maxmaskedfrac 0.15 --nomask --phase_labels 1:Father,2:Moth
er --maxmaskedfrac 0.9 --panelratios 3,5,1,3,3 --exonheight 1.2 --readmarkersize 4.0 --svg -d
```

### Supplemental Figure 6

```
methylartist region -p 16 -r /home/data/ref/hg38/Homo_sapiens_assembly38.fasta -n CG -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --phased -d placenta.data.txt --color_by_hp --smoothalpha 0.6 --genepalette dark:salmon --genes dmr_assoc_genes.txt --highlight_alpha 1.0 --highlight_bed curation/dmr_colour_by_novelty.bed --highlight_centerline 2 --scale_fullwidth 248956422 --svg -s 1642 --modspace 273 -i
```

### Supplemental Figure 7

```
methylartist locus -d placenta.data.txt -i chr19:53626141-53765585 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette viridis --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --maxmaskedfrac 0.1 --nomask --highlight_alpha 0.15 --phase_labels 1:Father,2:Mother -p 2,5,1,3,3 --nticks 6 -c all.merged.rna.father.bam,all.merged.rna.mother.bam --coverpalette viridis
```

### Supplemental Figure 8a

```
methylartist composite -d placenta.data.txt -s sst1.chr19.lowdiv.left_array.bed -r Homo_sapiens_assembly38.fasta -t sst1.cons.fa -p 32 --phased --color_by_phase --mincalls 50 --meanplot_cutoff 10 -c viridis --svg
```

### Supplemental Figure 8b

```
methylartist locus -d placenta.data.txt -i chr19:36255508-36269220 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --highlightpalette magma --phased --ignore_ps --color_by_hp --smoothalpha 0.6 --maxmaskedfrac 0.1 --nomask --highlight_alpha 0.15 --bed sst1_chr19.bed -l 36259508-36265220 -p 2,5,1,3,3 -c all.merged.rna.father.bam,all.merged.rna.mother.bam --coverpalette viridis
```

### Supplemental Figure 8c

See Figure5c/d for relevant script (`plot_exprs.py`)

### Supplemental Figure 9

See folder for SupplementalFigure9

### Supplemental Figures 10 and 11

```
/home/taewing/methylartist/methylartist locus -d placenta.data.txt -i $INTERVAL -l $HIGHLIGHT --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette viridis --highlightpalette cool --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --maxmaskedfrac 0.1 --nomask --highlight_panel 0.15 --phase_labels 1:Father,2:Mother --svg -c all.merged.rna.father.bam,all.merged.rna.mother.bam --coverpalette viridis
```
