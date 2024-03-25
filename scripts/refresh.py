import json
import requests

class Refresh:

	def __init__(self, refresh_token, base64):
		self.refresh_token = refresh_token
		self.base64 = base64
		
		
	def refresh(self):
		url = "https://accounts.spotify.com/api/token"
		data = {
			"grant_type": "refresh_token",
			"refresh_token": self.refresh_token
		}
		header = {
			"Authorization": "Basic " + self.base64
		}
		response = requests.post(
			url=url, data=data, headers=header
		).json()

		return response["access_token"]

