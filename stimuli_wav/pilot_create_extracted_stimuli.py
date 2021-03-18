# import numpy as np
from scipy.io import wavfile
import pandas as pd
import os.path as osp
import os
import argparse

def slice_wav(wav_file, begin, end, newfilename):

	"""
	This function slice an array into two values given as begin and end
	Args:
		WavArray: an array obtained by a wav file
		begin: beginning point for slicing (seconds)
		end:end point for slicing (seconds)
		newfilename: le nom di fichier du retour
	Returns:
		A new wav file which contains extracted part

	"""
	freq, data=wavfile.read(wav_file)
	new_sliced_array=data[(int(begin*freq)):(int(end*freq))]
	wavfile.write(newfilename,freq,new_sliced_array)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stimuli_info', type=str,
                        default='/home/coml/Documents/Victoria/data/zerospeech/annotation_data/zerospeech_stimuli.csv',
                        help='CSV file in which stimuli meta information is store')
    parser.add_argument('--source_dir', type=str,
                        default='/home/coml/Documents/Victoria/data/zerospeech/sound_data/wavs_source/',
                        help='Directory in which source wavs are stored')
    parser.add_argument('--output_dir', type=str,
                        default='/home/coml/Documents/Victoria/data/zerospeech/sound_data/wavs_extracted_bis/',
                        help='Directory in which extracted wavs are stored')
    args = parser.parse_args()
    # WAV_META_INFO = '/home/coml/Documents/Victoria/data/zerospeech/zerospeech_stimuli.csv'
    # WAV_SOURCE_FOLDER = '/home/coml/Documents/Victoria/data/zero_speech/sound_data/wavs_source/'
    # WAV_EXTRACTED_FOLDER = '/home/coml/Documents/Victoria/data/zero_speech/sound_data/wavs_extracted/'

    # store stimuli info
    stimuli_info = pd.read_csv(args.stimuli_info)

    problem_files = []
    count = 0

    # split the wavs
    for i in range(0, len(stimuli_info['#file'])):

        index = stimuli_info['index'][i]
        onset = stimuli_info['onset'][i]
        offset = stimuli_info['offset'][i]



        wav_file = args.source_dir + stimuli_info['#file_source'][i]

        extracted_wav_file = args.output_dir + stimuli_info['#file_source'][i].split('.')[0] + '_sliced_' + str(onset) + '.wav'

        if os.path.exists(wav_file):
            slice_wav(wav_file, onset, offset, extracted_wav_file)

        else:
            print(stimuli_info['#file_source'][i])
            problem_files.append(stimuli_info['#file_source'][i])

        count += 1

    print('RESULTS: problems encountered in {} files out of {} which are \n {}'.format(len(problem_files), count,  problem_files))




