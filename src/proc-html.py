#!/usr/bin/python3
# Charlie Redmon
# Process HTML from AIR regional bulletins (audio and text)

# %%

import os
import sys
import requests
from random import sample
import time
import dateutil.parser as dup 
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

html_dir = "../data/raw/html"
html_files = os.listdir(html_dir)

audio_files = [os.path.join(html_dir, f) for f in html_files if f.startswith("audio")]
text_files = [os.path.join(html_dir, f) for f in html_files if f.startswith("text")]

audio_files.sort()
text_files.sort()


def get_bulletin(file, bt='audio'):

    html_file = open(file, 'r')
    html = html_file.read()
    html_file.close()

    html_bs = BeautifulSoup(html, 'html.parser')

    bsec = html_bs.find('div', attrs={'class': 'bulletinTable'})
    tab = bsec.find('table')

    df = pd.read_html(StringIO(str(tab)), converters={'Play': str})[0]

    if bt == 'audio':
    
        lntags = tab.find_all('audio')
        links = [l['src'] for l in lntags]
        dlcol = "Play"

    elif bt == 'text':

        lntags = tab.find_all('a', attrs={'class': 'downloadBtn'})
        links = [l['href'] for l in lntags] 
        dlcol = "Download"

    else:
        raise Exception('Wrong bulletin type!')


    df['URL'] = ''
    j = 0

    for i in range(0, df.shape[0]): 
        
        if pd.isna(df.loc[i][dlcol]) or df.loc[i][dlcol] == "Download":

            df.loc[i, 'URL'] = links[j]
            j = j + 1

        else:

            df.loc[i, 'URL'] = 'NA'

    return(df)



audio_dfs = [get_bulletin(f, bt='audio') for f in audio_files]
audio_df_full = pd.concat(audio_dfs)

text_dfs = [get_bulletin(f, bt='text') for f in text_files]
text_df_full = pd.concat(text_dfs)

# reformat date/time columns
audio_df_full['Date'] = [dup.parse(d).strftime('%Y-%m-%d') for d in audio_df_full['Date']]
audio_df_full['Time'] = [str(t.replace(':', '')) for t in audio_df_full['Time']]

text_df_full['Date'] = [dup.parse(d).strftime('%Y-%m-%d') for d in text_df_full['Date']]
text_df_full['Time'] = [str(t.replace(':', '')) for t in text_df_full['Time']]

# output for later use
# audio_df_full.to_csv("../data/working/audio-bulletins.csv", index=False)
# text_df_full.to_csv("../data/working/text-bulletins.csv", index=False)

audio_df_full = pd.read_csv("../data/working/audio-bulletins.csv")
text_df_full = pd.read_csv("../data/working/text-bulletins.csv")


# merge text and audio data
mergecols = ['Station', 'Language', 'Date', 'Time']
audio_df_full = audio_df_full[mergecols + ['URL']]
text_df_full = text_df_full[mergecols + ['URL']]


df_full = audio_df_full.merge(text_df_full, left_on=mergecols, right_on=mergecols,
                              suffixes=('_audio', '_text'))
                               
df_full.Station = [str(s).lower() for s in df_full.Station]
df_full.Station = [s.replace(' ', '') for s in df_full.Station]
df_full.loc[df_full.Station == 'csnaagar', 'Station'] = 'csnagar'


df_full.Language = [str(s).lower() for s in df_full.Language]



lspairs = pd.read_csv('../data/working/language-station-pairs.csv')

df_list = [d for _,d in df_full.groupby('Date')] 

df_list_final = []
lspairs['Present'] = 0

for d in df_list:

    for i in range(0, lspairs.shape[0]):

        lang = lspairs.loc[i, 'Language']
        stat = lspairs.loc[i, 'Station']

        di = d[(d.Station == stat) & (d.Language == lang)]

        if di.shape[0] != 0:

            lspairs.loc[i, 'Present'] = 1
        
        else:

            lspairs.loc[i, 'Present'] = 0
    
    if all(lspairs.Present == 1):
    
        d.sort_values(['Station', 'Language', 'Time'], inplace=True)
        d.drop_duplicates(subset=['Station', 'Language'], inplace=True)
        df_list_final.append(d)

    
df_samp_list = [d for d in df_list_final if d.shape[0] == 54]

df_samp_list = sample(df_samp_list, 16)

df_samp_final = pd.concat(df_samp_list)

df_samp_final.to_csv('../data/working/sample-bulletins.csv', index=False)






# %%
