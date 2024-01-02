from flask import Flask, request, render_template, jsonify, session
from search import Search, Profile, Artist

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"


@app.route("/")
def homepage():

    profile = Profile()
    profile_contents = profile.convert()

    return render_template("index.html", **profile_contents)

@app.route("/search", methods=['GET', 'POST'])
def showresults():

    q = request.args.get["searchbar"]

    search = Search(q)
    search_results = search.show()

    return render_template("index.html", search_results=search_results)

@app.route("/results/<artist_id>", methods=['GET', 'POST'])
def display_results(artist_id):

    artist_details = Artist(artist_id)

    artistbio = artist_details.artistbio()
    artistTracksUS = artist_details.artistTracksUS()
    artistTracksBr = artist_details.artistTracksBr()
    artistTracksIN = artist_details.artistTracksIN()
    Albums = artist_details.Albums()
    Lyrics = artist_details.Lyrics()

    return render_template("artist.html", artistbio=artistbio, artistTracksUS=artistTracksUS, artistTracksBr=artistTracksBr, artistTracksIN=artistTracksIN, Albums=Albums, Lyrics=Lyrics)