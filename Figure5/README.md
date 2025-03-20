### Figure 5a

```
methylartist locus -d placenta.data.txt -i chr1:166880144-166997452 -l 166920144-166922253 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette viridis --highlightpalette cool --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --maxmaskedfrac 0.1 --nomask --highlight_panel 0.15 --phase_labels 1:Father,2:Mother --svg
```

### Figure 5b

```
methylartist locus -d placenta.data.txt -i chr5:87228235-87350097 -l 87248235-87253720,87269637-87282994,87323024-87330097 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette viridis --highlightpalette cool --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --maxmaskedfrac 0.1 --nomask --highlight_panel 0.15 --phase_labels 1:Father,2:Mother --svg
```

### Figure 5c and d

Use `plot_expr.py gene_name`
