from refresh import Refresh
from pytube import Search
from commands import SpotifyCommands, YoutubeCommands


class Main:
	def __init__(self):
		pass
	

if __name__ == "__main__":
	artist = "4wyNyxs74Ux8UIDopNjIai"
	#playlist = "03czRaUvmbOfqE9M3IPO6Q"
	playlist = "2lOBRIBV44kr3KufaxWZm6"
	
	sc = SpotifyCommands()
	playlist_tracks = sc.get_playlist_tracks(playlist)
	
	yc = YoutubeCommands()
	links = yc.get_links(playlist_tracks)
	
	path = "../tracks"
	
	yc.download_links(path, links)
	
