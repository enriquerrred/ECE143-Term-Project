# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:26:22 2019

@author: Enriq
"""

companies = data.groupby('company')
sort_by_company = {}
for company in pd.unique(data['company']):
    sort_by_company[company] = companies.get_group(company)

iscurrent = ['Current' in data['job-title'][i] for i in range(1,data.shape[0]+1)]
isformer = ['Former' in data['job-title'][i] for i in range(1,data.shape[0]+1)]
current = data[iscurrent]
former = data[isformer]