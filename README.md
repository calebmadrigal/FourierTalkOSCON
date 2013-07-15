FourierTalkOSCON
================

Presentation Materials for my [Sound Analysis with the Fourier Transform and Python OSCON 2013 Talk](http://www.oscon.com/oscon2013/public/schedule/detail/28946).

---

# Presentation Index

* [00_Introduction.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/00_Introduction.ipynb)
* [01_WaveConvolution.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/01_WaveConvolution.ipynb)
* [02_WaveDeconvolution.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/02_WaveDeconvolution.ipynb)
* [03_RotationWithE.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/03_RotationWithE.ipynb)
* [04_FourierTransform.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/04_FourierTransform.ipynb)
* [05_FFTInPython.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/05_FFTInPython.ipynb)
* [06_HarmonicsAndTimbre.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/06_HarmonicsAndTimbre.ipynb)
* [07_HammingWindow.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/07_HammingWindow.ipynb)
* [08_STFT.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/08_STFT.ipynb)
* [09_AudioFilterLowPass.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/09_AudioFilterLowPass.ipynb)
* [10_AudioFilterHighPass.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/10_AudioFilterHighPass.ipynb)
* [11_Conclusion.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/11_Conclusion.ipynb)
* [FourierEquations.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/FourierEquations.ipynb)
* [MarkdownCells.ipynb](http://nbviewer.ipython.org/url/raw.github.com/calebmadrigal/FourierTalkOSCON/master/MarkdownCells.ipynb)

---

To run locally, you must use this command to run ipython notebook: `ipython notebook --pylab inline`

You will also need to install these python libraries (along with their C dependencies):

* numpy
* scipy
* matplotlib
* ipython
* scikits.audiolab

---

**Useful commands**

To record audio on your laptop, you can use [sox](http://sox.sourceforge.net/) (note that `rec` is a commnad installed with `sox`).  Here are 2 useful sox commands

* `rec -r 44100 -c 2 -b 16 A4.wav` - records at 44100 samples per sec, 2 channels, and 16 bits per sample
* `sox audio_2channels.wav audio_1channel.wav channels 1` - converts from 2 channels to 1 channel

