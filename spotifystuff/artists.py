import spotipy
import requests
import json
import time
from spotipy.oauth2 import SpotifyOAuth
client_id = '14ecafe25d67441690c29c28c507ebdd'
client_secret = '1432bcdbf5ad47f99c23d6bd6582c3c4'
redirect_uri = 'http://localhost:8888/callback'



scope = 'playlist-modify-private,user-library-read'

session = requests.Session()
session.headers["User-Agent"] = "Your User Agent"  
session.headers["Accept-Language"] = "en-US"  
session.headers["Accept-Encoding"] = "gzip, deflate, br"  
session.headers["Accept"] = "application/json"  
session.timeout = 10  


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               open_browser=False),
                      requests_session=session)  
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, 'nothing,nowhere', public=False)
print(f'Playlist "Hello World" created with ID: {playlist["id"]}')


def search_saved_tracks_by_artist(artists):
    with open('info.txt', 'w+', encoding='utf-8') as file:
        offset = 0
        limit = 50 
        track_ID = []

        while True:
            results = sp.current_user_saved_tracks(limit=limit, offset=offset)
            for item in results['items']:
                track = item['track']
                artist_names = [artist['name'] for artist in track['artists']]

                if any(artist in artist_names for artist in artists):
                    print(f'Found track {track["name"]} by {", ".join(artist_names)}')
                    track_ID.append(track['id'])
            time.sleep(1)
            
            if len(results['items']) < limit:
                break
            else:
                offset += limit

        batch_size = 100 
        for i in range(0, len(track_ID), batch_size):
            sp.playlist_add_items(playlist["id"], track_ID[i:i+batch_size])

search_saved_tracks_by_artist(['nothing,nowhere']).lower()




