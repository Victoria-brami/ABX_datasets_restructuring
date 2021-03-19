import pandas as pd


def restructure_pilot_triplets(name, destination_path=None):
    old_data = pd.read_csv(name)
    new_data=dict()
    new_data['triplet_id'] = []
    new_data['TGT_first'] = []
    new_data['TGT_item'] = []
    new_data['OTH_item'] = []
    new_data['X_item'] = []
    new_data['language_TGT'] = []
    new_data['language_OTH'] = []
    new_data['language_X'] = []
    new_data['speaker_TGT'] = []
    new_data['speaker_OTH'] = []
    new_data['speaker_X'] = []
    NB_ROWS = old_data.count()[0]

    for i in range(NB_ROWS):
        if old_data['triplet_id'][i] not in new_data['triplet_id']:
            new_data['triplet_id'].append(old_data['triplet_id'][i])
            new_data['TGT_first'].append(old_data['TGT_first'][i])
            new_data['TGT_item'].append(old_data['TGT_item'][i])
            new_data['OTH_item'].append(old_data['OTH_item'][i])
            new_data['X_item'].append(old_data['X_item'][i])
            new_data['language_TGT'].append(old_data['language_TGT'][i])
            new_data['language_OTH'].append(old_data['language_OTH'][i])
            new_data['language_X'].append(old_data['language_X'][i])
            new_data['speaker_TGT'].append(old_data['speaker_TGT'][i])
            new_data['speaker_OTH'].append(old_data['speaker_OTH'][i])
            new_data['speaker_X'].append(old_data['speaker_X'][i])
    new_data = pd.DataFrame(new_data)
    new_data.to_csv(destination_path)



if __name__ == '__main__':

    PATH_TO_DATA = '/home/coml/Documents/Victoria/'

    JULY_TRIPLETS = PATH_TO_DATA + 'data/pilot-july-2018/annotation_data/pilot-july-2018_human_experimental_data.csv'
    AUG_TRIPLETS = PATH_TO_DATA + 'data/pilot-aug-2018/annotation_data/pilot-aug-2018_human_experimental_data.csv'

    JULY_NEW_TRIPLETS = PATH_TO_DATA + 'data/pilot-july-2018/annotation_data/pilot-july-2018_triplets.csv'
    AUG_NEW_TRIPLETS = PATH_TO_DATA + 'data/pilot-aug-2018/annotation_data/pilot-aug-2018_triplets.csv'

    restructure_pilot_triplets(JULY_TRIPLETS, JULY_NEW_TRIPLETS)
    restructure_pilot_triplets(AUG_TRIPLETS, AUG_NEW_TRIPLETS)