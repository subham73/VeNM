from pytube import YouTube 
import os
import re

def download_video(link):
	url = YouTube(link)
	print("downloading....")
	stream = url.streams.get_highest_resolution()
	target_path = "../data/video"
	stream.download(output_path= target_path)
	print("Downloaded! :)") 
	title = re.sub("[^A-Za-z0-9]","",url.title)
	return os.path.join(target_path,url.title+".mp4")

# if __name__ == "__main__":
# 	link = 'https://www.youtube.com/watch?v=SC7RoYf9JhM'
# 	download_video(link)