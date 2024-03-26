from refresh import Refresh
from pytube import Search
from commands import SpotifyCommands, YoutubeCommands
import os


class Main:
	def __init__(self):
		pass
		
		
def parse_playlist_link(playlist):
	# replace with some regex at some point because i dont like this.
	return playlist[34:56]

def check_playlist(playlist):
	sc = SpotifyCommands()
	playlist_info = sc.get_playlist_info(playlist)
	return playlist_info
	
	print("{} by {}".format(playlist_info["name"], playlist_info["owner"]["display_name"]))
	yn = input("Is this information correct? [y/N]: ").lower()
	
	if yn == "y":
		return True
	
	return False
	
	
if __name__ == "__main__":
	#artist = "4wyNyxs74Ux8UIDopNjIai"
	#playlist = "03czRaUvmbOfqE9M3IPO6Q"
	#playlist = "4TxH2ypGceAGIRJ5bdXPi2"
	
	
	
	link = input("Playlist: ")
	playlist = parse_playlist_link(link)
	
	sc = SpotifyCommands()
	
	playlist_info = check_playlist(playlist)
	
	print("{} by {}".format(playlist_info["name"], playlist_info["owner"]["display_name"]))
	yn = input("Is this information correct? [y/N]: ").lower()
	
	if yn == "y":
		playlist_tracks = sc.get_playlist_tracks(playlist)
		
		yc = YoutubeCommands()
		links = yc.get_links(playlist_tracks)
		
		
		track_dir = "../tracks"
		path = os.path.join(track_dir, playlist_info["name"])

		yc.download_links(path, links)
