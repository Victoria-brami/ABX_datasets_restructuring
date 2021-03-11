import pandas as pd

""" 
    This file aims to restructure several datasets into the format given by Zero Resource Speech Challenge 2017
    This latter is composed of:
        - sound data: each stimuli in a separate .wav folder
        - labels:
            1) A list of all the triplets and their characteristics (all_triplets.csv)
            2) Information related to each stimuli (row per row, each stimulae indexed): onset an offset especially
            3) Human answers on those triplets tests.
"""

phone_word_dict = {
    'f': 'F',
    't': 'T',
    'k': 'K',
    'p': 'P',
    'i': 'HEE',
    'u': 'WHO',
    'ÊŒ': 'HUH',
    'ÊŠ': 'HOO',
    'É‘': 'HA',
    'ɑ': 'HA',
    'Ã¦': 'HAE',
    'Î': 'TH',
    'θ': 'TH',
    'ʃ': 'SH',
    's': 'SS',
    'æ': 'HAE',
    'ʊ': 'HOO',
    'ʌ': 'HUH',
    'Êƒ': 'SH'
}


def restructure_triplets_dataset_3_july(name, destination_path=None):

    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['subject_id']
    new_data['subject_language'] = old_data['subject_language']
    new_data['triplet_id'] = old_data['tripletid']

    new_data['TGT_item'] = old_data['item_TGT']
    new_data['OTH_item'] = old_data['item_OTH']
    new_data['X_item'] = old_data['item_X']

    new_data['corr_ans'] = [old_data['CORR_ANS'][i][:1] for i in range(len(old_data['subject_id']))]
    new_data['user_ans'] = old_data['user_corr'] # old_data['user_resp']
    new_data['bin_user_ans'] = old_data['user_corr']


    new_data['speaker_TGT'] = old_data['speaker_TGT']
    new_data['speaker_OTH'] = old_data['speaker_OTH']
    new_data['speaker_X'] = old_data['speaker_X']

    new_data['language_TGT'] = old_data['subject_language.y']
    new_data['language_OTH'] = old_data['subject_language.y']
    new_data['language_X'] = old_data['subject_language.y']

    new_data['phone_TGT'] = old_data['phone_TGT']
    new_data['phone_OTH'] = old_data['phone_OTH']
    new_data['phone_X'] = old_data['phone_X']
    new_data['context'] = old_data['context_TGT']
    new_data['prev_phone'] = ['NA' for i in range(len(old_data['file_TGT']))]
    new_data['next_phone'] = ['NA' for i in range(len(old_data['file_TGT']))]
    new_data['dataset'] = ['pilot_Aug_2018' for i in range(len(old_data['file_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)



def restructure_triplets_dataset_3_august(name, destination_path=None):

    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['subject_id']
    new_data['subject_language'] = old_data['subject_language']
    new_data['triplet_id'] = old_data['tripletid']

    new_data['TGT_item'] = old_data['item_TGT']
    new_data['OTH_item'] = old_data['item_OTH']
    new_data['X_item'] = old_data['item_X']

    new_data['corr_ans'] = [old_data['CORR_ANS'][i][:1] for i in range(len(old_data['subject_id']))]
    new_data['user_ans'] = old_data['user_corr'] # old_data['user_resp']
    new_data['bin_user_ans'] = old_data['user_corr']


    new_data['speaker_TGT'] = old_data['speaker_TGT']
    new_data['speaker_OTH'] = old_data['speaker_OTH']
    new_data['speaker_X'] = old_data['speaker_X']

    new_data['language_TGT'] = old_data['subject_language.y']
    new_data['language_OTH'] = old_data['subject_language.y']
    new_data['language_X'] = old_data['subject_language.y']

    new_data['phone_TGT'] = old_data['phone_TGT']
    new_data['phone_OTH'] = old_data['phone_OTH']
    new_data['phone_X'] = old_data['phone_X']
    new_data['context'] = old_data['context_TGT']
    new_data['prev_phone'] = ['NA' for i in range(len(old_data['file_TGT']))]
    new_data['next_phone'] = ['NA' for i in range(len(old_data['file_TGT']))]
    new_data['dataset'] = ['pilot_Aug_2018' for i in range(len(old_data['file_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_stimuli_dataset_3_july(name, destination_path=None):

    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = [i for i in range(1, 1 + 3 * len(old_data['file_X']))]
    new_data['#file'] = [*old_data['file_TGT'], *old_data['file_OTH'], *old_data['file_X']]
    new_data['onset'] = [*old_data['onset_TGT'], *old_data['onset_OTH'], *old_data['onset_X']]
    new_data['offset'] = [*old_data['offset_TGT'], *old_data['offset_OTH'], *old_data['offset_X']]
    new_data['#phone'] = [*old_data['Target phone'], *old_data['Other phone'], *old_data['phone2_X']]
    new_data['context'] = [*[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
                           *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
                           *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))]]

    new_data['language'] = [*old_data['dialect_TGT'], *old_data['dialect_OTH'], *old_data['dialect_X']]
    new_data['speaker'] = [*old_data['talker_TGT'], *old_data['talker_OTH'], *old_data['talker_X']]

    new_data['prev_phone'] = [*old_data['phone1_TGT'], *old_data['phone1_OTH'], *old_data['phone1_X']]
    new_data['next_phone'] = [*old_data['phone3_TGT'], *old_data['phone3_OTH'], *old_data['phone3_X']]
    new_data['dataset'] = ['pilote_july_2018' for i in range(1, 1 + 3 * len(old_data['phoneitem_id_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_stimuli_dataset_3_august(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = [*old_data['item_TGT'], *old_data['item_OTH'], *old_data['item_X']]
    new_data['#file'] = [*old_data['file_TGT'], *old_data['file_OTH'], *old_data['file_X']]
    new_data['onset'] = [*old_data['onset_TGT'], *old_data['onset_OTH'], *old_data['onset_X']]
    new_data['offset'] = [*old_data['offset_TGT'], *old_data['offset_OTH'], *old_data['offset_X']]
    new_data['#phone'] = [*old_data['phone_TGT'], *old_data['phone_OTH'], *old_data['phone_X']]
    new_data['context'] = [*old_data['context_TGT'], *old_data['context_OTH'], *old_data['context_X']]

    new_data['language'] = ['english' for i in range(len(old_data['CORR_ANS'])*3)]
    new_data['speaker'] = [*old_data['speaker_TGT'], *old_data['speaker_OTH'], *old_data['speaker_X']]

    new_data['prev_phone'] = ['NA' for i in range(len(old_data['CORR_ANS'])*3)]
    new_data['next_phone'] = ['NA' for i in range(len(old_data['CORR_ANS'])*3)]
    new_data['dataset'] = ['pilote_aug_2018' for i in range(len(old_data['CORR_ANS'])*3)]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)

if __name__ == '__main__':

    """ 3) THIRD DATASET (PILOTE DATASET MADE BY AMELIA AND EWAN) """
    NAME_3 = '../geomphon-perception-ABX/experiments/pilot_Aug_2018/analysis/geomphon_pilot_results_for_analysis.csv'
    DESTINATION_3 = '../Cognitive_ML_datasets/data/pilote/pilote_data_aug_2018_human_experimental_results.csv'
    # restructure_triplets_dataset_3_august(NAME_3, DESTINATION_3)

    NAME_3 = '../geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    DESTINATION_3 = '../Cognitive_ML_datasets/data/pilote/pilote_data_july_2018_stimuli.csv'
    restructure_stimuli_dataset_3_july(NAME_3, DESTINATION_3)

    NAME_3 = '../geomphon-perception-ABX/experiments/pilot_Aug_2018/stimuli/item_meta_information.csv'
    DESTINATION_3 = '../Cognitive_ML_datasets/data/pilote/pilote_data_aug_2018_stimuli.csv'
    # restructure_stimuli_dataset_3_august(NAME_3, DESTINATION_3)

    NAME_3 = '../pilote_dataset/geomphon-perception-ABX/experiments/pilot_july_2018/human_experimental_results.csv'
    DESTINATION_3 = '../Cognitive_ML_datasets/data/pilote/pilote_data_aug_2018_human_experimental_results.csv'

    print('Done')