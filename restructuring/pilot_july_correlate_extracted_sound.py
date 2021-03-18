import pandas as pd

PATH_TO_DATA = '/home/coml/Documents/Victoria/'

def merge_information():
    MERGED_DATA = PATH_TO_DATA + 'datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/data/merged_results_cleaned.csv'


def restructure_stimuli_dataset_3_july(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['index'] = [i for i in range(1, 1 + 3 * len(old_data['file_X']))]
    new_data['#file_source'] = [*old_data['file_TGT'].apply(lambda x: x + '.WAV.wav'),
                                *old_data['file_OTH'].apply(lambda x: x + '.WAV.wav'),
                                *old_data['file_X'].apply(lambda x: x + '.WAV.wav')]
    new_data['#file_extract'] = [*old_data['file_TGT'], *old_data['file_OTH'], *old_data['file_X']]
    new_data['onset'] = [*old_data['onset_TGT'], *old_data['onset_OTH'], *old_data['onset_X']]
    new_data['offset'] = [*old_data['offset_TGT'], *old_data['offset_OTH'], *old_data['offset_X']]
    new_data['#phone'] = [*old_data['Target phone'], *old_data['Other phone'], *old_data['phone2_X']]
    new_data['context'] = [
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))],
        *[old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))]]

    new_data['language'] = [*old_data['dialect_TGT'].apply(lambda x: 'EN_' + x),
                            *old_data['dialect_OTH'].apply(lambda x: 'EN_' + x),
                            *old_data['dialect_X'].apply(lambda x: 'EN_' + x)]
    new_data['speaker'] = [*old_data['talker_TGT'], *old_data['talker_OTH'], *old_data['talker_X']]

    new_data['prev_phone'] = [*old_data['phone1_TGT'], *old_data['phone1_OTH'], *old_data['phone1_X']]
    new_data['next_phone'] = [*old_data['phone3_TGT'], *old_data['phone3_OTH'], *old_data['phone3_X']]
    new_data['dataset'] = ['pilot-july-2018' for _ in range(1, 1 + 3 * len(old_data['phoneitem_id_TGT']))]

    new_data['phoneitem_id'] = [*old_data['phoneitem_id_TGT'],
                                *old_data['phoneitem_id_OTH'],
                                *old_data['phoneitem_id_X']]

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)

def restructure_stimuli_dataset_3_july_TGT(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['TGT_item'] = [i for i in range(1, 1 + len(old_data['file_X']))]
    new_data['#file_source'] = old_data['file_TGT'].apply(lambda x: x + '.WAV.wav')
    new_data['#file_extract'] = old_data['file_TGT']
    new_data['onset'] = old_data['onset_TGT']
    new_data['offset'] = old_data['offset_TGT']
    new_data['#phone'] = old_data['Target phone']
    new_data['context'] = [old_data['phone1_TGT'][i] + '_' + old_data['phone3_TGT'][i] for i in range(len(old_data['phone3_TGT']))]

    new_data['language'] = old_data['dialect_TGT'].apply(lambda x: 'EN_' + x)
    new_data['speaker'] = old_data['talker_TGT']

    new_data['prev_phone'] = old_data['phone1_TGT']
    new_data['next_phone'] = old_data['phone3_TGT']
    new_data['dataset'] = ['pilot-july-2018' for _ in range(1, 1 + len(old_data['phoneitem_id_TGT']))]

    new_data['phoneitem_id'] = old_data['phoneitem_id_TGT']

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_stimuli_dataset_3_july_OTH(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['OTH_item'] = [i for i in range(1 + 1 * len(old_data['file_X']), 1 + 2 * len(old_data['file_X']))]
    new_data['#file_source'] = old_data['file_OTH'].apply(lambda x: x + '.WAV.wav')
    new_data['#file_extract'] = old_data['file_OTH']
    new_data['onset'] = old_data['onset_OTH']
    new_data['offset'] = old_data['offset_OTH']
    new_data['#phone'] = old_data['Target phone']
    new_data['context'] = [old_data['phone1_OTH'][i] + '_' + old_data['phone3_OTH'][i] for i in range(len(old_data['phone3_OTH']))]

    new_data['language'] = old_data['dialect_OTH'].apply(lambda x: 'EN_' + x)
    new_data['speaker'] = old_data['talker_OTH']

    new_data['prev_phone'] = old_data['phone1_OTH']
    new_data['next_phone'] = old_data['phone3_OTH']
    new_data['dataset'] = ['pilot-july-2018' for _ in range(1, 1 + len(old_data['phoneitem_id_OTH']))]

    new_data['phoneitem_id'] = old_data['phoneitem_id_OTH']

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)


def restructure_stimuli_dataset_3_july_X(name, destination_path=None):
    old_data = pd.read_csv(name)
    old_data = pd.DataFrame(old_data)

    new_data = dict()

    new_data['X_item'] = [i for i in range(1 + 2 * len(old_data['file_X']), 1 + 3 * len(old_data['file_X']))]
    new_data['#file_source'] = old_data['file_X'].apply(lambda x: x + '.WAV.wav')
    new_data['#file_extract'] = old_data['file_X']
    new_data['onset'] = old_data['onset_X']
    new_data['offset'] = old_data['offset_X']
    new_data['#phone'] = old_data['Target phone']
    new_data['context'] = [old_data['phone1_X'][i] + '_' + old_data['phone3_X'][i] for i in range(len(old_data['phone3_X']))]

    new_data['language'] = old_data['dialect_X'].apply(lambda x: 'EN_' + x)
    new_data['speaker'] = old_data['talker_X']

    new_data['prev_phone'] = old_data['phone1_X']
    new_data['next_phone'] = old_data['phone3_X']
    new_data['dataset'] = ['pilot-july-2018' for _ in range(1, 1 + len(old_data['phoneitem_id_X']))]

    new_data['phoneitem_id'] = old_data['phoneitem_id_X']

    # Save the new csv
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)

def merge_meta_with_TGT(meta_name, tgt_name, destination_path=None):

    META_DATA = pd.read_csv(meta_name)
    TGT_DATA = pd.read_csv(tgt_name)

    MERGE_DATA = pd.merge(META_DATA, TGT_DATA, on=[])

    MERGED_DATA.to_csv(destination_path)



if __name__ == '__main__':
    NAME_JULY_STIMULI = PATH_TO_DATA + 'datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    DESTINATION_JULY_STIMULI = PATH_TO_DATA + 'data/pilot-july-2018/annotation_data/pilot-july-2018_stimuli_TGT.csv'
    restructure_stimuli_dataset_3_july_TGT(NAME_JULY_STIMULI, DESTINATION_JULY_STIMULI)

    DESTINATION_JULY_STIMULI = PATH_TO_DATA + 'data/pilot-july-2018/annotation_data/pilot-july-2018_stimuli_OTH.csv'
    restructure_stimuli_dataset_3_july_OTH(NAME_JULY_STIMULI, DESTINATION_JULY_STIMULI)

    DESTINATION_JULY_STIMULI = PATH_TO_DATA + 'data/pilot-july-2018/annotation_data/pilot-july-2018_stimuli_X.csv'
    restructure_stimuli_dataset_3_july_X(NAME_JULY_STIMULI, DESTINATION_JULY_STIMULI)

    print('Script DONE')
