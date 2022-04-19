import config
import requests
import lyricsgenius as lg
from lyricsgenius import Genius
import re

token = config.client_token

genius = Genius(token, timeout=20)
songs = genius.search_artist('David Bowie').songs

text = ''
for song in songs:
    lyrics = song.lyrics
    lyrics = lyrics.lower()
    lyrics = lyrics.replace('lyrics','')
    lyrics = lyrics.replace('embed','')
    lyrics = re.sub(r'\[.*\]','',lyrics)
    lyrics = re.sub(r'[0-9]','',lyrics)
    text += (lyrics +'\n\n')

with open('output.txt', 'w') as file:  # Use file to refer to the file object
    file.write(text)