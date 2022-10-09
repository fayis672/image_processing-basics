import numpy as np

def log_transform(img,c):
    log_img = c*(np.log(img+1))
    log_img = np.array(log_img,dtype=np.uint8)
    return log_img;