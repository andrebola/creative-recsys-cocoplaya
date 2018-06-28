# STEP 3:

In order to generate the recommendations we use the precomputed audio features in step 2. 

First we train a Matrix Factorization model and then we generate the recommendations based on this model to the playlists in the challenge_set, then we combine this results with other model which computes the most probable songs based on the coocurrence in the playlists. This is all computed in the file model_creative.py.

To compute the Matrix Factorization we use the library LightFM, in requirements.txt you can find all the dependencies, we use the version 3.6.4 of Python.
Inside model_creative.py you can specify where the MPD dataset is located and were the challenge_set is located. Also in this file you can specify where the output CSV should be placed.

The file audio_features.py reads the json files with the extracted features of the songs, in this file you must specify where the json files are located.
