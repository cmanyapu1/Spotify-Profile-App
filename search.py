import httpx
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1091360323a84859aa2403664ddb294d",client_secret="bda783d8cb7c47bf9e44ba1c850f2a7a",redirect_uri="http://localhost:5173",scope="user-library-read"))

class Profile():

    def __init__(self):

        self.user = sp.current_user()
    
    def convert(self):

        country = self.user.get("country")
        display_name = self.user.get("display_name")
        email = self.user.get("email")
        if self.user.get("images"):
            image = self.user["images"][0]["url"]
        else:
            image = None

        return {"country": country, "display_name": display_name, "email": email, "image": image}

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

            results.append((name, id))
        
        return results
       ## What's the best way to store the ID data
    ##Get the name data / return name data

class Artist():

    def __init__(self, artist_id):

        self.artist_id = artist_id
        
    def artistbio(self):
    
        artist_bio_response = sp.artist(id = self.artist_id)

        results_dict = { 
            "Total_Followers" : artist_bio_response['followers']['total'],
            "Genres" : artist_bio_response['genres'],
            "Images" : artist_bio_response['images'],
            "Artist_Name" : artist_bio_response['name'],
            "Artist_Popularity" : artist_bio_response['popularity']
        }

        return results_dict

    def artistTracksUS(self):

        artist_tracks_US = sp. artist_top_tracks(self.artist_id, country='US')

        list = artist_tracks_US["tracks"]
        results = []

        for track in list:
            album = artist_tracks_US['album']
            markets = artist_tracks_US['available_markets']
            name = artist_tracks_US['name']
            popularity = artist_tracks_US['popularity']

            trackresults = {
            "US_Track_Album" : album,
            "US_Available_Markets" : markets,
            "US_Track_Name" : name,
            "US_Track_Popularity" : popularity
            }


            results.append((trackresults))

        return results
    
    def artistTracksBr(self):

        artist_tracks_Br = sp. artist_top_tracks(self.artist_id, country='BR')

        list = artist_tracks_Br["tracks"]
        results = []

        for track in list:
            album = artist_tracks_Br['album']
            markets = artist_tracks_Br['available_markets']
            name = artist_tracks_Br['name']
            popularity = artist_tracks_Br['popularity']

            trackresults = {
            "BR_Track_Album" : album,
            "BR_Available_Markets" : markets,
            "BR_Track_Name" : name,
            "BR_Track_Popularity" : popularity
            }


            results.append((trackresults))

        return results

    def artistTracksIN(self):

        artist_tracks_IN = sp. artist_top_tracks(self.artist_id, country='IN')
        
        list = artist_tracks_IN["tracks"]
        results = []

        for track in list:
            album = artist_tracks_IN['album']
            markets = artist_tracks_IN['available_markets']
            name = artist_tracks_IN['name']
            popularity = artist_tracks_IN['popularity']

            trackresults = {
            "In_Track_Album" : album,
            "In_Track_Available_Markets" : markets,
            "In_Track_Name" : name,
            "In_Track_Popularity" : popularity
            }


            results.append((trackresults))

        return results


    def Albums(self):

        artistalbums = sp.artist_albums(self.artist_id, album_type="album", country='US', limit=30, offset=0)

        list = artistalbums["items"]
        results = []
        for item in list:
            name = item["name"]
            images = item["images"]
            release_date = item["release_date"]
            popularity = item["popularity"]
            artists = item ["artists"]

            albumresults = {
            "Album_Name" : name,
            "Album_Images" : images,
            "Album_Release_Date" : release_date,
            "Album_Popularity" : popularity,
            "Album_Artists" : artists
        }

            results.append((albumresults))

        return results

       
#Items: , images, name, release_date, popularity, artists