# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:36:35 2018

Special functions to bring in some data for my intro class

@author: jgarber
"""

def get_rhap():
    import pandas as pd #importing pandas and giving it the nickname pd
    bohem_series = pd.read_csv('bohemian_list.csv',header = None) #using pandas read csv function because its easy and I like it!
    bohemian_list = list(bohem_series[1].values) #turning the letters into a series
    return bohemian_list


