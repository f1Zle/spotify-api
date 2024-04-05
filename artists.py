import spotipy
import requests
import json
from spotipy.oauth2 import SpotifyOAuth
client_id = '14ecafe25d67441690c29c28c507ebdd'
client_secret = '1432bcdbf5ad47f99c23d6bd6582c3c4'
redirect_uri = 'http://localhost:8888/callback'



scope = 'playlist-modify-private,user-library-read'

session = requests.Session()
session.headers["User-Agent"] = "Your User Agent"  # Specify your user agent
session.headers["Accept-Language"] = "en-US"  # Specify your preferred language
session.headers["Accept-Encoding"] = "gzip, deflate, br"  # Specify your preferred encoding
session.headers["Accept"] = "application/json"  # Specify your preferred response format
session.timeout = 10900000  # Set the read timeout to 10 seconds

# Initialize Spotify client with custom session
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               open_browser=False),  # Disable opening browser for authentication
                      requests_session=session)  # Pass the custom session
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, '$B', public=False)
# playlist_id = playlist_response['id']
print(f'Playlist "Hello World" created with ID: {playlist["id"]}')

# track_ID =[]

# def get_all_liked_songs():
#     results = sp.current_user_saved_tracks()
#     liked_songs = results['items']

#     while results['next']:
#         results = sp.next(results)
#         liked_songs.extend(results['items'])

#     return liked_songs

def search_saved_tracks_by_artist(artists):
    with open('info.txt', 'w+', encoding='utf-8') as file:
        offset = 0
        limit = 50  # Maximum limit per request
        track_ID = []

        while True:
            results = sp.current_user_saved_tracks(limit=limit, offset=offset)
            for item in results['items']:
                track = item['track']
                artist_names = [artist['name'] for artist in track['artists']]

                if any(artist in artist_names for artist in artists):
                    print(f'Found track {track["name"]} by {", ".join(artist_names)}')
                    track_ID.append(track['id'])

            # Check if there are more tracks to fetch
            if len(results['items']) < limit:
                break
            else:
                offset += limit

        batch_size = 100  # Set the batch size
        for i in range(0, len(track_ID), batch_size):
            sp.playlist_add_items(playlist["id"], track_ID[i:i+batch_size])

search_saved_tracks_by_artist(['$uicideboy$'])  # Replace 'artist1', 'artist2', 'artist3' with the desired artist names




