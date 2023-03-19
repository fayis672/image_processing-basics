import numpy as np


def power_law_transform(img,gamma):
    return np.array(255*(img/255)**gamma,dtype=np.uint8)