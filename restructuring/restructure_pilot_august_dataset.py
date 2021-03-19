import pandas as pd

########################################################################################################################
#                                                    AUGUST 2018 DATA
########################################################################################################################

def restructure_triplets_dataset_3_august(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['subject_id'] = old_data['subject_id']
    new_data['subject_language'] = [old_data['subject_language'][i][:2].upper() for i in
                                    range(len(old_data['subject_language']))]
    new_data['triplet_id'] = old_data['tripletid'].apply(lambda x: 'triplet_' + x[8:])

    new_data['TGT_item'] = old_data['item_TGT'].apply(lambda x: x + '.wav')
    new_data['OTH_item'] = old_data['item_OTH'].apply(lambda x: x + '.wav')
    new_data['X_item'] = old_data['item_X'].apply(lambda x: x + '.wav')

    new_data['TGT_first'] = [old_data['CORR_ANS'][i]=='A' for i in range(len(old_data['subject_id']))]
    new_data['user_ans'] = old_data['user_corr']  # old_data['user_resp']
    new_data['bin_user_ans'] = old_data['user_corr']

    new_data['speaker_TGT'] = old_data['speaker_TGT']
    new_data['speaker_OTH'] = old_data['speaker_OTH']
    new_data['speaker_X'] = old_data['speaker_X']

    new_data['language_TGT'] = [old_data['subject_language.y'][i][:2].upper() for i in
                                range(len(old_data['subject_language.y']))]
    new_data['language_OTH'] = [old_data['subject_language.y'][i][:2].upper() for i in
                                range(len(old_data['subject_language.y']))]
    new_data['language_X'] = [old_data['subject_language.y'][i][:2].upper() for i in
                              range(len(old_data['subject_language.y']))]

    new_data['phone_TGT'] = old_data['phone_TGT']
    new_data['phone_OTH'] = old_data['phone_OTH']
    new_data['phone_X'] = old_data['phone_X']
    new_data['context'] = old_data['context_TGT']
    new_data['prev_phone'] = ['NA' for _ in range(len(old_data['file_TGT']))]
    new_data['next_phone'] = ['NA' for _ in range(len(old_data['file_TGT']))]
    new_data['nb_stimuli'] = old_data['order'].apply(lambda x: int(x[:-1]) - 14)
    new_data['dataset'] = ['pilot-aug-2018' for _ in range(len(old_data['file_TGT']))]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def correct_bin_ans(filename):
    data = pd.read_csv(filename)
    data = pd.DataFrame(data)
    corr = [1 for _ in range(len(data['TGT_first']))]

    for i in range(len(data['TGT_first'])):
        if data['user_ans'][i] == 0:
            corr[i] = -1
    data['bin_user_ans'] = corr
    new_data = pd.DataFrame(data)
    new_data.to_csv(filename)


def restructure_stimuli_dataset_3_august(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = [i for i in range(1, 3*len(old_data['file_TGT'])+1)]
    new_data['#file_source'] = [*old_data['file_TGT'],
                                *old_data['file_OTH'],
                                *old_data['file_X']]
    new_data['#file_extract'] = [*old_data['item_TGT'].apply(lambda x: x + '.wav'),
                                 *old_data['item_OTH'].apply(lambda x: x + '.wav'),
                                 *old_data['item_X'].apply(lambda x: x + '.wav')]
    new_data['onset'] = [*old_data['onset_TGT'], *old_data['onset_OTH'], *old_data['onset_X']]
    new_data['offset'] = [*old_data['offset_TGT'], *old_data['offset_OTH'], *old_data['offset_X']]
    new_data['#phone'] = [*old_data['phone_TGT'], *old_data['phone_OTH'], *old_data['phone_X']]
    new_data['context'] = [*old_data['context_TGT'], *old_data['context_OTH'], *old_data['context_X']]

    new_data['language'] = ['EN' for _ in range(len(old_data['CORR_ANS']) * 3)]
    new_data['speaker'] = [*old_data['speaker_TGT'], *old_data['speaker_OTH'], *old_data['speaker_X']]

    new_data['prev_phone'] = ['NA' for _ in range(len(old_data['CORR_ANS']) * 3)]
    new_data['next_phone'] = ['NA' for _ in range(len(old_data['CORR_ANS']) * 3)]

    new_data['dataset'] = ['pilot-aug-2018' for _ in range(len(old_data['CORR_ANS']) * 3)]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)

def read_correct_ans(name, destination_path=None):

    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()
    new_data['triplet_id'] = old_data['tripletid']
    new_data['CORR_ANS'] = old_data['CORR_ANS']
    new_data['corr_ans'] = old_data['corr_ans']
    new_data['user_resp'] = old_data['user_resp']
    new_data['user_corr'] = old_data['user_corr']

    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


if __name__ == '__main__':

    PATH_TO_DATA = '/home/coml/Documents/Victoria/'
    NAME = PATH_TO_DATA + 'datasets_manipulation/geomphon-perception-ABX/experiments/pilot_Aug_2018/analysis/geomphon_pilot_results_for_analysis.csv'
    DEST = PATH_TO_DATA + 'datasets_manipulation/geomphon-perception-ABX/experiments/pilot_Aug_2018/analysis/corr_resp.csv'
    """ 3) THIRD DATASET (PILOTE DATASET MADE BY AMELIA AND EWAN) """
    read_correct_ans(NAME, DEST)
    """     B) August part    """

    NAME_3 = PATH_TO_DATA + 'datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_Aug_2018/analysis/geomphon_pilot_results_for_analysis.csv'
    DESTINATION_3 = PATH_TO_DATA + 'data/pilot-aug-2018/annotation_data/pilot-aug-2018_human_experimental_data.csv'
    restructure_triplets_dataset_3_august(NAME_3, DESTINATION_3)
    correct_bin_ans(DESTINATION_3)

    NAME_AUG_STIMULI = '../geomphon-perception-ABX/experiments/pilot_Aug_2018/stimuli/item_meta_information.csv'
    DESTINATION_AUG_STIMULI = '../../data/pilot-aug-2018/annotation_data/pilot-aug-2018_stimuli.csv'
    # restructure_stimuli_dataset_3_august(NAME_AUG_STIMULI, DESTINATION_AUG_STIMULI)

    print('Done')