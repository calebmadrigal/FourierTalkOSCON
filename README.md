FourierTalkOSCON
================

Presentation Materials for my [Sound Analysis with the Fourier Transform and Python](http://www.oscon.com/oscon2013/public/schedule/detail/28946) OSCON 2013 Talk.

---

### Link to this: http://tinyurl.com/fourierpython

---

# Presentation Index

* [01_Introduction.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/01_Introduction.ipynb)
* [02_NatureOfWaves.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/02_NatureOfWaves.ipynb)
* [03_FourierTransform.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/03_FourierTransform.ipynb)
* [04_WaveDeconvolution.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/04_WaveDeconvolution.ipynb)
* [05_RotationWithE.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/05_RotationWithE.ipynb)
* [06_FFTInPython.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/06_FFTInPython.ipynb)
* [07_SeeingSound.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/07_SeeingSound.ipynb)
* [08_STFT.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/08_STFT.ipynb)
* [09_AudioFiltering.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/09_AudioFiltering.ipynb)
* [10_Conclusion.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/10_Conclusion.ipynb)

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

