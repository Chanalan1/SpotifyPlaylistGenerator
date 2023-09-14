import spotipy
from spotipy.oauth2 import SpotifyOAuth
from clear_all_songs import clear_playlist
from create_playlist import create_playlist
import random

def initialize_spotify():
    # Initialize Spotify with user authentication
    sp_oauth = SpotifyOAuth(
        client_id='',
        client_secret='',
        # browser authenticator from spotify  developer dashboard
        redirect_uri='https://localhost:8888/callback',
        scope=["playlist-modify-public", "playlist-modify-private"]
    )
    return spotipy.Spotify(auth_manager=sp_oauth)


def find_top_hits_playlist(sp, genre, year):
    # Search for a playlist named "top {year} {genre} hits"
    query = f"top {year} {genre} hits"
    playlists = sp.search(q=query, type='playlist', limit=1)
    
    if playlists and 'playlists' in playlists and 'items' in playlists['playlists']:
        return playlists['playlists']['items'][0]['uri']
    
    return None

def add_random_songs_to_playlist(sp, source_playlist_uri, target_playlist_uri, num_songs=20):
    # Get the tracks from the source playlist
    source_tracks = sp.playlist_tracks(source_playlist_uri)
    
    # Shuffle the tracks to get random songs
    random.shuffle(source_tracks['items'])
    
    # Extract the track URIs
    track_uris = [track['track']['uri'] for track in source_tracks['items'][:num_songs]]
    
    # Add the selected random songs to the target playlist
    sp.playlist_add_items(target_playlist_uri, track_uris)
    print(f"Added {len(track_uris)} random songs to the playlist.")

if __name__ == "__main__":
    genre = input("Enter the genre of music: ")
    
    while True:
        decision = input("Would you like to create a new playlist or use an existing playlist uri? Respond with 'yes' or 'no': ").lower()

        if decision == 'yes':
            ask_name = input("What would you like the name of the playlist to be? ")
            playlist_uri = create_playlist(ask_name)
            break
        elif decision == 'no':
            playlist_uri = input("Enter the URI of the Spotify playlist to add songs to: ")
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # playlist URI
    year = input("What year of songs do you want to listen to: ")

    # Initialize Spotify
    sp = initialize_spotify()

    clear_playlist(playlist_uri)
    
    # Find the "top {genre} hits" playlist
    top_hits_playlist_uri = find_top_hits_playlist(sp, genre, year)
    
    if top_hits_playlist_uri:
        # Add up to 20 random songs from the "top {year} {genre} hits" playlist to the specified playlist
        add_random_songs_to_playlist(sp, top_hits_playlist_uri, playlist_uri)
    else:
        print(f"No playlist found for 'top {year} {genre} hits'.")