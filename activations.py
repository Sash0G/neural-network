import numpy as np

def relu(x):
    return max(0,x)

def sig(x):
 return 1/(1 + np.exp(-x))

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def binary_step(x):
   if x<=0: return 0
   return 1