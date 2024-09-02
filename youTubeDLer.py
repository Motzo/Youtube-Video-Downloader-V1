import sys
from pytube import YouTube
import os
from pytube. innertube import _default_clients

#overrides innertube.py default clients
_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]

def download_youtube_video(url, output_path):
    try:
        #url string
        yt = YouTube(url)
        print(f"Title:{yt.title}")
        print(f"Views: {yt.views}")
        print(f"Downloading video to {output_path}..")

        #progressive is both video and audio, function filters these and videos that have mp4 extension
        #sorts the videos by resolution 
        ytr = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        #grabs the highest sorted resolution, downloads it to output path
        ytr.desc().first().download(output_path)

        print(f"Download completed..")
    except Exception as e:
        print(f"Error:{e}")


print(f"Start: {sys.argv[0], sys.argv[1]}")
#take url from command line, hard code file path for now
url = sys.argv[1]
output_path = "C:\\Users\\sachi\\Desktop\\Python Repos\\Youtube Downloader\\youtube videos"
download_youtube_video(url, output_path)