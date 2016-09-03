#!/usr/bin/env python

import numpy as np
import scipy.io.wavfile as wavefile
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

    waveforms = []
    for ch in range(0, data[1].shape[1]):
        wav = data[1][:, ch]
        wav = wav.astype(float) / max(abs(wav))
        waveforms.append(wav)

    fs = data[0]

    return waveforms, fs

def audio_write(waveforms, fs):
    pass

# ffmpeg -i file.mp3 file.wav
test_dir = 'test_files/'
test_filename = 'Gang_Starr-Skillz'
test_fileext = '.wav'
test_paired_ext = '__instrumental'

filename1 = test_dir + test_filename + test_fileext
filename2 = test_dir + test_filename + test_paired_ext + test_fileext

wavs_OG, fs_OG = audio_read(filename1)
wavs_OPP, fs_OPP = audio_read(filename2)

t1 = np.arange(0, len(wavs_OG[0])).astype(float) / float(fs_OG)
plt.plot(t1, wavs_OG[0])

# TODO CONTINUE HERE
# resample wavs_OPP
# write audio_write()
# write out 1 minus other

plt.show()

