# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:00:54 2019

@author: Enriq

***NOTICE***

This script requires a dask Client named 'c'.

If you have not had a Clinet, please run following
commands in console: 

from dask.distributed import Client
c = Client()

If your kernel is currently running a Client with other names,
There the script may not work and raise error.

If you are already running Client named 'c' normally,
please delete line #24 

Description:
    

"""
import pandas as pd
from find_all_words2 import word_frequency


if __name__ == '__main__':      
    
    column = data['cons']
    lines = [_ for _ in column]     
    tasks = c.map(word_frequency, [_ for _ in lines])
    allDicts = c.gather(tasks)
    allDict = {}
    
    for dic in allDicts:
        for key in dic.keys():
            if key in allDict.keys():
                allDict[key] += 1
            else:
                allDict[key] = 1
                
    words = pd.Series(list(allDict.keys()), index = list(allDict.values()))
    words = words.sort_index()
    threshold = int(words.shape[0]/100)
    words = words.loc[threshold:]
    
                
    