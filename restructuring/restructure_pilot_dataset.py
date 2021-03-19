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


IPA_TRANSCRIPTION = {
    'aa': 'a',
    'ah': 'ʌ',
    'ae': 'æ',
    'tcl': 't̚',
    'dx': 'ɾ',
    'hh': 'h',
    'w': 'w',
    'd': 'd',
    't': 't',
    'k': 'k',
    'r': 'ɹ',
    'g': 'g',
    'n': 'n',
    'nx': 'ɾ̃',
    'hv': 'ɦ',
    'dcl': 'd̚',
    's': 's',
    'f': 'f',
    'm': 'm',
    'l': 'l',
    'iy': 'i',
    'uh': 'ʊ',
    'kcl': 'k̚',
    'uw': 'u',
    'pcl': 'p̚',
    'b': 'b',
    'p': 'p',
    'z': 'z',
    'dh': 'ð',
    'q': 'ʔ'
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
    new_data['subject_language'] = old_data['subject_language'].apply(lambda x: x.split('_')[0][:2].upper())
    new_data['triplet_id'] = old_data['tripletid'].apply(lambda x: 'triplet_' + x[1:])

    new_data['TGT_item'] = old_data['file_TGT']
    new_data['OTH_item'] = old_data['file_OTH']
    new_data['X_item'] = old_data['file_X']

    new_data['TGT_first'] = old_data['presentation_order'].apply(lambda x: x.startswith('A'))
    new_data['user_ans'] = [int(old_data['first_sound'][i] == correct_answer[i]) for i in
                            range(len(old_data['first_sound']))]
    new_data['bin_user_ans'] = [int(old_data['first_sound'][i] == correct_answer[i]) for i in
                                range(len(old_data['first_sound']))]

    new_data['speaker_TGT'] = old_data['talker_TGT']
    new_data['speaker_OTH'] = old_data['talker_OTH']
    new_data['speaker_X'] = old_data['talker_X']

    new_data['language_TGT'] = old_data['dialect_TGT'].apply(lambda x: 'EN_' + x)
    new_data['language_OTH'] = old_data['dialect_OTH'].apply(lambda x: 'EN_' + x)
    new_data['language_X'] = old_data['dialect_X'].apply(lambda x: 'EN_' + x)

    new_data['phone_TGT'] = old_data['Target phone'].apply(lambda x: IPA_TRANSCRIPTION[x])
    new_data['phone_OTH'] = old_data['Other phone'].apply(lambda x: IPA_TRANSCRIPTION[x])
    new_data['phone_X'] = old_data['phone2_X'].apply(lambda x: IPA_TRANSCRIPTION[x])
    new_data['context'] = [IPA_TRANSCRIPTION[old_data['phone1_TGT'][i]] + '_' + IPA_TRANSCRIPTION[old_data['phone3_TGT'][i]] for i in
                           range(len(old_data['phone3_TGT']))]
    new_data['prev_phone'] = old_data['phone1_TGT'].apply(lambda x: IPA_TRANSCRIPTION[x])
    new_data['next_phone'] = old_data['phone3_TGT'].apply(lambda x: IPA_TRANSCRIPTION[x])

    new_data['nb_stimuli'] = old_data['order'].apply(lambda x: x - 8)
    new_data['dataset'] = old_data['phone3_X'].apply(lambda x: 'pilot-july-2018')

    # Additional information
    new_data['gender_TGT'] = old_data['sex_TGT']
    new_data['gender_OTH'] = old_data['sex_OTH']
    new_data['gender_X'] = old_data['sex_X']

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def correct_bin_ans_july(filename):
    data = pd.read_csv(filename)
    data = pd.DataFrame(data)

    corr = [1 for _ in range(len(data['TGT_first']))]

    for i in range(len(data['TGT_first'])):
        if data['bin_user_ans'][i] == 0:
            corr[i] = -1
    data['user_ans'] = corr
    data['bin_user_ans'] = corr

    new_data = pd.DataFrame(data)
    new_data.to_csv(filename)



def restructure_stimuli_dataset_3_july(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = [*old_data['TGT_item'], *old_data['OTH_item'], *old_data['X_item']]
    new_data['#file_source'] = [*old_data['file_TGT'].apply(lambda x: x + '.WAV.wav'),
                                *old_data['file_OTH'].apply(lambda x: x + '.WAV.wav'),
                                *old_data['file_X'].apply(lambda x: x + '.WAV.wav')]
    new_data['#file_extract'] = [*old_data['TGT_filename'], *old_data['OTH_filename'], *old_data['X_filename']]
    new_data['onset'] = [*old_data['onset_TGT'], *old_data['onset_OTH'], *old_data['onset_X']]
    new_data['offset'] = [*old_data['offset_TGT'], *old_data['offset_OTH'], *old_data['offset_X']]
    new_data['#phone'] = [*old_data['Target phone'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                          *old_data['Other phone'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                          *old_data['phone2_X'].apply(lambda x: IPA_TRANSCRIPTION[x])]
    new_data['context'] = [
        *[IPA_TRANSCRIPTION[old_data['phone1_TGT'][i]] + '_' + IPA_TRANSCRIPTION[old_data['phone3_TGT'][i]] for i in range(len(old_data['phone3_TGT']))],
        *[IPA_TRANSCRIPTION[old_data['phone1_TGT'][i]] + '_' + IPA_TRANSCRIPTION[old_data['phone3_TGT'][i]] for i in range(len(old_data['phone3_TGT']))],
        *[IPA_TRANSCRIPTION[old_data['phone1_TGT'][i]] + '_' + IPA_TRANSCRIPTION[old_data['phone3_TGT'][i]] for i in range(len(old_data['phone3_TGT']))]]

    new_data['language'] = [*old_data['dialect_TGT'].apply(lambda x: 'EN_' + x),
                            *old_data['dialect_OTH'].apply(lambda x: 'EN_' + x),
                            *old_data['dialect_X'].apply(lambda x: 'EN_' + x)]
    new_data['speaker'] = [*old_data['talker_TGT'], *old_data['talker_OTH'], *old_data['talker_X']]

    new_data['prev_phone'] = [*old_data['phone1_TGT'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                              *old_data['phone1_OTH'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                              *old_data['phone1_X'].apply(lambda x: IPA_TRANSCRIPTION[x])]
    new_data['next_phone'] = [*old_data['phone3_TGT'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                              *old_data['phone3_OTH'].apply(lambda x: IPA_TRANSCRIPTION[x]),
                              *old_data['phone3_X'].apply(lambda x: IPA_TRANSCRIPTION[x])]
    new_data['dataset'] = ['pilot-july-2018' for _ in range(1, 1 + 3 * len(old_data['phoneitem_id_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)



if __name__ == '__main__':
    """ 3) THIRD DATASET (PILOTE DATASET MADE BY AMELIA AND EWAN) """

    """     A) July part    """

    ### Preprocess
    NAME = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results.csv'
    DESTINATION = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results_cleaned.csv'
    preprocess_triplets_pilot_dataset_july(NAME, DESTINATION)

    ### Merge files
    NAME_HUMAN = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/Aggregated_Results_cleaned.csv'
    NAME_META = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    DESTINATION = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'
    merge_pilot_dataset_july_information(NAME_HUMAN, NAME_META, DESTINATION)

    ### Build human responses
    NAME = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'
    DESTINATION = '../../data/pilot-july-2018/annotation_data/pilot-july-2018_human_experimental_data.csv'
    restructure_triplets_dataset_3_july(NAME, DESTINATION)
    correct_bin_ans_july(DESTINATION)

    ### Restructure stimuli dataset
    NAME_JULY_STIMULI = '../../datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information_tuned.csv'
    DESTINATION_JULY_STIMULI = '../../data/pilot-july-2018/annotation_data/pilot-july-2018_stimuli.csv'
    restructure_stimuli_dataset_3_july(NAME_JULY_STIMULI, DESTINATION_JULY_STIMULI)


    print('Done')
