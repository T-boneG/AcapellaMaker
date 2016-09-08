#!/usr/bin/env python

import numpy as np
import scipy.io.wavfile as wavefile
from scipy import signal
# import wave
import matplotlib.pyplot as plt

# TODO
# read both files
# read metadata and waveforms
# return one minus other

# eventually...
# make this a module with a __main__???
# write unit tests
# convert to c++ (juce)?
# make a gui
# create header and docstring:
# http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting

def audio_read(filename):
    data = wavefile.read(filename)
    # TODO assert read worked

    fs = data[0]
    wav_data = data[1]

    if wav_data.ndim == 1:
        wav_data = np.expand_dims(wav_data, axis=1)

    num_channels = wav_data.shape[1]

    waveforms = []
    for ch in range(0, num_channels):
        wav = wav_data[:, ch]
        wav = wav.astype(float) / max(abs(wav))
        waveforms.append(wav)

    waveforms = np.array(waveforms).transpose()

    return waveforms, fs

def audio_write(waveforms, fs):
    pass

# ffmpeg -i file.mp3 file.wav
test_dir = 'test_files/'
test_filename = 'Gang_Starr-Skillz'
test_fileext = '.wav'
test_paired_ext = '__instrumental'
test_clip = '_CLIP'

filename1 = test_dir + test_filename + test_clip + test_fileext
filename2 = test_dir + test_filename + test_paired_ext + test_clip + test_fileext

wavs_OG, fs_OG = audio_read(filename1)
wavs_OPP, fs_OPP = audio_read(filename2)

# wavs_OG = wavs_OG[40 * fs_OG : 70 * fs_OG, :]
# wavs_OPP = wavs_OPP[40 * fs_OPP : 70 * fs_OPP, :]
# wavefile.write('test_files/Gang_Starr-Skillz_CLIP.wav', fs_OG, wavs_OG)
# wavefile.write('test_files/Gang_Starr-Skillz__instrumental_CLIP.wav', fs_OPP, wavs_OPP)

new_len = int(len(wavs_OPP) * fs_OG/fs_OPP)
wavs_OPP = signal.resample(wavs_OPP, new_len)   #TODO check if wavs_OPP is multichannel
fs_OPP = fs_OG

t1 = np.arange(0, len(wavs_OG[:,0])).astype(float) / float(fs_OG)
plt.subplot('211')
plt.plot(t1, wavs_OG[:,0])
plt.plot(t1, wavs_OPP[:,0])

plt.subplot('212')
Rxy = np.correlate(wavs_OPP[:,0], wavs_OPP[:,0], 'full')
# tau = np.arange(0, len(Rxy[:,0])).astype(float) / float(fs_OG)
plt.plot(Rxy)


plt.show()

fs_DES = fs_OG
wavs_DES = wavs_OG
wavs_DES[:,0] -= wavs_OPP[:,0]
wavs_DES[:,1] -= wavs_OPP[:,0]

wavefile.write('results/Gang_Starr-Skillz__acapella_CLIP.wav', fs_DES, wavs_DES)

