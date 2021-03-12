import pandas as pd
import argparse
import sys

""" 
    This file aims to restructure several datasets into the format given by Zero Resource Speech Challenge 2017
    This latter is composed of:
        - sound data: each stimuli in a separate .wav folder
        - labels:
            1) A list of all the triplets and their characteristics (all_triplets.csv)
            2) Information related to each stimuli (row per row, each stimulae indexed): onset an offset especially
            3) Human answers on those triplets tests.
"""


def restructure_stimuli_csv_dataset_1(french_name, destination_path=None):
    old_data = pd.read_csv(french_name, sep=';')
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = old_data['indexnumber']
    new_data['#file'] = old_data['int_filename']
    new_data['onset'] = old_data['onset']
    new_data['offset'] = old_data['offset']
    new_data['#phone'] = old_data['vowel']
    new_data['context'] = old_data['context']

    new_data['language'] = [old_data['language'][i][:2] for i in range(len(old_data['language']))]
    new_data['speaker'] = old_data['speaker']
    new_data['dataset'] = ['ABX_Cogsci' for _ in range(len(old_data['context']))]

    # Specific to zerospeech dataset
    new_data['prev_phone'] = [old_data['context'][i].split('_')[0] for i in range(len(old_data['context']))]
    new_data['next_phone'] = [old_data['context'][i].split('_')[1] for i in range(len(old_data['context']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_triplets_dataset_1(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['subject_id']
    new_data['subject_language'] = old_data['subject_language.x']
    new_data['triplet_id'] = [i for i in range(len(old_data['subject_id']))]

    new_data['TGT_item'] = old_data['file_TGT']
    new_data['OTH_item'] = old_data['file_OTH']
    new_data['X_item'] = old_data['file_X']

    new_data['corr_ans'] = [old_data['corr_ans'][i][:1] for i in
                            range(len(old_data['subject_id']))]  # Equals to A if True, B otherwise
    new_data['user_ans'] = old_data['user_resp']
    new_data['bin_user_ans'] = old_data['user_resp']

    new_data['speaker_TGT'] = old_data['speaker_TGT']
    new_data['speaker_OTH'] = old_data['speaker_OTH']
    new_data['speaker_X'] = old_data['speaker_X']

    new_data['language_TGT'] = [old_data['file_TGT'][i].split('_')[1] for i in range(len(old_data['file_TGT']))]
    new_data['language_OTH'] = [old_data['file_OTH'][i].split('_')[1] for i in range(len(old_data['file_OTH']))]
    new_data['language_X'] = [old_data['file_X'][i].split('_')[1] for i in range(len(old_data['file_X']))]

    new_data['phone_TGT'] = old_data['vowel_TGT']
    new_data['phone_OTH'] = old_data['vowel_OTH']
    new_data['phone_X'] = old_data['vowel_X']
    new_data['context'] = old_data['context']
    new_data['prev_phone'] = [old_data['context'][i].split('_')[0] for i in range(len(old_data['context']))]
    new_data['next_phone'] = [old_data['context'][i].split('_')[-1] for i in range(len(old_data['context']))]
    new_data['dataset'] = ['cogsci-2019' for _ in range(len(old_data['context']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def BUILD_ARGPARSE():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--initial_file',
                        help="File from which you want to extract data",
                        type=str)
    parser.add_argument('--destination_file',
                        help="Name of the restructured file",
                        type=str)

    return parser


if __name__ == '__main__':
    """ First DATASET """

    parser = BUILD_ARGPARSE()
    args = parser.parse_args(sys.argv[1:])
    restructure_triplets_dataset_1(
        '../CogSci-2019-Unsupervised-speech-and-human-perception/experiment/analysis/outputs/experiment_data.csv',
        '../Cognitive_ML_datasets/data/cogsci_abx/abx_cogsci_dataset_human_experimental_data.csv')
    restructure_stimuli_csv_dataset_1('../CogSci-2019-Unsupervised-speech-and-human-perception/stimulus_meta.csv',
                                      '../Cognitive_ML_datasets/data/cogsci_abx/abx_cogsci_dataset_stimuli.csv')

    print('Done')
