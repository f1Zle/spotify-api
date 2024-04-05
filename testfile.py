import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
client_id = '4fe94719ff284848b501b361e38512d5'
client_secret = 'a697afc8c97f441abdf1c108f6b9c229'
redirect_uri = 'http://localhost:3000'



scope = 'playlist-modify-private,user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope=scope))

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

def search_saved_tracks_by_genre(genres):
    
    with open('info.txt', 'w+', encoding='utf-8') as file:
        
        results = sp.current_user_saved_tracks()
        resultTrack = json.dumps(results, ensure_ascii=False, indent=3)
        file.write(resultTrack)
        for item in results['items']:
            track = item['track']
        
            artist_id = track['artists'][0]['id']
       
            artist = sp.artist(artist_id)
        
            track_genres = artist['genres']
        
            # track_info_str = json.dumps(track, ensure_ascii=False)
            # artist_info_str = json.dumps(artist, ensure_ascii=False)
            # track_genres_str = json.dumps(track_genres, ensure_ascii=False)

            # Write the information to the file
            # file.write(f'Track: {track_info_str}\n')
            # file.write(f'Artist ID: {artist_id}\n')
            # file.write(f'Artist: {artist_info_str}\n')
            # file.write(f'Genres: {track_genres_str}\n')
            # file.write("\n\n\n")
        
            if any(genre in track_genres for genre in genres):
                print(f'Found track {track["name"]} by {track["artists"][0]["name"]} in genres {genres}')
                track_ID.append(track['id'])
                
        track_uris = ['spotify:track:59aL2q2UPYJkgLTSv0WTlB', 'spotify:track:7lPN2DXiMsVn7XUKtOW1CS']
    
        sp.playlist_add_items(playlist["id"], track_ID)

 
search_saved_tracks_by_genre(['rock'])




