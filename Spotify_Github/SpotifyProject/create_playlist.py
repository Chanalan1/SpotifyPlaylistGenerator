import spotipy
from spotipy.oauth2 import SpotifyOAuth

def initialize_spotify():
    # Initialize Spotify with user authentication
    sp_oauth = SpotifyOAuth(
        client_id='',
        client_secret='',
        redirect_uri='https://localhost:8888/callback',
        scope=["playlist-modify-public", "playlist-modify-private"]
    )
    return spotipy.Spotify(auth_manager=sp_oauth)

def create_playlist(playlist_name):
    # Initialize Spotify client with user authentication
    sp = initialize_spotify()

    # Get the user's Spotify username
    user_info = sp.me()
    user_id = user_info['id']

    try:
        # Create a new playlist on the user's Spotify account
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True)

        print(f"Playlist '{playlist_name}' created successfully.")
        print("Playlist URI:", playlist['uri'])

        return playlist['uri']  # Return the playlist URI
    except Exception as e:
        print(f"Error creating playlist: {str(e)}")
        return None  # Return None to indicate failure

if __name__ == "__main__":
    playlist_name = input("Enter the name of your new playlist: ")
    playlist_uri = create_playlist(playlist_name)

    #final check to see if playlist ends up failing to create
    if playlist_uri:
        None
    else:
        print("Playlist creation failed.")

