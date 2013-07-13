#!/usr/bin/env python

import sys, math, pylab
import numpy as np
from scikits.audiolab import Format, Sndfile
from matplotlib.mlab import specgram

DEFAULT_DISPLAY_SAMPLE_RATE = 1000 #Hz
num_channels = 1

def usage():
    print "USAGE:", sys.argv[0], "<sound file path> [display sample rate] [outfile]"
    sys.exit(1)

if __name__ == "__main__":
    infile = ""
    outfile = "spectrogram.png"
    display_sample_rate = DEFAULT_DISPLAY_SAMPLE_RATE

    if len(sys.argv) > 3:
        infile = sys.argv[1]
        display_sample_rate = int(sys.argv[2])
        outfile = sys.argv[3]
    elif len(sys.argv) > 2:
        infile = sys.argv[1]
        display_sample_rate = int(sys.argv[2])
    elif len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        usage()

    f = Sndfile(infile, 'r')

    if display_sample_rate > f.samplerate:
        print "Using sample rate of file:", f.samplerate
        display_sample_rate = f.samplerate

    sound_time = f.nframes*1.0/f.samplerate
    sound_data = f.read_frames(f.nframes)
    samples_to_take = int(math.floor(sound_time * display_sample_rate))
    time_step_for_samples = f.samplerate*1.0/display_sample_rate

    wave = []
    for i in xrange(samples_to_take):
        frame_offset = i * time_step_for_samples
        if num_channels == 1:
            wave.append(sound_data[frame_offset])
        else: # must be 2
            wave.append(sound_data[frame_offset][0])

    fig = pylab.figure()
    fig.set_size_inches(12,7)
    pylab.specgram(wave, Fs=display_sample_rate)
    fig.savefig(outfile)
    print "Saved spectrogram to image file:", outfile
    #pylab.show()

