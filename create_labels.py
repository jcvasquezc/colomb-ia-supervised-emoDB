# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:50:37 2017

@author: J.C. Vasquez-Correa
"""

import os
import numpy as np

def create_labelsEmoDB(PATH_AUDIO):
    hf=os.listdir(PATH_AUDIO)
    hf.sort()
    labelsd='WLEAFTN'
    labelshl=  [0, 1, 0, 0, 0, 1, 1] # 0 high arousal emotion, 1 low arousal emotions
    labelspn=  [0, 0, 0, 0, 1, 0, 1] # 0 negative valence emotion, 1 positive valence emotion
    labelshlpn=[0, 1, 2, 3, 4, 5, 6] # 0 negative and high arousal, 1 negative and low arousal, 2 positive and high arousal, 3 positive and low arousal
    LabelsHL=np.zeros(len(hf))
    LabelsNP=np.zeros(len(hf))
    LabelsHLPN=np.zeros(len(hf))
    for j in range(len(hf)):
    
        label=hf[j][5]
        poslabel=labelsd.find(label)
        LabelsHL[j]=labelshl[poslabel]
        LabelsNP[j]=labelspn[poslabel]
        LabelsHLPN[j]=labelshlpn[poslabel]
    return LabelsHL, LabelsNP, LabelsHLPN