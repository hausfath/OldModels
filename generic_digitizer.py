#!/usr/local/bin/python3.7

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

os.chdir('/Users/hausfath/Desktop/Climate Science/Model GCM Comparison/Old Models Project/')

filename = 'AR4 A1B CO2'
start_year = 2000
end_year = 2032

def import_data(filename, start_year, end_year):
    colnames = ['year', 'temp']
    df = pd.read_csv(filename+'.txt', names=colnames, delim_whitespace=True, header=None)
    df['year'] = df['year'].round().astype(int)
    df.set_index('year', inplace=True)
    del df.index.name
    df = df[~df.index.duplicated()]
    
    df = df.reindex(range(start_year, (end_year + 1), 1), fill_value=np.nan)
    df.interpolate(inplace=True)
    return df

results = import_data(filename, start_year, end_year)

#nordhaus_temp.to_csv('nordhaus')
print(results)

results.to_csv(filename+'.csv')


