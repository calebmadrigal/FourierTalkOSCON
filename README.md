FourierTalkOSCON
================

Presentation Materials for my [Sound Analysis with the Fourier Transform and Python OSCON 2013 Talk](http://www.oscon.com/oscon2013/public/schedule/detail/28946).

[View Presentation](https://github.com/calebmadrigal/FourierTalkOSCON/blob/master/PRESENTATION_INDEX.md)

<br />

To run locally, you must use this command to run ipython notebook: `ipython notebook --pylab inline`

You will also need to install these python libraries (along with their C dependencies):

* numpy
* scipy
* matplotlib
* ipython
* scikits.audiolab

**Useful commands**

To record audio on your laptop, you can use [sox](http://sox.sourceforge.net/) (note that `rec` is a commnad installed with `sox`).  Here are 2 useful sox commands

* `rec -r 44100 -c 2 -b 16 A4.wav` - records at 44100 samples per sec, 2 channels, and 16 bits per sample
* `sox audio_2channels.wav audio_1channel.wav channels 1` - converts from 2 channels to 1 channel

