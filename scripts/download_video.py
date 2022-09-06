from pytube import YouTube 
import os
def download_video(link):
	url = YouTube(link)
	print("downloading....")
	stream = url.streams.get_highest_resolution()
	target_path = "../data/video"
	stream.download(output_path= target_path)
	print("Downloaded! :)") 
	return os.path.join(target_path,url.title+".mp4")