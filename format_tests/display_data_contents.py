import pandas as pd
import os.path as osp
import argparse
from random import randint

PATH_TO_DATA_FOLDER = '/home/coml/Documents/Victoria/data'

CSV_PATH_NAME_1 = osp.join(PATH_TO_DATA_FOLDER, 'cogsci-2019/annotation_data/cogsci-2019_human_experimental_data.csv')
CSV_FILE_1 = pd.read_csv(CSV_PATH_NAME_1)
CSV_FILE_1 = pd.DataFrame(CSV_FILE_1)

CSV_PATH_NAME_2 = osp.join(PATH_TO_DATA_FOLDER, 'zerospeech/annotation_data/zerospeech_human_experimental_data.csv')
CSV_FILE_2 = pd.read_csv(CSV_PATH_NAME_2)
CSV_FILE_2 = pd.DataFrame(CSV_FILE_2)

CSV_PATH_NAME_3 = osp.join(PATH_TO_DATA_FOLDER, 'pilot-july-2018/annotation_data/pilot-july-2018_human_experimental_data.csv')
CSV_FILE_3 = pd.read_csv(CSV_PATH_NAME_3)
CSV_FILE_3 = pd.DataFrame(CSV_FILE_3)

CSV_PATH_NAME_4 = osp.join(PATH_TO_DATA_FOLDER, 'pilot-aug-2018/annotation_data/pilot-aug-2018_human_experimental_data.csv')
CSV_FILE_4 = pd.read_csv(CSV_PATH_NAME_4)
CSV_FILE_4 = pd.DataFrame(CSV_FILE_4)


CSV_STIMULI_PATH_NAME_1 = osp.join(PATH_TO_DATA_FOLDER, 'cogsci-2019/annotation_data/cogsci-2019_stimuli.csv')
CSV_STIMULI_FILE_1 = pd.read_csv(CSV_STIMULI_PATH_NAME_1)
CSV_STIMULI_FILE_1 = pd.DataFrame(CSV_STIMULI_FILE_1)

CSV_STIMULI_PATH_NAME_2 = osp.join(PATH_TO_DATA_FOLDER, 'zerospeech/annotation_data/zerospeech_stimuli.csv')
CSV_STIMULI_FILE_2 = pd.read_csv(CSV_STIMULI_PATH_NAME_2)
CSV_STIMULI_FILE_2 = pd.DataFrame(CSV_STIMULI_FILE_2)

CSV_STIMULI_PATH_NAME_3 = osp.join(PATH_TO_DATA_FOLDER, 'pilot-july-2018/annotation_data/pilot-july-2018_stimuli.csv')
CSV_STIMULI_FILE_3 = pd.read_csv(CSV_STIMULI_PATH_NAME_3)
CSV_STIMULI_FILE_3 = pd.DataFrame(CSV_STIMULI_FILE_3)

CSV_STIMULI_PATH_NAME_4 = osp.join(PATH_TO_DATA_FOLDER, 'pilot-aug-2018/annotation_data/pilot-aug-2018_stimuli.csv')
CSV_STIMULI_FILE_4 = pd.read_csv(CSV_STIMULI_PATH_NAME_4)
CSV_STIMULI_FILE_4 = pd.DataFrame(CSV_STIMULI_FILE_4)


def display_format():
    INDEX = randint(0, 1500)
    print('Index: ', INDEX)
    print()
    parser = argparse.ArgumentParser()
    parser.add_argument('--key_list', type=list, default=['nb_stimuli'])
    args = parser.parse_args()

    for key in args.key_list:
        print('COGSCI 2019')
        print('   {}: {}'.format(key, CSV_FILE_1[key][INDEX]), type(CSV_FILE_1[key][INDEX]))
        print('ZEROSPEECH')
        print('   {}: {}'.format(key, CSV_FILE_2[key][INDEX]), type(CSV_FILE_2[key][INDEX]))
        print('PILOT JULY 2018')
        print('   {}: {}'.format(key, CSV_FILE_3[key][INDEX]), type(CSV_FILE_3[key][INDEX]))
        print('PILOT AUGUST 2018')
        print('   {}: {}'.format(key, CSV_FILE_4[key][INDEX]), type(CSV_FILE_4[key][INDEX]))
        print()

def display_stimuli_format():
    INDEX = randint(0, 400)
    INDEX = 191
    print('Index: ', INDEX)
    print()
    parser = argparse.ArgumentParser()
    parser.add_argument('--key_list', type=list, default=['dataset'])
    args = parser.parse_args()

    for key in args.key_list:
        print('COGSCI 2019')
        print('   {}: {}'.format(key, CSV_STIMULI_FILE_1[key][INDEX]), type(CSV_STIMULI_FILE_1[key][INDEX]))
        print('ZEROSPEECH')
        print('   {}: {}'.format(key, CSV_STIMULI_FILE_2[key][INDEX]), type(CSV_STIMULI_FILE_2[key][INDEX]))
        print('PILOT JULY 2018')
        print('   {}: {}'.format(key, CSV_STIMULI_FILE_3[key][INDEX]), type(CSV_STIMULI_FILE_3[key][INDEX]))
        print('PILOT AUGUST 2018')
        print('   {}: {}'.format(key, CSV_STIMULI_FILE_4[key][INDEX]), type(CSV_STIMULI_FILE_4[key][INDEX]))
        print()


if __name__ == '__main__':
    display_format()
    # display_stimuli_format()