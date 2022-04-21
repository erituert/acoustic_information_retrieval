import os
import glob
import pandas as pd
import numpy as np
from sklearn.preprocessing import Binarizer

# Variables
in_path = '/home/vocalyre/ws/empatia/interspeech_aasc_tfidf/yamnet_outputs/biospeechplus'
out_path = '/home/vocalyre/ws/empatia/interspeech_aasc_tfidf/yamnet_outputs/biospeechplus/binscores'

N_CLASSES = 521
N_SEC = 91
THR = 0.0019


def main():
    median_array = np.zeros([N_CLASSES, 1], dtype='f')
    mean_array = np.zeros([N_CLASSES, 1], dtype='f')
    percentile_array = np.zeros([N_CLASSES, 1], dtype='f')
    print(str(os.path.join(in_path)))

    for file_name in glob.glob(os.path.join(in_path, '*_allscores_patchhop_1.csv')):
        input_df = pd.read_csv(file_name)
        file_name = file_name.replace(in_path, '').replace('_allscores_patchhop_1.csv', '')
        print(file_name)

        log_scores = input_df.transform(lambda x: np.log2(1 + x))

        median_scores = log_scores.median(axis=0).to_numpy().reshape((N_CLASSES, 1))
        mean_scores = log_scores.mean(axis=0).to_numpy().reshape((N_CLASSES, 1))
        percentile_scores = log_scores.quantile(q=0.75, axis=0).to_numpy().reshape((N_CLASSES, 1))

        scores_array = log_scores.values
        transformer = Binarizer(threshold=THR).fit(scores_array)  # fit does nothing.
        bin_scores = transformer.transform(scores_array)
        bin_df = pd.DataFrame(data=bin_scores, columns=log_scores.columns)
        bin_df = bin_df.replace([np.inf, -np.inf, np.nan], 0)
        bin_df.to_csv(path_or_buf=out_path + file_name + '_binary_logscores_th0019.csv', index=False)
        print('Saved\n-----\n')

        median_array = np.append(median_array, median_scores, axis=1)
        mean_array = np.append(mean_array, mean_scores, axis=1)
        percentile_array = np.append(percentile_array, percentile_scores, axis=1)

    median_array = median_array[1:]
    mean_array = mean_array[1:]
    percentile_array = percentile_array[1:]

    print('Median:\n' + str(np.mean(median_array)))  # 6.425617124727415e-07
    print('\nMean:\n' + str(np.mean(mean_array)))  # 0.0019466115241756966
    print('\nPercentile 75:\n' + str(np.mean(percentile_array)))  # 5.359594381623166e-06


if __name__ == '__main__':
    main()
