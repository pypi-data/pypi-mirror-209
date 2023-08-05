# Spotigrabber - Exporting your Spotify tracklists

This Python package allows you to export your Spotify playlists and recently played tracks as an Excel file. It uses the Spotipy library to interact with the Spotify Web API. Due limitations of the spotify API, at maximum the last 50 played songs can be exported. Also, only songs that were listended all to the end are in the record.

## Installation

### Setting up Spotify API credentials

To access the Spotify API, you need to have API credentials in the form of a `client_id`, `client_secret`, and a `redirect_uri`. Here's how you can get your credentials:

1. Go to the Spotify Developer Dashboard: https://developer.spotify.com/dashboard/
2. Log in with your Spotify account or create a new one if you don't have one yet.
3. Click on "Create an App" and fill in the required information.
4. After creating the app, you will see your `client_id` and `client_secret` in the app's Dashboard.
5. Set the `redirect_uri` for your app by clicking "Edit Settings" and adding a redirect URI, such as "http://localhost:9000".

Now that you have your credentials, you should add them to your systems environment variables. To do so, open a windows cmd and enter the commands: 

```cmd
setx SPOTIFY_CLIENT_ID "your-client-id"
setx SPOTIFY_CLIENT_SECRET "your-client-secret"
setx SPOTIFY_USERNAME "your-spotify-username"
```

The ID and secret are now stored on your computer locally and will be found by the python code.

### Installation of the python package
The package with all dependencies can be installed with the following command:
You can install them with the following command:

```cmd
pip install spotigrabber
```


## Package usage

The package contains several functions to interact with your Spotify playlists and recently played tracks. You can use it as a standalone script or import the functions in your own Python project.



### Main function

The `main` function is the entry point of the script. It takes two optional arguments:

- `playlists_file`: The filename for the Excel file that will contain all your playlists (default: 'playlists').
- `recently_file`: The filename for the Excel file that will contain your 50 most recently played songs (default: 'recently_played').

To run the script you have various options

1) In a shell, navigate to the installed package (in your pythons install directory under site-packages) and use the following command:

```cmd
python spotigrabber.py --playlistsfile my_playlists --recentlyfile my_recently_played
```

2) In a shell, start your python 
```cmd
python
 ```

then import the installed package

```python
import spotigrabber
```
and finally execute the main function

```python
spotigrabber.main(playlists_file='my_playlists',recently_file='my_recently_played')
```

3) From another python script. Create a new python script and add the two lines. 
```python 
import spotigrabber
spotigrabber.main()
```

In any case, the current date will be added in front of your filename, such that when you export on a later date the files are not overwritten.

