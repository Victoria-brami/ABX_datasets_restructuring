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
    old_french_data = pd.read_csv(french_name, sep=',')
    old_french_data = pd.DataFrame(old_french_data)
    old_english_data = pd.read_csv(english_name, sep=',')
    old_english_data = pd.DataFrame(old_english_data)
    for col in old_french_data.columns:
        print(col)

    new_data = dict()

    new_data['index'] = [*old_french_data['index'], *old_english_data['index']]
    new_data['#file_source'] = [*old_french_data['#file'].apply(lambda x: '1s_french/' + str(x) + '.wav'), *old_english_data['#file'].apply(lambda x: '1s_english/' + str(x) + '.wav')]
    new_data['#file_extract'] = [*old_french_data['#file'].apply(lambda x: '1s_french/' + str(x) + '.wav'),
                                *old_english_data['#file'].apply(lambda x: '1s_english/' + str(x) + '.wav')]
    new_data['onset'] = [*old_french_data['onset'], *old_english_data['onset']]
    new_data['offset'] = [*old_french_data['offset'], *old_english_data['offset']]
    new_data['#phone'] = [*old_french_data['#phone'], *old_english_data['#phone']]
    new_data['context'] = [*[old_french_data['prev-phone'][i] + '_' + old_french_data['next-phone'][i] for i in
                             range(len(old_french_data['onset']))],
                           *[old_english_data['prev-phone'][i] + '_' + old_english_data['next-phone'][i] for i in
                             range(len(old_english_data['onset']))]]

    new_data['language'] = [*['FR' for _ in range(len(old_french_data['onset']))],
                            *['EN' for _ in range(len(old_english_data['onset']))]]
    new_data['speaker'] = [*old_french_data['speaker'], *old_english_data['speaker']]

    # Specific to zerospeech dataset
    new_data['prev_phone'] = [*old_french_data['prev-phone'], *old_english_data['prev-phone']]
    new_data['next_phone'] = [*old_french_data['next-phone'], *old_english_data['next-phone']]
    new_data['dataset'] = [*['zerospeech' for _ in range(len(old_french_data['next-phone']))],
                           *['zerospeech' for _ in range(len(old_english_data['next-phone']))]]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)



