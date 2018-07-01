

# STEP 2:

After downloading all the audio samples from spotify we need to compute the features for each song, which are extracted using [Essentia](http://essentia.upf.edu/documentation/), an open-source library for audio and music analysis licences under Affero GPL v3.

The [essentia music extractor](http://essentia.upf.edu/documentation/streaming_extractor_music.html) computes low-level and high-level features from the audio, in this case we only use the Tagtraum classifier which gives the probability for each of the following genres: Blues, Country, Electronic, Folk, Jazz, Latin, Metal, Pop, Rap, Reggae, RnB, Rock, World.

In order to compute the extractor we used the static build from essentia (streaming_extractor_music) which can be downloaded from essentia's web, also we need to download the trained model to compute tagtraum features, both can be downloaded from http://essentia.upf.edu/documentation/extractors/. We also include these in the repo, the corresponding file is essentia-extractor-tagtraum-v2.1_beta2-linux-x86_64.tar.gz.

After uncompressing the file we can run the script hd_test.sh which reads all the audio in the specified folder and creates the respective json files with the output of the extractor. Computing the features for each song takes aproximately 3 seconds, therefore we recommend executing multiple times this script in order to parallelize the task.

