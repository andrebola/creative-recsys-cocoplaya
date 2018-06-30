#!/bin/sh -e
set +xv

audio_path="../audio/"
ls $audio_path |sort -R |while read first_dir; do
  ls "$audio_path/$first_dir" | while read entry ; do
    base=`basename $entry`
    str_sn=$(echo ${base} | cut -c3-4) 
    str_fn=$(echo ${base} | cut -c1-2)
    output_folder_ess="../essentia/${str_fn}/${str_sn}"
    if [ ! -f "${output_folder_ess}/${base}.json" ]; then
      mkdir -p ${output_folder_ess}
      echo "Reading $audio_path/$first_dir/$entry"
      ./streaming_extractor_music "$audio_path/$first_dir/$entry" "$output_folder_ess/${base}.json" profile.yaml || true
    fi
  done
done
