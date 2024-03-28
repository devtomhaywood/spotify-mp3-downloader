from refresh import Refresh
from pytube import Search
from commands import SpotifyCommands, DownloadCommands
import os
import subprocess


class Main:
	def __init__(self):
		self.playlist = ""
		self.playlist_id = ""
		self.playlist_items = ""
		self.playlist_info = ""
		self.playlist_tracks = ""


	def input_playlist_menu(self):
		link = input("Playlist: ")
		self.playlist = link
		self.parse_playlist_link()
		self.playlist_details()

		check = self.check_details()
		if check == False:
			return self.input_playlist()
	

	def parse_playlist_link(self):
		# replace with some regex at some point because i dont like this.
		self.playlist_id = self.playlist[34:56]


	def playlist_details(self):
		sc = SpotifyCommands()
		self.playlist_info = sc.get_playlist_info(self.playlist_id)
		self.playlist_items = sc.get_playlist_items(self.playlist_id)
	

	def get_playlist_tracks(self):
		tracks = []
		
		for item in self.playlist_items["items"]	:
			track = item["track"]["artists"][0]["name"] + " - " + item["track"]["name"] 
			tracks.append(track)
		
		self.playlist_tracks = tracks


	def check_details(self):
		print("\nFound playlist:")
		print("{} by {} \n".format(self.playlist_info["name"], self.playlist_info["owner"]["display_name"]))
		check = input("Is this the correct playlist? [y/n]: ").lower()

		# validitiy check required (any value that isnt y/n)
		if check == "n":
			return False
		elif check == "y":
			return True
		
	

	
if __name__ == "__main__":
	
	m = Main()
	sc = SpotifyCommands()
	dc = DownloadCommands()


	m.input_playlist_menu()
	m.get_playlist_tracks()
	
	dc.get_track_links(m.playlist_tracks)

	track_dir = "../tracks"
	path = os.path.join(track_dir, m.playlist_info["name"])

	dc.download_links(path)
	dc.convert_to_mp3(path)


	# https://open.spotify.com/playlist/2lOBRIBV44kr3KufaxWZm6?si=33c9609595d7433c
	