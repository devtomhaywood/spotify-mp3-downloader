import requests
import pytube
import json
import base64
from refresh import Refresh
from pytube import Search, YouTube
import os
import subprocess

class SpotifyCommands:


	def __init__(self):
		self.access_token = ""
	
	
	def get_artist(self, artist):
		self.__refresh_access_token()
		url = "https://api.spotify.com/v1/artists/" + artist
		header = {
			"Authorization": "Bearer " + self.access_token
		}
		response = requests.get(
			url=url, headers=header
		).json()

		return response


	def get_playlist_info(self, playlist):
		self.__refresh_access_token()
		url = "https://api.spotify.com/v1/playlists/{}".format(playlist)
		header = {
			"Authorization": "Bearer " + self.access_token
		}
		response = requests.get(
			url=url, headers=header
		).json()
		
		return response


	def get_playlist_items(self, playlist):
		self.__refresh_access_token()
		url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist)
		header = {
			"Authorization": "Bearer " + self.access_token
		}
		response = requests.get(
			url=url, headers=header
		).json()
		
		return response
	
	
	def get_playlist_tracks(self, playlist):
		result = self.get_playlist_items(playlist)	
		tracks = []
		
		for item in result["items"]:
			track = item["track"]["artists"][0]["name"] + " - " + item["track"]["name"] 
			tracks.append(track)
		
		return tracks
	
	
	def __refresh_access_token(self):
		with open("../tokens.json", "r") as f:
			data = json.loads(f.read())

		ref = Refresh(data["refresh_token"], data["base64"])
		self.access_token = ref.refresh()


class YoutubeCommands:


	def __init__(self):
		pass
	
	
	def get_links(self, tracks):
		track_count = len(tracks)
		
		links = []
	
		for track in tracks:
			result = Search(track).results[0].watch_url
			print("Found {}".format(track))
		
			links.append(result)
		
		link_count = len(links)
		
		print("Successfully found... {} links out of {} tracks.".format(link_count, track_count))		
			
		return links
	
	
	def download_links(self, path, tracks):
		print("Downloading links to... {}".format(path))
		
		for track in tracks:
		
			track = YouTube(track)
			video = track.streams.filter(only_audio=True).first()
			out_file = video.download(output_path=path)

			#base, ext = os.path.splitext(out_file) 
			
			#new_file = base + '.mp3'
		
			#os.rename(out_file, new_file) 
		
		'''
			i feel like i dont have to do something stupid like this but i cannot for the life
			of me understand why i cant download a file as an mp3 using pytube?
			am i stupid?
		'''
		
		for track in os.listdir(path):
			f = path + "/" + track
			subprocess.run(["ffmpeg", "-i", "{}".format(f), "{}".format(f[:-4] + ".mp3")])
			os.remove(f)
		
		print("Files succesfully downloaded!")
	
