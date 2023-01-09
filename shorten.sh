#!/usr/bin/env bash

INFILE="${1:-urls_long.txt}"

readarray -t arr < "$INFILE"

for long_url in "${arr[@]}"
do
   response=$(curl -s -XPOST --data-urlencode "url=$long_url" 'https://cleanuri.com/api/v1/shorten')
   printf '%b\n' "$response" | jq -r '.result_url' >> urls_short.txt
done
