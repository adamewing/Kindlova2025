### Figure 1a

```
methylartist segplot -s hg38.10kbp.placenta_plus_other.data.segmeth.tsv -g -m hippocampus,heart,liver,013,023,025,044,054,103,172,190 --palette magma --svg
```

### Figure 1b

```
awk '{print $1":1-"$2}' hg38.genome | xargs -n 1 -P 2 methylartist region -d placenta.tissues.data.colours.txt -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz -r Homo_sapiens_assembly38.fasta -p 32 -n CG --smoothalpha 0.6 --svg -i
```

### Figure 1c

```
awk '{print $1":1-"$2}' hg38.genome | xargs -n 1 -P 2 methylartist region -p 32 -r Homo_sapiens_assembly38.fasta -n CG -g Homo_sapiens.GRCh38.97.chr.sorted.gtf.gz --samplepalette viridis --phased -d placenta.data.txt --color_by_hp --smoothalpha 0.6 --genepalette dark:salmon --svg -i
```
