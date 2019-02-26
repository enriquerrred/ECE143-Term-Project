# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:55:33 2019

@author: Enriq
"""

import pandas as pd

path = 'C:/Users/Enriq/OneDrive/Documents/ECE 143'
data = pd.read_csv(path+'/employee_reviews.csv', index_col=0)