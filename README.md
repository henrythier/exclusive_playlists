# Exclusive Playlists
Spotify does not allow you to specify which users can contribute to a collaborative playlist. This script allows you to specify a range of users that are allowed to add songs to a range of playlists.

To run it you need a configuration file (config.py) detailing:
* the allowed users uris: allowed_users = [_uri-1_,  _uri-2... ..._uri-n_]
* the playlists that you want to make exclusive: playlists = [_uri-1_,  _uri-2... ..._uri-n_]
* a Spotify token that authorizes you to edit playlists: spotify_credentials = {"token": _token_}

## Notes
* Spotify only allows the owner of a playlist to edit them through the Web API.
* The script only deletes songs by unauthorized users - it does not recover songs deleted by unauthorized users.
