# Charlie Redmon
# 2025-08-10
# Download audio and text bulletins from sample set

#%%

import os
import requests 
import pandas as pd
from tqdm import tqdm 

# dirs
audio_dir = "../data/raw/audio/"
text_dir = "../data/raw/text/"

# data
d = pd.read_csv('../data/working/sample-bulletins.csv')

# loop through and download files
for i in tqdm(range(0, d.shape[0])):

    ilang = str(d.loc[i, 'Language'])
    icity = str(d.loc[i, 'RNU Name'])
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
    

    







# %%
