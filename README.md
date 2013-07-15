FourierTalkOSCON
================

Presentation Materials for my [Sound Analysis with the Fourier Transform and Python](http://www.oscon.com/oscon2013/public/schedule/detail/28946) OSCON 2013 Talk.

#### Bitly Link to THIS: **http://bit.ly/15zoIIn**

---

# Presentation Index

* [01_Introduction.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/01_Introduction.ipynb)
* [02_WaveConvolution.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/02_WaveConvolution.ipynb)
* [03_WaveDeconvolution.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/03_WaveDeconvolution.ipynb)
* [04_RotationWithE.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/04_RotationWithE.ipynb)
* [05_FourierTransform.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/05_FourierTransform.ipynb)
* [06_FFTInPython.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/06_FFTInPython.ipynb)
* [07_HarmonicsAndTimbre.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/07_HarmonicsAndTimbre.ipynb)
* [08_HammingWindow.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/08_HammingWindow.ipynb)
* [09_STFT.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/09_STFT.ipynb)
* [10_AudioFilterLowPass.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/10_AudioFilterLowPass.ipynb)
* [11_AudioFilterHighPass.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/11_AudioFilterHighPass.ipynb)
* [12_Conclusion.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/12_Conclusion.ipynb)

---

To run locally, you must use this command to run ipython notebook: `ipython notebook --pylab inline`

You will also need to install these python libraries (along with their C dependencies):

* numpy
* scipy
* matplotlib
* ipython
* scikits.audiolab

---

To record audio on your laptop, you can use [sox](http://sox.sourceforge.net/) (note that `rec` is a commnad installed with `sox`).  Here are 2 useful sox commands

* `rec -r 44100 -c 2 -b 16 A4.wav`
    - records at 44100 samples per sec, 2 channels, and 16 bits per sample
* `sox audio_2channels.wav audio_1channel.wav channels 1`
    - converts from 2 channels to 1 channel

