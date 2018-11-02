# -*- coding: utf-8 -*-
import numpy as np
import json
import os.path

ESSENTIA_PATH = '../essentia/{}/{}/{}.mp3.json'

def get_sample_dict(all_features=True):
    # This is used to train DictVectorizer
    return get_audio_features_dict("00006c661b0c80ef519ba561e321d100", all_features)


def get_audio_features_dict(songid, all_features=True):
    # This method returns all the audio features of a song or only the highlevel features
    audio_path = ESSENTIA_PATH.format(songid[:2], songid[2:4], songid)
    audio_features_dict = None
    if os.path.isfile(audio_path):
        audio_features_dict = {}
        audio_features = json.load(open(audio_path), strict=False)
        features = {"lowlevel": ["average_loudness", "dissonance", "dynamic_complexity", "zerocrossingrate"],
                    "rhythm": ["bpm", "bpm_histogram_first_peak_bpm", "bpm_histogram_second_peak_bpm", "danceability" ,"onset_rate"],
                    "tonal": ["chords_changes_rate", "chords_number_rate", "chords_strength"]}
        if all_features:
            # Add mean and variance for all features in 'features'
            for k in features.keys():
                for f in features[k]:
                    if isinstance(audio_features[k][f], dict):
                        audio_features_dict["%s_var" % f] = audio_features[k][f]["var"]
                        audio_features_dict["%s_mean" % f] = audio_features[k][f]["mean"]
                    else:
                        audio_features_dict[f] = audio_features[k][f]

        # Add Tagtraum highlevel "class" features
        # We always add this features, it doesn't depend on 'all_features' parameter

        for k in ["tagtraum"]:
            for f in audio_features["highlevel"][k]["all"]:
                audio_features_dict["class_f_%s_%s" % (k,f)] = audio_features["highlevel"][k]["all"][f]

        if all_features:
            # Add MFCC and HPCP
            """
            for i,f in enumerate(audio_features["lowlevel"]["mfcc"]["mean"]):
                audio_features_dict["mfcc_%d"%i] = f
            for i,f in enumerate(audio_features["tonal"]["hpcp"]["var"]):
                audio_features_dict["hpcp_var_%d"%i] = f
            for i,f in enumerate(audio_features["tonal"]["hpcp"]["mean"]):
                audio_features_dict["hpcp_mean_%d"%i] = f
            """

            # Add key and scale
            audio_features_dict["class_f_key"] = audio_features["tonal"]["key_key"]
            audio_features_dict["class_f_scale"] = audio_features["tonal"]["key_scale"]
    return audio_features_dict



