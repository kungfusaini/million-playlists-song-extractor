# million-playlists-song-extractor
This project is for extracting information from the [spotify million playlist dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#dataset)

There is no database of spotify IDs to use in data projects. This project aims to fix this.

[Spotipy](https://spotipy.readthedocs.io/en/2.21.0/#license) was used to create this project. You must install it to run the code.

[Pandas](https://pandas.pydata.org/) is required.

Also, a spotify client ID and secret is required to use the project. You can do this via the spotify developer dashboard by creating a new app. Then create a file called 'secrets.json' with the following format:

~~~
{
    "client_id" : "your-client-id",
    "client_secret" : "your-client-secret"
}
~~~
To see more details about the given features of each song, check the [Spotify Documentation](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features)
