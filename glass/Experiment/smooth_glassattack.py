# this file is based on https://github.com/locuslab/smoothing
# This is done by Jeremy Cohen, Elan Rosenfeld, and Zico Kolter 

'''
This file is used to test the randomized smoothing against glass attacks
Type 'python smooth_glassattack.py {}.pt -sigma 1 -outfile output1'
{}.pt is the name of gaussian model you need to train by gaussian_train.py
1 is sigma of gaussian noise (I use same sigma with the sigma training the gaussian model)
output1 is the file name of your output file 

[1 , 2  , 3  , 5  , 7  , 10 , 20 , 50 , 100 , 300 ] # this is default numbers we used in experiment, 
which is the iterations of attacks 
'''



import argparse
from core import Smooth
from time import time
import torch
import datetime
import torch
from origin_train import data_process
import numpy as np
import torchvision
from new_vgg_face import VGG_16
from torchvision import datasets, models, transforms
import os
import copy
import cv2
from glass_attack import glass_attack



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Predict on many examples')
    parser.add_argument("model", type=str, help="test_model")
    parser.add_argument("-sigma", type=float, help="noise hyperparameter")
    parser.add_argument("-outfile", type=str, help="output file")
    parser.add_argument("--batch", type=int, default=32, help="batch size")
    parser.add_argument("--skip", type=int, default=1, help="how many examples to skip")
    parser.add_argument("--max", type=int, default=-1, help="stop after this many examples")
    parser.add_argument("--N", type=int, default=1000, help="number of samples to use")
    parser.add_argument("--alpha", type=float, default=0.001, help="failure probability")
    args = parser.parse_args()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    f = open(args.outfile, 'w')
    print("idx\tlabel\tpredict\tcorrect\ttime", file=f, flush=True)
    batch_size = 1
    dataloaders,dataset_sizes =data_process(batch_size)
    glass1 = cv2.imread('/home/research/tongwu/glass/models/dataprepare/silhouette.png')
    glass = transforms.ToTensor()(glass1)
    model = VGG_16() 
    model.load_state_dict(torch.load('../donemodel/'+args.model))
    model.to(device)
    smoothed_classifier = Smooth(model, 10, args.sigma)

    # default iterations 
    for i in [1 , 2  , 3  , 5  , 7  , 10 , 20 , 50 , 100 , 300 ]:
        cor = 0
        tot = 0 
        for k in dataloaders['test']:
            (x, label) = k
            x = x[:,[2,1,0],:,:]
            x = x.to(device)
            labels = label.to(device)
            glass = glass.to(device)
            before_time = time()
            x1 = glass_attack(model, x, labels, glass, alpha=20, num_iter=i,momentum=0.4)
            prediction = smoothed_classifier.predict(x1, args.N, args.alpha, args.batch)
            #print("label is ", label, "prediction is ", prediction)
            after_time = time()
            cor += int(prediction == int(label))
            time_elapsed = str(datetime.timedelta(seconds=(after_time - before_time)))
            # log the prediction and whether it was correct
            print("{}\t{}\t{}\t{}\t{}".format(i, label, prediction, cor, time_elapsed), file=f, flush=True)
            
    f.close()


