#!/usr/bin/env python

import sys
import math
import pylab
import numpy as np
from scikits.audiolab import Format, Sndfile

DEFAULT_DISPLAY_SAMPLE_RATE = 1000 #Hz
num_channels = 1

def usage():
    print "USAGE:", sys.argv[0], "<sound file path> [display sample rate] [outfile]"
    sys.exit(1)

def get_component_frequencies(samples):
    num_samples = len(samples)
    # Due to Nyquist theorem, we can only get frequencies up to num_samples/2
    # E.g: if we got 1000 samples, we can get frequencies from 1 to 500Hz.
    num_frequencies = num_samples/2
    get_freq_amplitude = lambda z: math.sqrt(np.real(z)**2 + np.imag(z)**2) / num_frequencies
    F = np.fft.rfft(samples)
    frequencies = range(num_frequencies)
    freq_amplitudes = [get_freq_amplitude(z) for z in F][0:-1] # Remove last
    return (frequencies, freq_amplitudes)

if __name__ == "__main__":
    infile = ""
    outfile = "fft.png"
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
        else:
            wave.append(sound_data[frame_offset][0])

    (freq, amp) = get_component_frequencies(wave)

    # Only plot first 700 Hz
    #hz=3000
    #hz=16000
    #freq = freq[0:hz]
    #amp = amp[0:hz]

    fig = pylab.figure()
    fig.set_size_inches(12,7)
    pylab.plot(freq, amp, 'r')
    fig.savefig(outfile)
    print "Saved fft to image file:", outfile

