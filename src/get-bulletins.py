# Charlie Redmon
# 2025-08-10
# Download audio and text bulletins from sample set

#%%

import os
import requests 
import pandas as pd
from tqdm import tqdm 
from pydub import AudioSegment

# dirs
audio_dir = "../data/raw/audio/"
text_dir = "../data/raw/text/"

# data
d = pd.read_csv('../data/working/sample-bulletins.csv')

# loop through and download files
for i in tqdm(range(0, d.shape[0])):

    ilang = str(d.loc[i, 'Language'])
    icity = str(d.loc[i, 'Station'])
    idate = str(d.loc[i, 'Date'])
    itime = str(d.loc[i, 'Time'])
    aurl = str(d.loc[i, 'URL_audio'])
    turl = str(d.loc[i, 'URL_text'])

    fn = "_".join([ilang, icity, idate, itime]) 
    audiofn = fn + ".mp3" 
    textfn = fn + ".pdf" 

    # download audio
    r = requests.get(aurl)
    with open(os.path.join(audio_dir, audiofn), 'wb') as f:
        f.write(r.content)
    
    # download text
    r = requests.get(turl)
    with open(os.path.join(text_dir, textfn), 'wb') as f:
        f.write(r.content)


d.Time = d.Time.apply(str)

d['audio_file'] = audio_dir + d.Language + "_" + d.Station + "_" + d.Date + "_" + d.Time + ".mp3"
d['pdf_file'] = text_dir + d.Language + "_" + d.Station + "_" + d.Date + "_" + d.Time + ".pdf"

# check times

d['audio_dur'] = 0

for i in tqdm(range(0, d.shape[0])):

    ifile = d.loc[i, 'audio_file']
    isound = AudioSegment.from_mp3(ifile)
    dur = isound.duration_seconds / 60
    d.loc[i, 'audio_dur'] = round(dur, 2)


d_summ1 = d.groupby(['Language', 'Station'], as_index=False)['audio_dur'].sum()
d_summ2 = d.groupby(['Language'], as_index=False)['audio_dur'].sum()

d_summ1['hours'] = d_summ1['audio_dur'] // 60
d_summ1['minutes'] = d_summ1['audio_dur'] % 60

d_summ2['hours'] = d_summ2['audio_dur'] // 60
d_summ2['minutes'] = d_summ2['audio_dur'] % 60




# d.to_csv('../data/working/sample-bulletins.csv', index=False)



# %%
