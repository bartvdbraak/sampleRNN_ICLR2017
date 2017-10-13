# Given an array of PCM samples, return a feature matrix
# The feature matrix doesn't need to be upsampled to the sample rate
# However long the matrix is, we assume it matches the length of the WAV
# So you can use any frame_rate (hop_size)
import numpy as np
def build_features(filename):
    features = np.array(range(0,1000))/1000
    return features
