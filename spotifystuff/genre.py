import spotipy
import requests
import time
from spotipy.oauth2 import SpotifyOAuth
client_id = '4fe94719ff284848b501b361e38512d5'
client_secret = 'a697afc8c97f441abdf1c108f6b9c229'
redirect_uri = 'http://localhost:3000'



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
playlist = sp.user_playlist_create(user_id, ':(', public=False)

print(f'Playlist "Hello World" created with ID: {playlist["id"]}')



def search_saved_tracks_by_genre(genres):
    with open('info.txt', 'w+', encoding='utf-8') as file:
        offset = 0
        limit = 50  
        track_ID = []

        while True:
            results = sp.current_user_saved_tracks(limit=limit, offset=offset)
            for item in results['items']:
                track = item['track']
                artist_id = track['artists'][0]['id']
                artist = sp.artist(artist_id)
                track_genres = artist['genres']
                time.sleep(1)
                if any(genre in track_genres for genre in genres):
                    print(f'Found track {track["name"]} by {track["artists"][0]["name"]} in genres {genres}')
                    track_ID.append(track['id'])
            time.sleep(3)
           
            if len(results['items']) < limit:
                break
            else:
                offset += limit

        
        batch_size = 50 
        for i in range(0, len(track_ID), batch_size):
            sp.playlist_add_items(playlist["id"], track_ID[i:i+batch_size])
            time.sleep(1)

 
search_saved_tracks_by_genre(['emo rap'])




