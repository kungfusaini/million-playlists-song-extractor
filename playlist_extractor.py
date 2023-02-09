import csv
import json

import spotipy
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
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    print('Client Details Loaded!')


def writeData(data):
    data = list(filter((None).__ne__, data))
    print('Creating CSV')
    f = open('dataset.csv', 'w')
    writer = csv.writer(f)

    header = ['name', 'artist', 'danceability', 'energy', 'key', 'loudness', 'mode', 
              'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
              'duration_ms', 'time_signature', 'realease_year']
    writer.writerow(header)

    for i in range(0, len(data)):
        print("Writing Data for Track Number : " + str(i + 1))
        writer.writerow(data[i])

    f.close()
    print("Done!")


def get_song_data(track_id):
    global spotify
    meta = spotify.track(track_id)
    album = meta['album']
    artists = album['artists']
    features = spotify.audio_features(track_id)[0]

    try:
        return [meta['name'], artists[0]['name'], features['danceability'], features['energy'], 
        features['key'], features['loudness'], features['mode'], features['speechiness'], 
        features['acousticness'], features['instrumentalness'], features['liveness'], features['valence'], 
        features['tempo'], features['duration_ms'], features['time_signature'], 
        album['release_date'].split('-')[0]]
    except:
        return None


def playlistGetter(playlist_id):
    song_info = []
    for i in range(0, 10):
        data = spotify.playlist_items(playlist_id=playlist_id, offset=i*100)['items']
        for song in data:
            song_info.append(get_song_data(song['track']['id']))
        print('Retrieved first {} songs'.format(i*100))

    writeData(song_info)


def main():
    get_secrets()
    playlistGetter(playlist_id='37i9dQZF1DWWQRwui0ExPn')


if __name__ == "__main__":
    main()


