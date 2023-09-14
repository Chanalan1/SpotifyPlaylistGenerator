import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

def clear_playlist(playlist_uri):
    # Initialize the Spotify client with user authentication
    sp = initialize_spotify()

    try:
        # Extract the playlist ID from the URI
        playlist_id = playlist_uri.split(":")[-1]

        # Get the current tracks in the playlist
        current_tracks = sp.playlist_tracks(playlist_id)

        # Extract the URIs of the current tracks
        track_uris = [track['track']['uri'] for track in current_tracks['items']]

        # Remove all tracks from the playlist by setting it to an empty list
        sp.playlist_replace_items(playlist_id, [])
        
        print(f"All tracks removed from the playlist with URI: {playlist_uri}")
    except Exception as e:
        print(f"Error clearing the playlist: {str(e)}")

if __name__ == "__main__":
    # Input the URI of the Spotify playlist to clear
    playlist_uri = input("Enter the URI of the Spotify playlist to clear: ")

    # Clear all tracks from the playlist
    clear_playlist(playlist_uri)
