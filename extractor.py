import json
import csv

f = open('tracks.csv', 'w')
writer = csv.writer(f)

f = open('test_set.json')
data = json.load(f)

for playlist in data['playlists']:
    if playlist['tracks'] is not None:
        for track in playlist['tracks']:
            track_id = track['track_uri'].split(':')[-1]
            writer.writerow([track_id])

f.close()

