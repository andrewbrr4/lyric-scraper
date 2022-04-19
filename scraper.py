import config
import requests
import lyricsgenius as lg
from lyricsgenius import Genius

token = config.client_token

genius = Genius(token)
songs = genius.search_artist('David Bowie',max_songs = 4).songs

text = ''
for song in songs:
    text += (song.lyrics+'\n\n')

with open('output.txt', 'w') as file:  # Use file to refer to the file object
    file.write(text)