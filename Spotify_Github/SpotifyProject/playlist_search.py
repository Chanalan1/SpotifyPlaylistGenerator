import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotify_songs(playlist_uri):
    # Read the Spotify API credentials from the config.txt file
    config = {}
    with open("config.txt", "r") as config_file:
        for line in config_file:
            # Split the line into key and value parts
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                key, value = parts
                config[key] = value.strip("'")
    
    # Check if required keys are present in the config dictionary
    required_keys = ['SPOTIPY_CLIENT_ID', 'SPOTIPY_CLIENT_SECRET']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"{key} is missing in the config.txt file")

    # Create a Spotify client using the credentials from the config file
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(
            client_id=config['SPOTIPY_CLIENT_ID'],
            client_secret=config['SPOTIPY_CLIENT_SECRET']
        )
    )

    playlist = spotify.playlist_tracks(playlist_uri)

    list_songs = []
    list_artists = []
    for track in playlist['items']:
        track_name = track['track']['name']
        list_songs.append(track_name)

        artists = track['track']['artists'][0]
        list_of_artist = artists['name']
        list_artists.append(list_of_artist)

    # zip is used to iterate two or more lists in parallel so that we can match artist and song together
    # done so that we can see what songs are inside that playlist
    my_songs = []
    for track_name, artist_name in zip(list_songs, list_artists):
        my_songs.append(f"{track_name} by {artist_name}")
    
    return my_songs

if __name__ == "__main__":
    # Prompt the user for the Spotify playlist URI
    playlist_uri = input("Enter the URI of your Spotify playlist: ")

    # Call the spotify_songs function with the provided URI
    for_youtube = spotify_songs(playlist_uri)
    for song in for_youtube:
        print(song)


