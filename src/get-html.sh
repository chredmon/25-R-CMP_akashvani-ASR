#!/bin/bash

# set up arguments
## news bulletin type
if [ $1 == "audio" ]; then
    baseurl="https://www.newsonair.gov.in/bulletins-category/regional-audio/"
elif [ $1 == "text" ]; then
    baseurl="https://www.newsonair.gov.in/bulletins-category/regional-text/"
else
    echo "ERROR: Neither audio nor text bulletin indicated."
    exit 1
fi

# dirs
outdir="../data/raw/html/"

## start and stop pages
istart=$(($2))
iend=$(($3))

# iterate through web pages and save
for i in $(seq $istart $iend); do

    tstart=`date +%s`

    echo -n "Downloading page ${i}..."

    iurl="${baseurl}?page=${i}"
    outf=$(printf "${outdir}$1-%04d.html" "$i")

    response=$(curl -s -k -m 120 -o $outf -w "%{http_code}" $iurl)
    http_code=$(tail -n1 <<< "$response")

    until [ $http_code == "200" ]; do 
        echo -n "."
	sleep 1
        response=$(curl -s -k -m 120 -o $outf -w "%{http_code}" $iurl)
        http_code=$(tail -n1 <<< "$response")
    done

    tend=`date +%s`
    runtime=$(((tend-tstart)/60))
    stime=$(printf "%d" "$runtime")

    echo " ✓ DL complete in ${stime} minutes."

    sleep 1

done




