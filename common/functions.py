import numpy as np

def step(x):
    y = x > 0
    return y.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

def identity(x):
    return x

def softmax(x):
    c = np.max(x)
    np.exp(x - c) / np.sum(np.exp(x - c))