
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import pandas as pd

token = '   """ Put your spotify API token here """   '


spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

while True:
    print("1 - exit")
    print()
    searchQuery = input("Ok, what is the artist's name ? ")
    print()


    searchResults = spotifyObject.search(searchQuery,1,0,"artist")

    artist = searchResults['artists']['items'][0]
    print(artist['name'])
    print(str(artist['followers']['total']) + " followers")
    print(artist['genres'][0])
    print()
    artistID = artist['id']


    trackURIs = []
    z = 0

    albumResults = spotifyObject.artist_albums(artistID)
    albumResults = albumResults['items']

    datas = []
    for item in albumResults:
        if z == 99 :
            break
        print("                     ALBUM:  " + item['name'])
        albumID = item['id']


        trackResults = spotifyObject.album_tracks(albumID)
        trackResults = trackResults['items']

        for item in trackResults:
            if z == 99 :
                break
            print(str(z) + "   :   " + item['name'])
            trackURIs.append(item['uri'])
            z+=1
            trackResults = spotifyObject.audio_features(trackURIs)




    i = input("Ok, what is the song's index ? ")
    i = int(i)
    json_obj = json.dumps(trackResults[i], sort_keys=True, indent=4)
    with open('""" HERE: Put your directory  which you want to save the data.json file to """', 'w') as outfile:
        outfile.write("[")
        outfile.write(json_obj)
        outfile.write("]")



    while True:
        songSelection = input("(x to exit)")
        if songSelection == "x" :
            break
