import json
import os
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# --------------------------- CONSTANTS ---------------------------#

LYRICAL_RAP = 'c' # * done
    # 768 major, 432 minor
LOFI = '0vvXsWCC9xrXsKd4FyS8kM' # * done
    # 320 major, 180 minor
POP = '6vI3xbpdPYYJmicjBieLcr' # * done
    # 65 major, 35 minor
MELODIC_RAP = '3VXwYZevNjxgD897IaAcUO' # * done
    # 192 major, 208 minor
ROCK = '77RvyLiqmUimojxq3vg6mY' # * done
    # 450 major, 150 minor


# issues of data bias
# -----------------------------------------------------------------#

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def get_playlist_ids(playlist_id, length):

    splits = length // 100

    offset = 0
    uris = []
    for i in range(splits):
        res = sp.playlist_tracks(playlist_id,  fields='items,uri,name,id,total', market='GB', offset=offset)
        for i in res['items']:
            uri_string = i['track']['uri']
            uri = uri_string.split(':')[-1]
            uris.append(uri)
    offset += 100


    return uris

def get_audio_features(playlist_id, length):

    uris = get_playlist_ids(playlist_id, length)
    splits = len(uris) // 100
    print(splits)
    uris = chunks(uris, 100)

    audio_features = []
    major_count = 0
    minor_count = 0
    for i in range(splits):
        uri_sublist = next(uris)
        val = sp.audio_features(uri_sublist)
        audio_features += val # combining the two lists
    
    for i in audio_features:
        if i['mode'] == 1:
            major_count += 1
        elif i['mode'] == 0:
            minor_count += 1 

    print(f'\n\nMajor: {major_count}, Minor: {minor_count}')
    return [[i['speechiness'], i['danceability'], i['acousticness'], i['mode']] for i in audio_features]




