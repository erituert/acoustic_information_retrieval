# An Information Retrieval-based Approach for Bridging the Semantic Gap with Affective Acoustic Scene Classification (AASC)

## Introduction
This GitHub repository aims to provide the details of the methodology used to define the acoustic fingerprint of 10 different emotions by generating embeddings from acoustic events that may cause them, answering to the following question: Is it possible to characterize the acoustic events that induce emotions? 

## Summary
We use YAMNet, an acoustic events classifier trained in Audioset to classify acoustic events in the WEMAC Audiovisual stimuli dataset. Each video in this dataset is labelled with the categorical emotion it induces by crowdsourcing. Thus we determine the relevance of the acoustic events to induce each emotion, creating acoustic fingerprints of such emotions, by means of the information retrieval based
TF-IDF algorithm. 

## Dataset
We use a subset of the <a href = "https://arxiv.org/abs/2203.00456">UC3M4Safety Database Audiovisual stimuli (videos)</a>. 
The <i>Code number video</i> of the audiovisual stimuli used in this study are the following:
```
9 12 13 37 148 14 45 117 133 141 82 83 84 85 86 88 89 90 91 92 93 94 95 98 99 101 121 132 136 24 66 67 68 51 55 58 159 161 103 104 106 111 70 105 158 
```
This dataset will be also refered as *BBDDLab* for convenience at some points of the pipeline.

## Part 1: Detecting acoustic events in WEMAC Audiovisual stimuli dataset

### Required files: 
* requirements.txt
* class_labels_indices.csv
* extract_corpus_bbddlab.py
* extract_corpus_bbddlab.py
* extract_corpus_bbddlab.py
* scores_to_binary_bbddlab.py
* scores_to_binary_biosplus.py

You can create a virtual environment of your choice (conda/virtual env) and install all package dependencies with the following command:
```
pip install -r requirements.txt
```

### 1.A. Binary matrix of sound events:

The provided YAMNet outputs located in `yamnet_outputs`, have been log-scaled and binarized afterwards:
<img src="https://render.githubusercontent.com/render/math?math=y = \log_2(1 + x)">

#### Code 
Run the following python scripts to obtain the binary matrices.
```
  python scores_to_binary_bbddlab.py
  python scores_to_binary_biosplus.py
```

### 1.B. Corpus of sound events

We filter a set of classes that provide too much detail for our purposes, resulting in noisy results if not eluded. The following classes have been filtered:

* Musical instrument, Music genre, Music role and all their children.
* Domestic animals, pets, Livestock, farm animals, working animals.
* Musical ensemble was excluded from the original ontology.json because YAMNet was not trained with this class, although it is contained in the original Audioset dataset.

All children classes are referenced in the provided `ontology_noblacklist.json`.

#### Code 
Run the following python scripts to obtain the binary matrices corpus of sound events for each dataset:
```
  python extract_corpus_bbddlab.py
  python extract_corpus_biosplus.py
```


## Part 2: Applying TF-IDF to the acoustic events

### Required files: 
<ul>
  <li>class_labels_indices.csv -> Available in <i>/corpus/</i></li>
  <li>corpus_mids_220325_wemac_allemotions_all_patchhop_1.csv -> Available in <i>/corpus/uc3m4safety_stimulus/</i> </li>
  <li>01_dataset_list_video_uc3m4safety_database_2021_v01.xlsx -> To be located in <i>/corpus/</i> and available for download <a href="https://doi.org/10.21950/LUO1IZ">here</a></li>
</ul>

### Code 
In Google Colab Notebook:
```
  aasc_tdidf.ipynb
```
## Result of the Emotional Characterization of the Acoustic Scene Analysis
![Heatmap of emotion embeddings](https://github.com/erituert/acoustic_information_retrieval/blob/main/imgs/heatmap_emotions.png)

## Citing 
```bibtex
@misc{luismingueza2022acoustic,
      title={Bridging the Semantic Gap with Affective Acoustic Scene Classification: an Information Retrieval-based Approach}, 
      author={Clara Luis-Mingueza and Esther Rituerto-González and Carmen Peláez-Moreno},
      year={2022},
      publisher = {...}, 
      doi = {...},
      url = {...},
      note={submitted to Interspeech 2022}
}
```

## Authors
Esther Rituerto González, erituert [at] ing(dot)uc3m(dot)es <a href="https://github.com/erituert/">[GitHub]</a> <br />
Clara Luis Mingueza, clmingueza [at] tsc(dot)uc3m(dot)es <a href="https://github.com/clm-empatia">[GitHub]</a> <br />

## Acknowledgements 
The authors thank all the members of the UC3M4Safety for their support in the present work! 🟣
