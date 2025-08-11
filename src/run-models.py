# Charlie Redmon
# 2025-08-10
# Run speech recognition models

#%%

import os
import sys 
from openai import OpenAI
sys.path.insert(0, '/home/cr/.config/api_keys/')

import import_keys as crkeys

# directories
adir = "../data/raw/audio"

# data
audio_files = os.listdir("../data/raw/audio")
hindi_files = [f for f in audio_files if f.startswith('hindi')]

# test
tf = os.path.join(adir, hindi_files[0])

tf_audio = open(tf, 'rb')

client = OpenAI(api_key=crkeys.openai)

ts = client.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe", 
    file=tf_audio,
    response_format='text',
    language='hin',
) 















