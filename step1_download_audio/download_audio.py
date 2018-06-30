import json
import os
import urllib.request


def download_item(audio_path, uri, url):
    fn = uri+'.mp3'
    subpath = uri[-2:]
    full_path = os.path.join(audio_path, subpath)
    full_fn = os.path.join(full_path, fn)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    if not os.path.exists(full_fn):
        for i in range(5):
            try:
                urllib.request.urlretrieve(url, full_fn)
            except:
                continue
            else:
                break
        else:
            print('url error. continue')


if __name__ == '__main__':
    audio_path = '../audio/'
    all_urls = json.load(open('./all_dicts.json'))
    for uri, url in all_urls.items():
        download_item(audio_path, uri, url)
