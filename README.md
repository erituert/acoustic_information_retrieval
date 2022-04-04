# An Information Retrieval-based Approach for Bridging the Semantic Gap with Affective Acoustic Scene Classification (AASC)

[Coming soon]
![Under Construction](https://freerangestock.com/sample/112995/website-under-construction.jpg)

## Introduction
This GitHub repository aims to provide the details of the methodology used to define the acoustic fingerprint of emotions by generating embeddings from acoustic
events that may cause them, answering to the following question: Is it possible to characterize the acoustic events that induce emotions? 

## Summary
We use YAMNet, an acoustic events classifier trained in Audioset to classify acoustic events in the WEMAC Audiovisual stimuli dataset. Each video in this dataset is labelled with the categorical emotion it induces by crowdsourcing. Thus we determine the relevance of the acoustic events to induce each emotion, creating acoustic fingerprints of such emotions, by means of the information retrieval based
TF-IDF algorithm. 

## Dataset
We use a subset of the <a href = "https://arxiv.org/abs/2203.00456">UC3M4Safety Database Audiovisual stimuli (videos)</a>. 
The Video IDs used in this study are the following:
```
V01 V02 V03 V04 V05 V06 V07 V08 V09 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19 V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30 V31 V32 V33 V34 V35 V36 V37 V38 V39 V40 V41 V42 V43 V44 V45 
```
## Methodology Part 1: Detecting acoustic events in WEMAC Audiovisual stimuli dataset

...

## Mehotdology Part 2: Applying tf-idf in acoustic events in WEMAC Audiovisual stimuli dataset

Required files: 
```
 class_labels_indices.csv
 corpus_mids_220325_wemac_allemotions_all_patchhop_1.csv
 <a href="https://doi.org/10.21950/LUO1IZ">wemac_summer.csv</a>
```

Code in Google Colab Notebook:
```
 aasc_tdidf.ipynb
```
## Result of the Emotional Characterization of the Acoustic Scene Analysis
![Heatmap of emotion embeddings](https://github.com/erituert/acoustic_information_retrieval/blob/main/imgs/heatmap_emotions.png)

## Authors
Esther Rituerto González, erituert [at] ing(dot)uc3m(dot)es <a href="https://github.com/erituert/">[GitHub]</a> <br />
Clara Luis Mingueza, clmingueza [at] tsc(dot)uc3m(dot)es <a href="https://github.com/clm-empatia">[GitHub]</a> <br />

## Acknowledgements 
The authors thank all the members of the UC3M4Safety for their support in the present work! 🟣
