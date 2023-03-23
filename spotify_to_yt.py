import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic
import random
yt = YTMusic('headers_auth.json')
playlistURI="6VZNeXQEd76Oa6CWeRhq1X"


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=YOUR CLIENT iD,
                                                           client_secret=CLIENT SECRET KEY ));
# get list of tracks in a given playlist (note: max playlist length 100)


tracks = sp.playlist_tracks(playlistURI)["items"] #songs in the spotify playlist
playlistId = yt.create_playlist('new_playlist'+str(random.randint(1,100000)), '') #creating youtube playlist
for track in tracks:
    song_name=track["track"]["name"]
    search_results = yt.search(song_name) #search youtube music for the song
    if search_results:
        print("done")
        yt.add_playlist_items(playlistId, [search_results[0]['videoId']])

    










