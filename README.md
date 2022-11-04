# million-playlists-song-extractor
This project is for extracting information from the [spotify million playlist dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#dataset)

There is no database of spotify IDs to use in data projects. This project aims to fix this.

[Spotipy](https://spotipy.readthedocs.io/en/2.21.0/#license) was used to create this project. You must install it to run the code.

Also, a spotify client ID and secret is required to use the project. You can do this via the spotify developer dashboard by creating a new app. Then run the following in your terminal:

~~~
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
~~~