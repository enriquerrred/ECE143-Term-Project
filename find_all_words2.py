# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:07:41 2019

@author: Enriq
"""

import re, string

def find_all_words(stri):
    '''
    find all words in a given string,
    return a list contains all those words.
    
    :param: stri
    :type : str
    
    '''
    strList = []
    spaceIndex = [-1]
    for i in range(len(stri)):
        if stri[i] == ' ':
            spaceIndex.append(i)
    spaceIndex.append(len(stri))
    for i in range(len(spaceIndex)-1):
        a = spaceIndex[i]
        b = spaceIndex[i+1]
        newWord = stri[a+1:b]
        if newWord:
            strList.append(newWord)
    return strList



def word_frequency(line):
    '''
    find the frequency of each word in a string,
    return words and their corresponding frequencies
    in a dictionary.
    
    :param: line
    :type : str
    
    '''
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    allList = []
    allDict = {}
    
    if isinstance(line, str):
        line = line.lower()
        line = regex.sub(' ', line)
        wordList = find_all_words(line)
        for word in wordList:
            if word in allList:
                allDict[word] += 1
            else:
                allList.append(wordList)
                allDict[word] = 1
                    
    return allDict
