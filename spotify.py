import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

global client_id
global client_secret

def get_secrets():
    try:
        s = json.load(open('secrets.json'))
    except:
        print('secrets.json not found')
        exit()
    client_id = s['client_id']
    client_secret = s['client_secret']
    print('Client Details Loaded!')


path = 'spotify:track:'

with open('track_IDs.csv', 'r') as f:
    data = f.read().splitlines()

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id='client_id',client_secret='client_secret'))


result = spotify.track(path + data[0])
album = result['album']
artists = album['artists']
print(result['name'], artists[0]['name'], album['release_date'].split('-')[0])

def main():
    get_secrets()

if __name__ == "__main__":
    main()