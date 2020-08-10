import pickle
import numpy as np

def sigmoid(X):
   return 1/(1+np.exp(-X))

def predict(usrinput):
    with open("model.h5","rb") as f:
        weights = pickle.load(f)
    print(sum(weights))
    z = sum(np.multiply(usrinput,weights))
    y = sigmoid(z)
    if y>= 0.5:
        return 1
    else:
        return 0



