# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v

# loading images one by one and extracting features

def extractor(amount=None):
    
    counter = 0
    if amount is None:
        amount = len(glob.glob("../data/Creative Assets_/*.png"))

    features = {"game_key":[], "shape":[], "feature_matrix":[]}

    for img in range(amount):
        imgs = glob.glob("../data/Creative Assets_/*.png")[img]
        image = imread(imgs)


        game_key = imgs.split("/")[-1].split(".")[0]
        shape = image.shape

        feature_matrix = np.zeros((image.shape[0],image.shape[1])) 
        feature_matrix.shape

        for i in range(0,image.shape[0]):
            for j in range(0,image.shape[1]):
                feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2] + int(image[i,j,3]))/4))

        features["game_key"].append(str(game_key))
        features["shape"].append(str(shape))
        features["feature_matrix"].append(str(feature_matrix))
        counter = counter + 1

        if(counter%int((amount/2) + 1) == 0):
            print("successfully extracted")

    df = pd.DataFrame(features)
    df.to_csv("../data/extracted_features.csv")
    print("Completed")
    return df


    