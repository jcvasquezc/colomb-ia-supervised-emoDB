# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:23:10 2017

@author: J. C. Vasquez-Correa
"""

from scipy.io.wavfile import read
import numpy as np
from voiceAnalysis import mfcc
from scipy import stats
import os

def extractFeatAudio(file_audio, N_MFCC=12, sizeframe=0.02, size_step=0.01):
    fs, data=read(file_audio)
    
    data=data-np.mean(data,0)
    data=data/np.max(np.abs(data))
    size_frameS=sizeframe*fs
    size_stepS=size_step*fs
    nF=int((len(data)/size_stepS))-1
    MFCCcoef=np.zeros((nF,N_MFCC)) 
            
    for l in range(nF):
        data_frame=data[int(l*size_stepS):int(l*size_stepS+size_frameS)]
        data_frame=data_frame*np.hamming(len(data_frame))
        MFCCcoef[l,:]=mfcc(data_frame,fs,sizeframe,size_step,N_MFCC)
    DMFCCcoef=np.asarray([np.diff(MFCCcoef[:,nf], n=1) for nf in range(N_MFCC)])
    DDMFCCcoef=np.asarray([np.diff(MFCCcoef[:,nf], n=2) for nf in range(N_MFCC)])

    featmean=[]
    featstd=[]
    featsk=[]
    featku=[]
    
    featmean.append(MFCCcoef.mean(0))
    featstd.append(MFCCcoef.std(0,ddof=1))
    featsk.append(stats.skew(MFCCcoef))
    featku.append(stats.kurtosis(MFCCcoef,fisher=False))
    
    featmean.append(DMFCCcoef.mean(1))
    featstd.append(DMFCCcoef.std(1,ddof=1))
    featsk.append(stats.skew(DMFCCcoef.T))
    featku.append(stats.kurtosis(DMFCCcoef.T,fisher=False))
            
    featmean.append(DDMFCCcoef.mean(1))
    featstd.append(DDMFCCcoef.std(1,ddof=1))
    featsk.append(stats.skew(DDMFCCcoef.T))
    featku.append(stats.kurtosis(DDMFCCcoef.T,fisher=False))        

    featmean=np.hstack(featmean)
    featstd=np.hstack(featstd)
    featsk=np.hstack(featsk)
    featku=np.hstack(featku)
            
    Featvec=np.hstack((featmean, featstd, featsk, featku))
    
    return Featvec


def extractFeaturesFolder(path_audios, file_features):
    list_audio=os.listdir(path_audios)
    list_audio.sort()
    Features=[]
    for j in range(len(list_audio)):
        print('audio '+str(j+1)+' '+list_audio[j]+' '+str(len(list_audio)))
        file_audio=path_audios+list_audio[j]
        feat_vector=extractFeatAudio(file_audio)
        Features.append(feat_vector)
    Features=np.asarray(Features)
    np.savetxt(file_features, np.asarray(Features, dtype=np.float64), fmt='%s')   