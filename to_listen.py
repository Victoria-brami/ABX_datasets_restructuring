#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pandas as pd
import sys
# from wav_util import slice_wav
import pygame
import os
import keyboard
import numpy as np 
from scipy.io import wavfile

def slice_wav(file,begin,end,newfilename):
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
	freq, data=wavfile.read(file)
	new_sliced_array=data[(int(begin*freq)):(int(end*freq))]
	wavfile.write(newfilename,freq,new_sliced_array)



if __name__ == '__main__':
	index = 0
	folder_wav = '../ABX_bilingual/CogSci-2019-Unsupervised-speech-and-human-perception/Stimuli/wavs_extracted'
	folder_wav = '../zero_speech_dataset/sound_data/1s_english/1s'
	data1 = pd.read_table('../zero_speech_dataset/interspeech-2020-perceptimatic/DATA/english/all_aligned_clean_english.csv')

	# wav_file=os.path.join(folder_wav, str(data1[index.index('#file')])+".wav") #file which contains the wav file
	wav_file = os.path.join(folder_wav, str(data1['#file'][index]) + ".wav")
	freq, data=wavfile.read(wav_file)

	pygame.mixer.init(frequency=freq) # là il faut mettre la fréquence de tes fichiers

	# onset=float(data1[index.index('onset')]) #onset time
	# offset=float(data1[index.index('offset')]) #offset time
	onset=float(data1['onset'][index]) #onset time
	offset=float(data1['offset'][index]) #offset time

	sliced_wav=slice_wav(wav_file,onset,offset,'sliced.wav')
	# play_wav('sliced.wav')
	pygame.mixer.music.load('sliced.wav')
	pygame.mixer.music.play()
