import config
import spotipy
import pandas as pd
import pprint

# read configuration file
token = config.spotify_credentials['token']
playlist_uris = config.playlists
allowed_users = config.allowed_users

# identify with token
sp = spotipy.Spotify(auth=token)

# loop through all playlists
for uri in playlist_uris:

    # put data into neat dataframe for further processing
    results = sp.playlist(uri)
    df = pd.DataFrame.from_dict(results['tracks']['items'])[['added_by', 'track']]
    df['track_name'] = df['track'].apply(lambda x: x['name'])
    df['track'] = df['track'].apply(lambda x: x['id'])
    df['added_by'] = df['added_by'].apply(lambda x: x['id'])

    # find all tracks added by other users
    df['legit'] = df['added_by'].apply(lambda x: x in allowed_users)

    # filter out the tracks that are not legit
    illegal_tracks = df[~df['legit']]

    # retrieve their position from the index
    illegal_tracks = illegal_tracks.reset_index().rename(columns={'index':'position'})

    # make list of uris and corresponding positions
    tracks = illegal_tracks['track'].unique()
    delete_tracks = []
    for t in tracks:
        positions = illegal_tracks['position'][illegal_tracks['track'] == t].values.tolist()
        delete_tracks.append({
            "uri": t,
            "positions": positions
        })

    # delete illegitimate track
    if len(delete_tracks):
        results = sp.user_playlist_remove_specific_occurrences_of_tracks(sp.me()['id'], uri.split(':')[2], delete_tracks)
        pprint.pprint(results)

    else:
        print('no illegal tracks found')
