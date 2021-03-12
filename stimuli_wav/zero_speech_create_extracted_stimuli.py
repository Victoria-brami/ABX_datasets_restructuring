# import numpy as np
import pandas as pd
from scipy.io import wavfile


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
    freq, data = wavfile.read(wav_file)
    new_sliced_array = data[(int(begin * freq)):(int(end * freq))]
    wavfile.write(newfilename, freq, new_sliced_array)


if __name__ == '__main__':

    WAV_META_INFO = '/home/coml/Documents/Victoria/data/zero_speech/zero_speech_dataset_stimuli.csv'
    WAV_SOURCE_FOLDER = '/home/coml/Documents/Victoria/data/zero_speech/sound_data/wavs_source/'
    WAV_EXTRACTED_FOLDER = '/home/coml/Documents/Victoria/data/zero_speech/sound_data/wavs_extracted/'

    # store stimuli info
    stimuli_info = pd.read_csv(WAV_META_INFO)

    # split the wavs
    for i in range(39, len(stimuli_info['#file'])):

        if stimuli_info['#file'][i] != '1s_french/8682.wav':
            index = stimuli_info['index'][i]
            onset = stimuli_info['onset'][i]
            offset = stimuli_info['offset'][i]

            print(stimuli_info['#file'][i])

            wav_file = WAV_SOURCE_FOLDER + stimuli_info['#file'][i]

            extracted_wav_file = WAV_EXTRACTED_FOLDER + stimuli_info['#file'][i].split('.')[0] + '_sliced_' + str(index) + '.wav'

            slice_wav(wav_file, onset, offset, extracted_wav_file)

    print('Done')
