# An Information Retrieval-based Approach for Bridging the Semantic Gap with Affective Acoustic Scene Classification (AASC)

### Introduction
This GitHub subrepository aims to provide the details of the methodology used to define the acoustic fingerprint of emotions by generating embeddings from acoustic
events that may cause them, answering to the following question: Is it possible to characterize the acoustic events that induce emotions? 

### Summary
We use YAMNet, an acoustic events classifier trained in Audioset to classify acoustic events in the WEMAC Audiovisual stimuli dataset. Each video in this dataset is labelled with the categorical emotion it induces by crowdsourcing. Thus we determine the relevance of the acoustic events to induce each emotion, creating acoustic fingerprints of such emotions, by means of the information retrieval based
TF-IDF algorithm. 

### Part 1: Detecting acoustic events in WEMAC Audiovisual stimuli dataset

...

### Part 2: Applying tf-idf in acoustic events in WEMAC Audiovisual stimuli dataset

Required files: 
```
 class_labels_indices.csv
 corpus_mids_220325_wemac_allemotions_all_patchhop_1.csv
 wemac_summer.csv 
```

Code in Google Colab Notebook:
```
 aasc_tdidf.ipynb
```
## Result
![Heatmap of emotion embeddings](https://github.com/erituert/acoustic_information_retrieval/imgs/heatmap_emotions.png)

## Notes
Please note that this GitHub repository is subject to changes. Contact the corresponding authors for any request.

## Authors
Esther Rituerto González, erituert [at] ing(dot)uc3m(dot)es <a href="https://github.com/erituert/">[GitHub]</a> <br />
Clara Luis Mingueza, cluis [at] pa(dot)uc3m(dot)es <a href="https://github.com/clm-empatia">[GitHub]</a> <br />

## Acknowledgements 
The authors thank all the members of the UC3M4Safety for their support in the present work! 🟣
