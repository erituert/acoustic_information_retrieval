import os
import glob
import pandas as pd
import numpy as np
import difflib
import json
import csv

# Variables
in_path = './yamnet_outputs/biospeechplus/binscores/'
out_path = './corpus/biospeechplus/'
mid_parents = ['/m/04rlf', '/m/09x0r', '/m/068hy',
               '/m/0ch8v', '/m/0ghcn6', '/m/0kpv1t',
               '/t/dd00028']


# List of Audioset classes (plus all their children) that have been excluded:
# Musical instrument, Music genre, Music role,
# Domestic animals, pets, Livestock, farm animals, working animals.
# Musical ensemble was excluded from the original ontology.json because YAMNet was not trained with this class.

def main():
    id_df = pd.read_csv(in_path + 'class_labels_indices.csv')  # Read ids csv
    mids_corpus = []
    n_file = 0
    # Read Audioset Ontology file:
    with open('./ontology_noblacklist.json', 'r') as f:
        audioset_ontology = json.load(f)

    # TASK 1: From a mid parent list extract str children names
    str_children = []

    for ontology_object in audioset_ontology:
        for parent_mid in mid_parents:
            print('Appending children from parent class: ' + str(parent_mid))
            if parent_mid == ontology_object['id']:
                mid_children = ontology_object['child_ids']  # List
                for mid_child in mid_children:
                    str_child = id_df.loc[id_df['mid'] == str(mid_child), 'display_name']  # Convert to string
                    if str_child.values.size > 0:  # If exists (not empty position), append to drop afterwards
                        str_children.append(str_child.values[0])

    for ontology_object in audioset_ontology:
        for child_str in str_children:
            print('Appending children from class: ' + str(child_str))
            child_mid = id_df.loc[id_df['display_name'] == str(child_str), 'mid']  # Convert to mid
            if child_mid.values[0] == ontology_object['id']:
                mid_children_children = ontology_object['child_ids']  # List
                for mid_child in mid_children_children:
                    str_child = id_df.loc[id_df['mid'] == str(mid_child), 'display_name']  # Convert to string
                    if str_child.values.size > 0:  # If exists (not empty position), append to drop afterwards
                        str_children.append(str_child.values[0])
    print('Complete list of excluded classes:\n'+str(str_children))

    # TASK 2: For each .csv in folder, extract corpus:
    for file_name in sorted(glob.glob(os.path.join(in_path, '*_binary_logscores_th0019.csv'))):  # BIOSPLUS
        n_file += 1
        input_df = pd.read_csv(file_name)
        file_name = file_name.replace(in_path, '').replace('_binary_logscores_th0019.csv', '')
        print(file_name)

        filtered_input_df = input_df.copy()
        for child in str_children:
            if child in filtered_input_df.columns:
                if id_df['display_name'].str.contains(child).any():
                    filtered_input_df = filtered_input_df.drop([child], axis=1)  # Drop children columns
        print(file_name + '- After filtering shape:' + str(np.shape(filtered_input_df)))

        mids_list = []
        # Convert binary matrix to mid and zeros matrix:
        for label_str in list(filtered_input_df.columns):
            # Match strings from input and mid indices dataframes
            match = difflib.get_close_matches(str(label_str), list(id_df['display_name']), n=1, cutoff=0.8)
            mid_series = id_df.loc[id_df['display_name'] == ''.join(match), 'mid']
            mid_str = mid_series.to_string().split("/", 1)[1]  # get content only
            # Add MID to every 1 position in the column
            filtered_input_df.loc[filtered_input_df[label_str] == 1, label_str] = '/' + str(mid_str)

        # For each row, append mids to create the corpus
        for index, row in filtered_input_df.iterrows():
            mids_str = row.values.tolist()
            mids_str = [i for i in mids_str if i != 0]
            mids_strstr = ' '.join(mids_str)  # list of one row to string

            mids_row_list = [mids_strstr, str(n_file)]  # list of one row to string with file ref
            mids_list.append(mids_row_list)  # list of all rows

        mids_corpus.append(mids_list)

    filtered_input_df.to_csv(path_or_buf=in_path + 'biosplus_filtered_220421_logscores.csv', index=False)
    print('Saved\n-----\n')

    # Save corpus
    file = open(out_path + "corpus_mids_220421_biosplus_fear_all_patchhop_1.txt", "w")  # BBDD_LAB (ALL)
    file.write(str(mids_corpus))
    file.close()

    with open(out_path + "corpus_mids_220421_biosplus_fear_all_patchhop_1.csv", "w") as f:  # BBDD_LAB (ALL)
        wr = csv.writer(f)
        wr.writerows(mids_corpus)


if __name__ == '__main__':
    main()
