import numpy as np

STATIC = np.array(
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0],
 [1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
 [0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
])

OSCILLATOR = np.array(
[[1,0,0,0,0,1,0,0],
 [1,0,0,0,1,0,0,1],
 [1,0,0,0,1,0,0,1],
 [0,0,0,0,0,0,1,0]])

GLIDER = np.array(
[[0,0,0,0],
 [0,0,1,0],
 [0,0,0,1],
 [0,1,1,1]])


GLIDER_GUN = np.array(
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
