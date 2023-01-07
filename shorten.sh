#!/usr/bin/env bash

readarray -t arr < urls_long.txt

for long_url in "${arr[@]}"
do
   response=$(curl -s -XPOST --data-urlencode "url=$long_url" 'https://cleanuri.com/api/v1/shorten')
   printf '%b\n' "$response" | jq -r '.result_url' >> urls_short.txt
done
