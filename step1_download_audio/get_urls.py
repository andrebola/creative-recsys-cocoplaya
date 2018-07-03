import tqdm
import os
import json
import spotipy
import spotipy.util as util
import time
from collections import defaultdict
from spotipy.client import SpotifyException


def get_all_uris(playlists_path):
    uris = defaultdict(int)
    filenames = os.listdir(playlists_path)
    for filename in sorted(filenames):
        if filename.startswith("mpd.slice.") and filename.endswith(".json"):
            fullpath = os.sep.join((playlists_path, filename))
            f = open(fullpath)
            js = f.read()
            f.close()
            mpd_slice = json.loads(js)
            for playlist in mpd_slice['playlists']:
                for track in playlist['tracks']:
                    uris[track['track_uri'][14:]]
    return list(uris.keys())


def get_urls(uris, client_id, client_secret):
    partial_output_file = "partial_output.json"
    username = ""
    scope = ","
    redirect_uri = "http://localhost/"
    token = util.prompt_for_user_token(username, scope,
            client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    market = "US"
    existing_uris = {}
    if os.path.isfile(partial_output_file):
        existing_uris = json.load(open(partial_output_file, 'r'))
    all_ids = [x for x in uris if x not in existing_uris]
    iter_size = 50
    num_iter = len(all_ids)//iter_size
    res_iter = len(all_ids)%iter_size

    if token:
        for _iter in tqdm.tqdm(range(num_iter)):
            results = None
            while results == None:
                try:
                    sp = spotipy.Spotify(auth=token)
                    ids = ",".join(all_ids[_iter*iter_size:(_iter+1)*iter_size])
                    results = sp._get('tracks?ids=%s&market=%s'%(ids, market), limit=iter_size)
                except SpotifyException:
                    # Refresh token
                    print ("Refreshing token...")
                    time.sleep(10)
                    token = util.prompt_for_user_token(username, scope,
                        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
            for res in results['tracks']:
                if res is not None and res['preview_url'] is not None:
                    url = res['preview_url']
                    uri = res['uri'][14:]
                    existing_uris[uri] = url
            if _iter % (num_iter//10) == 0:
                json.dump(existing_uris, open(partial_output_file, "w"))
        if res_iter > 0:
            sp = spotipy.Spotify(auth=token)
            ids = ",".join(all_ids[(-1)*res_iter:])
            results = sp._get('tracks?ids=%s&market=%s'%(ids, market), limit=iter_size)
            for res in results['tracks']:
                if res is not None and res['preview_url'] is not None:
                    url = res['preview_url']
                    uri = res['uri'][14:]
                    existing_uris[uri] = url
        return existing_uris
    else:
        print("Error, can't get token for", username)
        return None


if __name__ == '__main__':
    uris_file = "all_dicts_uri.json"
    if not os.path.isfile(uris_file):
        # Specify the location of the MPD:
        mpd_path = "mpd/data/"
        all_uris = get_all_uris(mpd_path)
        json.dump(all_uris, open(uris_file, 'w'))
    else:
        all_uris = json.load(open(uris_file, 'r'))

    # Specify the client secret and id of Spotify API:
    client_secret = ""
    client_id = ""

    all_dicts = get_urls(all_uris, client_id, client_secret)
    if all_dicts != None:
        output_file = "all_dicts.json"
        json.dump(all_dicts, open(output_file, "w"))

