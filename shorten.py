#!/usr/bin/env python

import argparse
import json
from time import sleep
from urllib import parse, request


def shorten_url(url: str) -> str:
    """Shorten a single URL using cleanuri.com"""
    data = parse.urlencode({"url": url}).encode()
    req = request.Request(
        "https://cleanuri.com/api/v1/shorten",
        headers={"User-Agent": "Mozilla/5.0"},
        data=data,
    )

    response = json.loads(request.urlopen(req).read().decode())

    return response["result_url"]


def shorten_urls(infile: str = "urls_long.txt", outfile: str = "urls_short.txt"):
    """Read long URLs from a file, shorten them with cleanuri.com, and write to a file"""
    with open(infile) as f:
        long_urls = [line.strip() for line in f]

    short_urls = []
    for url in long_urls:
        short_urls.append(shorten_url(url))
        sleep(0.5)

    with open(outfile, "w") as f:
        [f.write(url + "\n") for url in short_urls]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", type=str, required=False)
    args = parser.parse_args()

    if args.infile:
        shorten_urls(infile=args.infile)
    else:
        shorten_urls()
