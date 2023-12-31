By: Alan Chan

# SpotifyPlaylistGenerator
<br/>
<br/>
Project Description:
<br/>
<br/>
Using the Spotipy python library for the Spotify Web API, this app allows a user to create a playlist of up to 20 random songs.
<br/>
The playlist is created from a search query that takes the users genre input and year input, concatenates it into a "top {year} {genre} hits" search query, which then finds a playlist and inside that playlist, 20 songs are randomly chosen and put into 
either a new or existing playlist after clearing the playlist of any previous songs.
<br/>
<br/>
Features of the app:
<br/>
<br/>
- A script that creates a new playlist into your spotify account and returns the playlist URI
<br/>
- Ability to clear all songs from an existing playlist given the URI
<br/>
- Search up all songs in a playlist given URI
<br/>
- Generate twenty random songs into a playlist given genre and year input
<br/>
<br/>
Getting Started:
<br/>
<br/>
This app leverages the Spotipy library, so for your local environment, pip install spotipy, will be needed
<br/>
for my case, I found it easier to use a venv (virtual environment) for this project so it was easier to control packages
<br/>
Done by python3 -m venv name_of_project-env
<br/>
To start the script on windows, cd to -env layer, and Script/activate to enter venv, once inside environment you can pip install the dependencies
<br/>
<br/>
You will also need to authenticate your spotify account when running the spotify api, which can be done at developer.spotify.com/dashboard, creating a new project
<br/>
and storing the Client ID and Client Secret in the .txt file or into the python code. The redirect URI can be set to your localhost any port.
