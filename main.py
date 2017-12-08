import tensorflow as tf
import numpy as np
import keras as ks
import matplotlib.pyplot as plt

import scipy.signal as signal
from scipy.io import wavfile

#do FFT because indecies will be the same length of the file ??

filepath = "./train/audio"
filename = "/bed/00f0204f_nohash_0.wav"

sample_rate, sample = wavfile.read(filepath + filename)

