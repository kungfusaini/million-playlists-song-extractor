import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

path = 'spotify:track:'

with open('track_IDs.csv', 'r') as f:
    data = f.read().splitlines()

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id='client_id',client_secret='client_secret'))


result = spotify.track(path + data[0])
album = result['album']
artists = album['artists']
print(result['name'], artists[0]['name'], album['release_date'].split('-')[0])