def restructure_triplets_dataset_2_bis(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['individual'].apply(lambda x: 'X_' + str(x))
    new_data['subject_language'] = old_data['language'].apply(lambda x: x[:2].upper())
    new_data['triplet_id'] = old_data['filename'].apply(lambda x: 'triplet_' + x)

    new_data['TGT_item'] = old_data['TGT_item']
    new_data['OTH_item'] = old_data['OTH_item']
    new_data['X_item'] = old_data['X_item']

    new_data['TGT_first'] = old_data['TGT_first']
    new_data['user_ans'] = old_data['correct_answer']
    new_data['bin_user_ans'] = old_data['binarized_answer']

    new_data['speaker_TGT'] = old_data['speaker_tgt_oth']
    new_data['speaker_OTH'] = old_data['speaker_tgt_oth']
    new_data['speaker_X'] = old_data['speaker_x']

    new_data['language_TGT'] = old_data['filename'].apply(lambda x: x[:2].upper())
    new_data['language_OTH'] = old_data['filename'].apply(lambda x: x[:2].upper())
    new_data['language_X'] = old_data['filename'].apply(lambda x: x[:2].upper())

    new_data['phone_TGT'] = old_data['TGT']
    new_data['phone_OTH'] = old_data['OTH']
    new_data['phone_X'] = ['NA' for _ in range(len(old_data['next_phone']))]
    new_data['context'] = [old_data['prev_phone'][i] + '_' + old_data['next_phone'][i] for i in
                           range(len(old_data['next_phone']))]
    new_data['prev_phone'] = old_data['prev_phone']
    new_data['next_phone'] = old_data['next_phone']
    new_data['dataset'] = ['zerospeech' for _ in range(len(old_data['next_phone']))]

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


def build_extracted_wav_name(language, file, index):
    """

    Args:
        language: (str) either FR or EN
        file: (str) name of the source file (form 1s_french/4576.wav)
        index: (int) corresponding index in stimuli file

    Returns: 1s_french/4576_sliced_<index>.wav

    """
    if language == 'FR':
        lang = 'french'
    elif language == 'EN':
        lang = 'english'

    return '1s_{}/{}_sliced_{}.wav'.format(lang, file, index)


def try_to_link_wav_file_to_annotations():

    new_x_items = []
    new_tgt_items = []
    new_oth_items = []
    PATH_TO_DATA = '/home/coml/Documents/Victoria/'

    HUMAN_DATA = pd.read_csv(PATH_TO_DATA + 'data/zerospeech/annotation_data/zerospeech_human_experimental_data.csv')
    HUMAN_DATA = pd.DataFrame(HUMAN_DATA)
    STIMULI_FRENCH_DATA = pd.read_csv(PATH_TO_DATA + 'datasets_manipulation/interspeech-2020-perceptimatic/DATA/french/all_aligned_clean_french.csv', sep=',')
    STIMULI_FRENCH_DATA = pd.DataFrame(STIMULI_FRENCH_DATA)
    STIMULI_ENGLISH_DATA = pd.read_csv(PATH_TO_DATA + 'datasets_manipulation/interspeech-2020-perceptimatic/DATA/english/all_aligned_clean_english.csv', sep=',')
    STIMULI_ENGLISH_DATA = pd.DataFrame(STIMULI_ENGLISH_DATA)

    print([col for col in STIMULI_ENGLISH_DATA.columns])
    NB_LINES = HUMAN_DATA.count()[0]

    for i in range(NB_LINES):
        #look whether english or not (same for the 3 stimuli)
        LANGUAGE = HUMAN_DATA['language_TGT'][i]
        if LANGUAGE == 'EN':
            # TGT_SEARCHED_ROW = STIMULI_ENGLISH_DATA[STIMULI_ENGLISH_DATA['index'] == HUMAN_DATA['TGT_item'][i], '#file_extract'].values()[0]
            TGT_SEARCHED_ROW = STIMULI_ENGLISH_DATA[STIMULI_ENGLISH_DATA['index'] == HUMAN_DATA['TGT_item'][i]]
            OTH_SEARCHED_ROW = STIMULI_ENGLISH_DATA[STIMULI_ENGLISH_DATA['index'] == HUMAN_DATA['OTH_item'][i]]
            X_SEARCHED_ROW = STIMULI_ENGLISH_DATA[STIMULI_ENGLISH_DATA['index'] == HUMAN_DATA['X_item'][i]]
        elif LANGUAGE == 'FR':
            TGT_SEARCHED_ROW = STIMULI_FRENCH_DATA[STIMULI_FRENCH_DATA['index'] == HUMAN_DATA['TGT_item'][i]]
            OTH_SEARCHED_ROW = STIMULI_FRENCH_DATA[STIMULI_FRENCH_DATA['index'] == HUMAN_DATA['OTH_item'][i]]
            X_SEARCHED_ROW = STIMULI_FRENCH_DATA[STIMULI_FRENCH_DATA['index'] == HUMAN_DATA['X_item'][i]]

        print('TGT: {}'.format(TGT_SEARCHED_ROW['#file']))
        print('OTH: {}'.format(OTH_SEARCHED_ROW['#file']))
        print('X: {}'.format(X_SEARCHED_ROW['#file']))
        print()

        TGT_SEARCHED_FILE = TGT_SEARCHED_ROW['#file'].item()
        OTH_SEARCHED_FILE = OTH_SEARCHED_ROW['#file'].item()
        X_SEARCHED_FILE = X_SEARCHED_ROW['#file'].item()

        TGT_SEARCHED_INDEX = TGT_SEARCHED_ROW['index'].item()
        OTH_SEARCHED_INDEX = OTH_SEARCHED_ROW['index'].item()
        X_SEARCHED_INDEX = X_SEARCHED_ROW['index'].item()

        new_tgt_items.append(build_extracted_wav_name(LANGUAGE, TGT_SEARCHED_FILE, TGT_SEARCHED_INDEX))
        new_oth_items.append(build_extracted_wav_name(LANGUAGE, OTH_SEARCHED_FILE, OTH_SEARCHED_INDEX))
        new_x_items.append(build_extracted_wav_name(LANGUAGE, X_SEARCHED_FILE, X_SEARCHED_INDEX))

    HUMAN_DATA['TGT_item'] = new_tgt_items
    HUMAN_DATA['OTH_item'] = new_oth_items
    HUMAN_DATA['X_item'] = new_x_items

    HUMAN_DATA.to_csv(PATH_TO_DATA + 'data/zerospeech/annotation_data/zerospeech_human_experimental_data.csv')


def rename_stimuli(filename):

    STIMULI_DATA = pd.read_csv(filename)
    STIMULI_DATA = pd.DataFrame(STIMULI_DATA)

    extracted_wavs = []

    for i in range(STIMULI_DATA.count()[0]):
        source_name = STIMULI_DATA['#file_source'][i].split('.')[0]
        index = STIMULI_DATA['index'][i]

        extracted_wavs.append('{}_sliced_{}.wav'.format(source_name, index))

    STIMULI_DATA['#file_extract'] = extracted_wavs
    STIMULI_DATA.to_csv(filename)


if __name__ == '__main__':
    """ SECOND DATASET """
    PATH_TO_DATA = '/home/coml/Documents/Victoria/'
    parser = BUILD_ARGPARSE()
    args = parser.parse_args(sys.argv[1:])
    # restructure_triplets_dataset_2('../interspeech-2020-perceptimatic/DATA/human_and_models.csv',
    #                                '../../data/zerospeech/annotation_data/zerospeech_human_experimental_data.csv')

    restructure_triplets_dataset_2_bis(PATH_TO_DATA + 'datasets_manipulation/interspeech-2020-perceptimatic/DATA/all_info_french_english_last.csv',
                                   PATH_TO_DATA + 'data/zerospeech/annotation_data/zerospeech_human_experimental_data.csv')

    restructure_stimuli_csv_dataset_2(PATH_TO_DATA + 'datasets_manipulation/interspeech-2020-perceptimatic/DATA/french/all_aligned_clean_french.csv',
                                      PATH_TO_DATA + 'datasets_manipulation/interspeech-2020-perceptimatic/DATA/english/all_aligned_clean_english.csv',
                                      PATH_TO_DATA + 'data/zerospeech/annotation_data/zerospeech_stimuli.csv')

    try_to_link_wav_file_to_annotations()
    rename_stimuli(PATH_TO_DATA + 'data/zerospeech/annotation_data/zerospeech_stimuli.csv')

    print('Done')
