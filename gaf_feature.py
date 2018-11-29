# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:56:58 2018

@author: Veer
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GASF, GADF, RecurrencePlots, MTF

sig = pd.read_csv('sample_1.csv').iloc[0:10000, 4:7]

n_samples, n_features = 100, 1

rng = np.random.RandomState(41)

X = rng.randn(n_samples, n_features)

# Recurrence plot transformation
rp = RecurrencePlots(dimension=1,
                     epsilon='percentage_points',
                     percentage=30)

X_rp = rp.fit_transform(X)

plt.figure(figsize=(8, 8))
plt.imshow(X_rp[0], cmap='binary', origin='lower')
plt.show()



# MTF transformation
image_size = 1
mtf = MTF(image_size)
X_mtf = mtf.fit_transform(sig)

# Show the results for the first time series
plt.figure(figsize=(8, 8))
plt.imshow(X_mtf[0], cmap='rainbow', origin='lower')
plt.show()