#!/bin/bash
outfile='../../playlist-private/skynet-pl-private.m3u'
targetfile='../skynet-pl-local.m3u'
file="secret-path" #the file where you keep your string name
secretprefix=$(cat "$file")        #the output of 'cat $file' is assigned to the $name variable
oldprefix='udp://@'
oldprefix=$(echo "$oldprefix" | sed 's/\//\\\//g')
secretprefix=$(echo "$secretprefix" | sed 's/\//\\\//g')

sed "s/$oldprefix/$secretprefix/g" $targetfile | tee $outfile

# git magic
cd ../../playlist-private
git add skynet-pl-private.m3u
DATE=`date`
git commit -m "Playlist update for $DATE"
git push origin master
