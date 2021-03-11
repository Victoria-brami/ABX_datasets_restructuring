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


def preprocess_triplets_pilot_dataset_july(name, destination_path=None):
    old_data = pd.read_csv(name)
    new_data = pd.DataFrame(old_data)

    # elements to delete
    to_delete_first = new_data[new_data['tripletid'].str.startswith('attention')].index.tolist()
    to_delete_then = new_data[new_data['tripletid'].str.startswith('practice')].index.tolist()
    print(to_delete_first)
    print()
    print(to_delete_then)
    new_data = new_data.drop(to_delete_first)
    new_data = new_data.drop(to_delete_then)
    new_data['tripletid'] = new_data['tripletid'].apply(lambda x: x.split('_')[1])
    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def merge_pilot_dataset_july_information(name_human, name_meta_info, destination_path=None):
    human_data = pd.read_csv(name_human)
    human_data = pd.DataFrame(human_data)

    meta_data = pd.read_csv(name_meta_info)
    meta_data = pd.DataFrame(meta_data)

    print(len(human_data['tripletid']))
    print(len(meta_data['tripletid']))

    new_data = pd.merge(human_data, meta_data, on='tripletid')

    print(len(new_data['tripletid']))

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_triplets_dataset_3_july(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    correct_answer = old_data['presentation_order'].apply(lambda x: int(x.startswith('A')))
    print(correct_answer)

    new_data = dict()

    new_data['subject_id'] = old_data['subject_id']
    new_data['subject_language'] = old_data['subject_language'].apply(lambda x: x.split('_')[0])
    new_data['triplet_id'] = old_data['tripletid']

    new_data['TGT_item'] = old_data['file_TGT']
    new_data['OTH_item'] = old_data['file_OTH']
    new_data['X_item'] = old_data['file_X']

    new_data['corr_ans'] = correct_answer
    new_data['user_ans'] = [old_data['first_sound'][i] == correct_answer[i] for i in
                            range(len(old_data['first_sound']))]
    new_data['bin_user_ans'] = [old_data['first_sound'][i] == correct_answer[i] for i in
                                range(len(old_data['first_sound']))]

    new_data['speaker_TGT'] = old_data['talker_TGT']
    new_data['speaker_OTH'] = old_data['talker_OTH']
    new_data['speaker_X'] = old_data['talker_X']

    new_data['language_TGT'] = old_data['dialect_TGT'].apply(lambda x: 'english_' + x)
    new_data['language_OTH'] = old_data['dialect_OTH'].apply(lambda x: 'english_' + x)
    new_data['language_X'] = old_data['dialect_X'].apply(lambda x: 'english_' + x)

    new_data['phone_TGT'] = old_data['Target phone']
    new_data['phone_OTH'] = old_data['Other phone']
    new_data['phone_X'] = old_data['phone2_X']
    new_data['context'] = [old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in
                           range(len(old_data['phone3_TGT']))]
    new_data['prev_phone'] = old_data['phone1_TGT']
    new_data['next_phone'] = old_data['phone3_TGT']
    new_data['dataset'] = old_data['phone3_X'].apply(lambda x: 'pilote_july_2018')

    # Additional information
    new_data['gender_TGT'] = old_data['sex_TGT']
    new_data['gender_OTH'] = old_data['sex_OTH']
    new_data['gender_X'] = old_data['sex_X']

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
    new_data['context'] = [
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))]]

    new_data['language'] = [*old_data['dialect_TGT'], *old_data['dialect_OTH'], *old_data['dialect_X']]
    new_data['speaker'] = [*old_data['talker_TGT'], *old_data['talker_OTH'], *old_data['talker_X']]

    new_data['prev_phone'] = [*old_data['phone1_TGT'], *old_data['phone1_OTH'], *old_data['phone1_X']]
    new_data['next_phone'] = [*old_data['phone3_TGT'], *old_data['phone3_OTH'], *old_data['phone3_X']]
    new_data['dataset'] = ['pilote_july_2018' for _ in range(1, 1 + 3 * len(old_data['phoneitem_id_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


########################################################################################################################
#                                                    AUGUST 2018 DATA
########################################################################################################################

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
    new_data['user_ans'] = old_data['user_corr']  # old_data['user_resp']
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
    new_data['prev_phone'] = ['NA' for _ in range(len(old_data['file_TGT']))]
    new_data['next_phone'] = ['NA' for _ in range(len(old_data['file_TGT']))]
    new_data['dataset'] = ['pilot_Aug_2018' for _ in range(len(old_data['file_TGT']))]

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

    new_data['language'] = ['english' for _ in range(len(old_data['CORR_ANS']) * 3)]
    new_data['speaker'] = [*old_data['speaker_TGT'], *old_data['speaker_OTH'], *old_data['speaker_X']]

    new_data['prev_phone'] = ['NA' for _ in range(len(old_data['CORR_ANS']) * 3)]
    new_data['next_phone'] = ['NA' for _ in range(len(old_data['CORR_ANS']) * 3)]
    new_data['dataset'] = ['pilote_aug_2018' for _ in range(len(old_data['CORR_ANS']) * 3)]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


if __name__ == '__main__':
    """ 3) THIRD DATASET (PILOTE DATASET MADE BY AMELIA AND EWAN) """

    """     A) July part    """

    ### Preprocess
    NAME = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results.csv'
    DESTINATION = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results_cleaned.csv'
    # preprocess_triplets_pilot_dataset_july(NAME, DESTINATION)

    ### Merge files
    NAME_HUMAN = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results_cleaned.csv'
    NAME_META = '../geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    DESTINATION = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'
    # merge_pilot_dataset_july_information(NAME_HUMAN, NAME_META, DESTINATION)

    ### Build human responses
    NAME = '../geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'
    DESTINATION = '../Cognitive_ML_datasets/data/pilote/pilote_data_july_2018_human_experimental_data.csv'
    restructure_triplets_dataset_3_july(NAME, DESTINATION)

    ### Restructure stimuli dataset
    NAME_JULY_STIMULI = '../geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    DESTINATION_JULY_STIMULI = '../Cognitive_ML_datasets/data/pilote/pilote_data_july_2018_stimuli.csv'
    # restructure_stimuli_dataset_3_july(NAME_JULY_STIMULI, DESTINATION_JULY_STIMULI)

    """     B) August part    """

    NAME_3 = '../geomphon-perception-ABX/experiments/pilot_Aug_2018/analysis/geomphon_pilot_results_for_analysis.csv'
    DESTINATION_3 = '../Cognitive_ML_datasets/data/pilote/pilote_data_aug_2018_human_experimental_results.csv'
    # restructure_triplets_dataset_3_august(NAME_3, DESTINATION_3)

    NAME_AUG_STIMULI = '../geomphon-perception-ABX/experiments/pilot_Aug_2018/stimuli/item_meta_information.csv'
    DESTINATION_AUG_STIMULI = '../Cognitive_ML_datasets/data/pilote/pilote_data_aug_2018_stimuli.csv'
    # restructure_stimuli_dataset_3_august(NAME_AUG_STIMULI, DESTINATION_AUG_STIMULI)

    print('Done')