if __name__ == '__main__':

    # main()

    WAV_META_INFO = '/home/coml/Documents/Victoria/data/pilot-july-2018/annotation_data/pilot-july-2018_stimuli.csv'
    WAV_META_INFO = '/home/coml/Documents/Victoria/datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information.csv'
    WAV_SOURCE_FOLDER = '/home/coml/Documents/Victoria/data/pilot-july-2018/sound_data/wavs_source/'
    WAV_EXTRACTED_FOLDER = '/home/coml/Documents/Victoria/data/pilot-july-2018/sound_data/wavs_extracted'

    stimuli_info = pd.read_csv(WAV_META_INFO)
    NB_ROWS = stimuli_info.count()[0]

    TGT_indexes = [i for i in range(1, NB_ROWS + 1)]
    OTH_indexes = [i for i in range(NB_ROWS + 1, 2 * NB_ROWS + 1)]
    X_indexes = [i for i in range(2 * NB_ROWS + 1, 3 * NB_ROWS + 1)]

    TGT_files = []
    OTH_files = []
    X_files = []

    for i in range(NB_ROWS):
        # TGT element
        TGT_index = 1 + i
        TGT_onset = stimuli_info['onset_TGT'][i]
        TGT_offset = stimuli_info['offset_TGT'][i]
        TGT_wav_file = WAV_SOURCE_FOLDER + stimuli_info['file_TGT'][i] + '.WAV.wav'

        TGT_stimuli_folder = stimuli_info['file_TGT'][i].split('/')
        TGT_f_prefix = TGT_stimuli_folder.pop()
        TGT_stimuli_folder_part_1 = '/'.join(TGT_stimuli_folder[:1])
        TGT_stimuli_folder_part_2 = '/'.join(TGT_stimuli_folder[:2])
        TGT_stimuli_folder_part_3 = '/'.join(TGT_stimuli_folder[:3])

        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_1)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_1))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_2)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_2))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_3)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, TGT_stimuli_folder_part_3))

        extracted_wav_file = WAV_EXTRACTED_FOLDER  + '/' + TGT_stimuli_folder_part_3  + '/' + TGT_f_prefix + '_sliced_' + str(TGT_index) + '.wav'
        slice_wav(TGT_wav_file, TGT_onset, TGT_offset, extracted_wav_file)
        TGT_files.append('/'.join(extracted_wav_file.split('/')[-4:]))

        # OTH element
        OTH_index = 1 + i + NB_ROWS
        OTH_onset = stimuli_info['onset_OTH'][i]
        OTH_offset = stimuli_info['offset_OTH'][i]
        OTH_wav_file = WAV_SOURCE_FOLDER + stimuli_info['file_OTH'][i] + '.WAV.wav'

        OTH_stimuli_folder = stimuli_info['file_OTH'][i].split('/')
        OTH_f_prefix = TGT_stimuli_folder.pop()
        OTH_stimuli_folder_part_1 = '/'.join(OTH_stimuli_folder[:1])
        OTH_stimuli_folder_part_2 = '/'.join(OTH_stimuli_folder[:2])
        OTH_stimuli_folder_part_3 = '/'.join(OTH_stimuli_folder[:3])

        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_1)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_1))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_2)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_2))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_3)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, OTH_stimuli_folder_part_3))

        extracted_wav_file = WAV_EXTRACTED_FOLDER + '/' + OTH_stimuli_folder_part_3 + '/' + OTH_f_prefix + '_sliced_' + str(
            OTH_index) + '.wav'
        slice_wav(OTH_wav_file, OTH_onset, OTH_offset, extracted_wav_file)
        OTH_files.append('/'.join(extracted_wav_file.split('/')[-4:]))

        # X element
        X_index = 1 + i + 2 * NB_ROWS
        X_onset = stimuli_info['onset_X'][i]
        X_offset = stimuli_info['offset_X'][i]
        X_wav_file = WAV_SOURCE_FOLDER + stimuli_info['file_X'][i] + '.WAV.wav'

        X_stimuli_folder = stimuli_info['file_X'][i].split('/')
        X_f_prefix = TGT_stimuli_folder.pop()
        X_stimuli_folder_part_1 = '/'.join(X_stimuli_folder[:1])
        X_stimuli_folder_part_2 = '/'.join(X_stimuli_folder[:2])
        X_stimuli_folder_part_3 = '/'.join(X_stimuli_folder[:3])

        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_1)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_1))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_2)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_2))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_3)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, X_stimuli_folder_part_3))

        extracted_wav_file = WAV_EXTRACTED_FOLDER + '/' + X_stimuli_folder_part_3 + '/' + X_f_prefix + '_sliced_' + str(
            X_index) + '.wav'
        slice_wav(X_wav_file, X_onset, X_offset, extracted_wav_file)
        X_files.append('/'.join(extracted_wav_file.split('/')[-4:]))

    stimuli_info['TGT_item'] = TGT_indexes
    stimuli_info['TGT_filename'] = TGT_files
    stimuli_info['OTH_item'] = OTH_indexes
    stimuli_info['OTH_filename'] = OTH_files
    stimuli_info['X_item'] = X_indexes
    stimuli_info['X_filename'] = X_files

    stimuli_info.to_csv('/home/coml/Documents/Victoria/datasets_manipulation/first-geomphon-perception-ABX/experiments/pilot_july_2018/stimuli/item_meta_information_tuned.csv')

    # # store stimuli info
    # stimuli_info = pd.read_csv(WAV_META_INFO)
    #
    # # split the wavs
    # for i in range(len(stimuli_info['#file_source'])):
    #
    #     index = stimuli_info['index'][i]
    #     onset = stimuli_info['onset'][i]
    #     offset = stimuli_info['offset'][i]
    #     wav_file = WAV_SOURCE_FOLDER + stimuli_info['#file_source'][i]
    #
    #
    #     stimuli_folder = stimuli_info['#file_source'][i].split('/')
    #     f_prefix = stimuli_folder.pop().split('.')[0]
    #     stimuli_folder_part_1 = '/'.join(stimuli_folder[:1])
    #     stimuli_folder_part_2 = '/'.join(stimuli_folder[:2])
    #     stimuli_folder_part_3 = '/'.join(stimuli_folder[:3])
    #     print(i)
    #
    #     if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_1)):
    #         os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_1))
    #     if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_2)):
    #         os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_2))
    #     if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_3)):
    #         os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_3))
    #
    #     extracted_wav_file = WAV_EXTRACTED_FOLDER  + '/' + stimuli_folder_part_3  + '/' + f_prefix + '_sliced_' + str(index) + '.wav'
    #
    #     slice_wav(wav_file, onset, offset, extracted_wav_file)

	# print('Script DONE')