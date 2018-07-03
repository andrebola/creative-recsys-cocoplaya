
# STEP 1

The first step is to download the audio samples for the songs from Spotify, this step could be ommited if you already count with the audio, but take in to account that the mp3 files must be placed in a folder following this structure, for example: for the song spotify:track:01EADvpwhTIvFgyDAuC108:

`/audio_folder/08/01EADvpwhTIvFgyDAuC108.mp3`

To download the audio samples from Spotify first you need to retrieve the urls of the samples, this is done by running the python 3 script `get_urls.py`. In order to run this script you need to install the same requirement specified in [requiremets file](../step3_recommendations/requirements.txt). This script collects all the songs ids from the MPD, so you need to specify the location of the dataset. 

Also you need to specify the client id and secret of the Spotify API, when you run the script you will be requested to enter a url in the browser and then copy the url which you get redirected and paste it in the console. This is done in order to get an authetication token.

After you retrieved all the urls you need to run the python script `download_audio.py`, which will download the audio. The folder where the audio files will be downloaded can be specified inside the script.
