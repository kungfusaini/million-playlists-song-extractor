import json
import csv
import pandas as pd

f = open('track_IDs.csv', 'w')
writer = csv.writer(f)

f = open('test_set.json')
data = json.load(f)

for playlist in data['playlists']:
    if playlist['tracks'] is not None:
        for track in playlist['tracks']:
            track_id = track['track_uri'].split(':')[-1]
            writer.writerow([track_id])

f.close()

# Remove duplicates
df = pd.read_csv("track_IDs.csv")
df.drop_duplicates(inplace=True)
df.to_csv("track_IDs.csv", index=False)
