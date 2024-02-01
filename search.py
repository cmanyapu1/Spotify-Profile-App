import httpx
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

config = dotenv_values(".env") 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config['SPOTIFY_CLIENT_ID'],client_secret=config['SPOTIFY_CLIENT_SECRET'],redirect_uri="http://localhost:5173",scope="user-library-read"))




class Profile():

    def __init__(self):

        self.user = sp.current_user()
    
    def convert(self):

        print(self)
        # country = self.user["country"]
        display_name = self.user["display_name"]
        # email = self.user["email"]
        image = self.user["images"][0]["url"]

        return {"display_name": display_name, "image": image}

class Search():

    def __init__(self, search):

        self.search = search

    def show(self):

        searchresult = sp.search(q=self.search, limit=3, type='artist', market='US')

        list = searchresult["artists"]["items"]
        results = []
        for item in list:
            name = item["name"]
            id = item["id"]

            results.append({"name": name, "id": id})
        
        return results
       ## What's the best way to store the ID data
    ##Get the name data / return name data

class Artist():

    def __init__(self, artist_id):

        self.artist_id = artist_id
        
    def artistbio(self):
    
        artist_bio_response = sp.artist(artist_id = self.artist_id)

        results_dict = { 
            "Total_Followers" : artist_bio_response['followers']['total'],
            "Genres" : artist_bio_response['genres'],
            "Images" : artist_bio_response['images'],
            "Artist_Name" : artist_bio_response['name'],
            "Artist_Popularity" : artist_bio_response['popularity']
        }

        return results_dict

    def artistTracksUS(self):

        artist_tracks_US = sp.artist_top_tracks(self.artist_id, country='US')

        list = artist_tracks_US["tracks"]
        results = []

        for track in list:
            # album = track['album']
            # # markets = track['available_markets']
            # name = track['name']
            # popularity = track['popularity']
            # release_date = track['release_date']
            
            trackresults = {
            "US_Track_Album" : track.get('album'),
            # "US_Available_Markets" : markets,
            "US_Track_Name" : track.get('name'),
            "US_Track_Popularity" : track.get('popularity'),
            "US_Track_Release_Date" : track.get('release_date')
            }


            results.append((trackresults))

        return results
    
    def artistTracksBr(self):

        artist_tracks_Br = sp. artist_top_tracks(self.artist_id, country='BR')

        list = artist_tracks_Br["tracks"]
        results = []

        for track in list:
            # album = track['album']
            # # markets = track['available_markets']
            # name = track['name']
            # popularity = track['popularity']
            # release_date = track['release_date']

            trackresults = {
            "BR_Track_Album" : track.get('album'),
            # "BR_Available_Markets" : markets,
            "BR_Track_Name" : track.get('name'),
            "BR_Track_Popularity" : track.get('popularity'),
            "BR_Track_Release_Date" : track.get('release_date')
            }


            results.append((trackresults))

        return results

    def artistTracksIN(self):

        artist_tracks_IN = sp. artist_top_tracks(self.artist_id, country='IN')
        
        list = artist_tracks_IN["tracks"]
        results = []

        for track in list:
            # album = track['album']
            # # markets = track['available_markets']
            # name = track['name']
            # popularity = track['popularity']
            # release_date = track['release_date']


            trackresults = {
            "IN_Track_Album" : track.get('album'),
            # "In_Track_Available_Markets" : markets,
            "IN_Track_Name" : track.get('name'),
            "IN_Track_Popularity" : track.get('popularity'),
            "IN_Track_Release_Date" : track.get('release_date')

            }


            results.append((trackresults))

        return results


    def Albums(self):

        artistalbums = sp.artist_albums(self.artist_id, album_type="album", country='US', limit=30, offset=0)

        list = artistalbums["items"]
        results = []
        for item in list:
            # name = item["name"]
            # images = item["images"]
            # release_date = item["release_date"]
            # # popularity = item["popularity"]
            # artists = item ["artists"]

            albumresults = {
            "Album_Name" : item.get('name'),
            "Album_Images" : item.get('images'),
            "Album_Release_Date" : item.get('release_date'),
            # "Album_Popularity" : popularity,
            "Album_Artists" : item.get('artists')
        }

            results.append((albumresults))

        return results

    def Lyrics(self):

        artist_response = sp.artist(artist_id = self.artist_id)

        Artist_Name_1 = artist_response['name'],

        # Replace 'YOUR_API_KEY' with your actual OpenAI API key
        Openai_api_key = 'OPEN_AI_APIKey'

        # Specify the API endpoint
        Openai_api_url = 'https://api.openai.com/v1/chat/completions'

        # Set up the headers with the API key
        headers = {
        'Authorization': f'Bearer {Openai_api_key}',
        'Content-Type': 'application/json',
        }
        
        # Define the data for your API request  
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': f'Give me a {Artist_Name_1} lyric (nothing else in the response and do not reply).'},  # Modify the user message
            ],
        }

        # Send a POST request to the OpenAI API
        lyric_response = requests.post(Openai_api_url, json=data, headers=headers)
        
        lyric_result = lyric_response.json()

        generated_lyric = lyric_result['choices'][0]['message']['content']
        return generated_lyric



       
    

