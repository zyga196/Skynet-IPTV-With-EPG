#!/bin/bash
outfile='skynet-pl-private.m3u'
targetfile='skynet-pl-local.m3u'
file="secret-path" #the file where you keep your string name
secretprefix=$(cat "$file")        #the output of 'cat $file' is assigned to the $name variable
oldprefix='udp://@'
oldprefix=$(echo "$oldprefix" | sed 's/\//\\\//g')
secretprefix=$(echo "$secretprefix" | sed 's/\//\\\//g')

sed "s/$oldprefix/$secretprefix/g" $targetfile | tee $outfile
