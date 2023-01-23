#!/usr/bin/python

from concurrent.futures import ThreadPoolExecutor
import os
import sys

def downloadVideo(url):
    print("starting " + url, end="")
    os.system("2>/dev/null 1>/dev/null youtube-dl --yes-playlist --cookies cookies.txt --merge-output-format mp4 " + url)
    print("done with "+ url, end="")

threads = 20
try:
    threads = int(sys.argv[1])
except:
    pass
inf = open("links", "r")
links = inf.readlines()
inf.close()
linksfiltered = []
for i in links:
    if "/watch" in str(i) or "playlist" in str(i):
        linksfiltered.append(str(i))
with ThreadPoolExecutor(max_workers = threads) as executor:
    executor.map(downloadVideo, linksfiltered)
