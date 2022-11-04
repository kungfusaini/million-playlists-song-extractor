import spotipy
import json
import csv
from spotipy.oauth2 import SpotifyClientCredentials

global client_id
global client_secret
global spotify

def get_secrets():
    global client_id
    global client_secret
    global spotify
    try:
        s = json.load(open('secrets.json'))
    except:
        print('secrets.json not found')
        exit()
    client_id = s['client_id']
    client_secret = s['client_secret']
    spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id='client_id',client_secret='client_secret'))
    print('Client Details Loaded!')



def get_all_track_data():
    print("Getting Track Data...")
    stub = 'spotify:track:'
    f = open('dataset.csv', 'w')
    writer = csv.writer(f)
    header = ['name', 'artist', 'danceability', 'energy', 'key', 'loudness', 'mode', 
    'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    'duration_ms', 'time_signature', 'realease_year']
    writer.writerow(header)

    with open('track_IDs.csv', 'r') as f:
        data = f.read().splitlines()
    
    for track_id in data:
        track_id = stub + track_id
        data = get_song_data(track_id)
        writer.writerow(data)
    f.close()
    print("Done!")
def get_song_data(track_id):
    global spotify
    meta = spotify.track(track_id)
    album = meta['album']
    artists = album['artists']
    features = spotify.audio_features(track_id)[0]
    return [meta['name'], artists[0]['name'], features['danceability'], features['energy'], 
    features['key'], features['loudness'], features['mode'], features['speechiness'], 
    features['acousticness'], features['instrumentalness'], features['liveness'], features['valence'], 
    features['tempo'], features['duration_ms'], features['time_signature'], 
    album['release_date'].split('-')[0]]

def main():
    get_secrets()
    get_all_track_data()

if __name__ == "__main__":
    main()