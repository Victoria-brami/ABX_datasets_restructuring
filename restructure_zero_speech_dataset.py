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
            
    The zero speech dataset is almost at the final shape, there are only small changes to be done
"""

def restructure_stimuli_csv_dataset_2(french_name, english_name, destination_path=None):

    old_french_data = pd.read_table(french_name)
    old_french_data = pd.DataFrame(old_french_data)
    old_english_data = pd.read_table(english_name)
    old_english_data = pd.DataFrame(old_english_data)
    for col in old_french_data.columns:
        print(col)

    new_data = dict()

    new_data['index'] = [*old_french_data['index'], *old_english_data['index']]
    new_data['#file'] = [*old_french_data['#file'], *old_english_data['#file']]
    new_data['onset'] = [*old_french_data['onset'], *old_english_data['onset']]
    new_data['offset'] = [*old_french_data['offset'], *old_english_data['offset']]
    new_data['#phone'] = [*old_french_data['#phone'], *old_english_data['#phone']]
    new_data['context'] = [*[old_french_data['prev-phone'] + '_' + old_french_data['next-phone'] for i in range(len(old_french_data['onset']))],
                           *[old_english_data['prev-phone'] + '_' + old_english_data['next-phone'] for i in range(len(old_english_data['onset']))]]

    new_data['language'] = [*['FR' for i in range(len(old_french_data['onset']))],
                            *['EN'for i in range(len(old_english_data['onset']))]]
    new_data['speaker'] = [*old_french_data['speaker'], *old_english_data['speaker']]

    # Specific to zerospeech dataset
    new_data['prev_phone'] =[*old_french_data['prev-phone'], *old_english_data['prev-phone']]
    new_data['next_phone'] = [*old_french_data['next-phone'], *old_english_data['next-phone']]
    new_data['dataset'] =[*['zero_speech' for i in range(len(old_french_data['next-phone']))], *['zero_speech' for i in range(len(old_english_data['next-phone']))]]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)



def restructure_triplets_dataset_2(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['individual']
    new_data['subject_language'] = old_data['language']
    new_data['triplet_id'] = old_data['filename']

    new_data['TGT_item'] = old_data['TGT_item']
    new_data['OTH_item'] = old_data['OTH_item']
    new_data['X_item'] = old_data['X_item']

    new_data['corr_ans'] = old_data['TGT_first'] # Equals to A if True, B otherwise
    new_data['user_ans'] =  old_data['correct_answer']
    new_data['bin_user_ans'] =  old_data['binarized_answer']


    new_data['speaker_TGT'] = old_data['speaker_tgt_oth']
    new_data['speaker_OTH'] = old_data['speaker_tgt_oth']
    new_data['speaker_X'] = old_data['speaker_x']

    new_data['language_TGT'] = [old_data['filename'][i][:2] for i in range(len(old_data['next_phone']))]
    new_data['language_OTH'] = [old_data['filename'][i][:2] for i in range(len(old_data['next_phone']))]
    new_data['language_X'] = [old_data['filename'][i][:2] for i in range(len(old_data['next_phone']))]

    new_data['phone_TGT'] = old_data['TGT']
    new_data['phone_OTH'] = old_data['OTH']
    new_data['phone_X'] = ['NA' for i in range(len(old_data['next_phone']))]
    new_data['context'] = [old_data['prev_phone'][i] + '_' + old_data['next_phone'][i] for i in range(len(old_data['next_phone']))]
    new_data['prev_phone'] = old_data['prev_phone']
    new_data['next_phone'] = old_data['next_phone']
    new_data['dataset'] = ['zero_speech' for i in range(len(old_data['next_phone']))]

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

    """ SECOND DATASET """
    parser = BUILD_ARGPARSE()
    args = parser.parse_args(sys.argv[1:])
    restructure_triplets_dataset_2('../interspeech-2020-perceptimatic/DATA/human_and_models.csv', '../Cognitive_ML_datasets/data/zero_speech_dataset_human_experimental_results.csv')

    restructure_stimuli_csv_dataset_2('../interspeech-2020-perceptimatic/DATA/french/all_aligned_clean_french.csv',
                                      '../interspeech-2020-perceptimatic/DATA/english/all_aligned_clean_english.csv',
                                      '../Cognitive_ML_datasets/data/zero_speech_dataset_stimuli.csv')
    print('Done')