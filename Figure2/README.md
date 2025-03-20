### Figure 2a

```
methylartist locus -d placenta.data.txt -i chr19:53626141-53765585 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --labelgenes --samplepalette viridis --phased --ignore_ps --color_by_hp --smoothalpha 0.7 --maxmaskedfrac 0.1 --nomask --highlight_alpha 0.15 --phase_labels 1:Father,2:Mother -p 2,5,1,3,3 --nticks 6
```

### Figure 2b
```
methylartist locus -d placenta.data.txt -i chr19:36,241,377-36,340,233 --gtf Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --highlightpalette magma --phased --ignore_ps --color_by_hp --smoothalpha 0.6 --maxmaskedfrac 0.1 --nomask --highlight_alpha 0.15 --bed sst1_chr19.bed -l 36258222-36268770 --svg -p 2,5,1,3,3
```
