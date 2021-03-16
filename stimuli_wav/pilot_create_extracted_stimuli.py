# import numpy as np
from scipy.io import wavfile
import pandas as pd
import os.path as osp
import os

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
                        default='/home/coml/Documents/Victoria/data/zerospeech/sound_data/wavs_extracted/',
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



        wav_file = args.source_dir + stimuli_info['#file'][i]

        extracted_wav_file = args.output_dir + stimuli_info['#file'][i].split('.')[0] + '_sliced_' + str(index) + '.wav'

        if os.path.exists(wav_file):
            slice_wav(wav_file, onset, offset, extracted_wav_file)

        else:
            print(stimuli_info['#file'][i])
            problem_files.append(stimuli_info['#file'][i])

        count += 1

    print('RESULTS: problems encountered in {} files out of {} which are \n {}'.format(len(problem_files), count,  problem_files))




if __name__ == '__main__':

    main()

    WAV_META_INFO = '/home/coml/Documents/Victoria/data/pilote/pilote_data_july_2018_stimuli.csv'
    WAV_SOURCE_FOLDER = '/home/coml/Documents/Victoria/data/pilote/sound_data/wavs_source/timit/'
    WAV_EXTRACTED_FOLDER = '/home/coml/Documents/Victoria/data/pilote/sound_data/wavs_extracted'


    # store stimuli info
    stimuli_info = pd.read_csv(WAV_META_INFO)

    # split the wavs
    for i in range(len(stimuli_info['#file'])):

        index = stimuli_info['index'][i]
        onset = stimuli_info['onset'][i]
        offset = stimuli_info['offset'][i]
        wav_file = WAV_SOURCE_FOLDER + stimuli_info['#file'][i] + '.WAV.wav'


        stimuli_folder = stimuli_info['#file'][i].split('/')
        f_prefix = stimuli_folder.pop()
        stimuli_folder_part_1 = '/'.join(stimuli_folder[:1])
        stimuli_folder_part_2 = '/'.join(stimuli_folder[:2])
        stimuli_folder_part_3 = '/'.join(stimuli_folder[:3])
        print(i)

        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_1)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_1))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_2)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_2))
        if not os.path.exists(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_3)):
            os.mkdir(osp.join(WAV_EXTRACTED_FOLDER, stimuli_folder_part_3))

        extracted_wav_file = WAV_EXTRACTED_FOLDER  + '/' + stimuli_folder_part_3  + '/' + f_prefix + '_' + str(index) + '_sliced.wav'

        slice_wav(wav_file, onset, offset, extracted_wav_file)

	print('Script DONE')