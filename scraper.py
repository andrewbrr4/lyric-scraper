import config
import requests
import lyricsgenius as lg
from lyricsgenius import Genius

token = config.client_token

genius = Genius(token)
genius.search_artist('David Bowie')
artist.save_lyrics()

