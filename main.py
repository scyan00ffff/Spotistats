# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
#imports classes from other python files 
from login import Login 
from homepage import HomePage
from stats import Stats
from recon import Recon 
from profile_1 import Profile
from logout import Logout 

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

import webbrowser
from multiprocessing import Process

#sets the appaearance of the application either light or dark mode 
ctk.set_appearance_mode("Dark")
#ctk.set_default_color_theme("D:\Code\Spotipy\ColourTheme.json")
ctk.set_default_color_theme("green")

class windows(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        

        #creates a title for the page 
        self.title("Spotistats") 
        #self.wm_attributes("-fullscreen", True)
        #self.wm_state("zoomed")
        self.geometry("1400x950")
        #self.minsize(1400,950)
        #creates a frame and assigns it to the container variable 
        container = ctk.CTkFrame(self, height=400, width=600)
        #positions the frame inside of the root page 
        container.pack(side="top",fill="both",expand=True)
        #configures the location of the container using the grid method 
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #creates an empty array for the diffrerent pages to go into 
        self.frames = {}

        #defines each page of the application 
        #remember to add login back into the array after testing
        for F in ( HomePage, Stats, Recon, Profile, Logout, Login):
            frame = F(container, self)

            #windows class acts as the hidden root window for the frames therfore we call the self function
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #calls the method to switch the frames 
        self.show_frame(Login)

    #procedure to switch between pages in the application by bringing the selected page to the top using tkraise
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    #function runs every time the application is opened, sends an API request to the spotify database and returns the recently played songs into a text file
    def UpdateRecentlyplayed():
        scope = "user-read-recently-played"
        #intialises and sends the API request to the spotify database
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        #stores the results from the API request into an array
        results = sp.current_user_recently_played()
        #parses and stores the data from the array into a text file that can then be accessed later 
        recently_played = open("recently_played.txt", mode="w", encoding='utf-8')
        for idx, item in enumerate(results["items"]):
            track = item["track"]
            data = (idx, track["artists"][0]["name"], " - ", track["name"])
            recently_played.write(str(data) + "\n")
        recently_played.close()

    UpdateRecentlyplayed()

    def UpdateProfileinfo():
        scope = "user-read-private"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
    
        results = sp.me()
        
        split_results = str(results).split(",")
        
        with open("Profileinfo.txt", "w") as outfile:
            outfile.write("\n".join(split_results))

        
    
    UpdateProfileinfo()



    def CurrentlyPlaying():
        scope = "user-read-playback-state"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))

        results = sp.current_playback()
        

        split_results = str(results).split(",")
        
        with open("CurrentlyPlaying.txt", "w") as outfile:
            outfile.write("\n".join(split_results))
    
    CurrentlyPlaying()

    #functions for retrieving the data for the top 10 top played songs by the user in short, medium and long term. All data is stored in seperate text files 

    global limit
    limit = 100

    #this function sends a request to the spotify API for the top streamed songs of the user in the last 4 weeks
    #once results are returned they are enumerated and added to a text file for retrieval later 
    def TopTracksShort():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "short_term"
        results = sp.current_user_top_tracks(time_range=range, limit=limit)
        ToptracksFile = open("TopTracksShort.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item['name'])
            ToptracksFile.write(str(data) + "\n")
        ToptracksFile.close()
    
    TopTracksShort()

    def TopTracksMed():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "medium_term"
        results = sp.current_user_top_tracks(time_range=range, limit=limit)
        ToptracksFile = open("TopTracksMed.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item['name'])
            ToptracksFile.write(str(data) + "\n")
        ToptracksFile.close()
    
    TopTracksMed()

    def TopTracksLong():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "long_term"
        results = sp.current_user_top_tracks(time_range=range, limit=limit)
        ToptracksFile = open("TopTracksLong.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item['name'])
            ToptracksFile.write(str(data) + "\n")
        ToptracksFile.close()
    
    TopTracksLong()

    #functions for retrieving the top 10 most played artists and store them in seperate text files 

    def TopArtistsShort():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "short_term"
        results = sp.current_user_top_artists(time_range=range, limit=limit)
        TopArtistsFile = open("TopArtistsShort.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item["name"])
            TopArtistsFile.write(str(data) + "\n")
        TopArtistsFile.close()

    TopArtistsShort()

    def TopArtistsMed():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "medium_term"
        results = sp.current_user_top_artists(time_range=range, limit=limit)
        TopArtistsFile = open("TopArtistsMed.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item["name"])
            TopArtistsFile.write(str(data) + "\n")
        TopArtistsFile.close()

    TopArtistsMed()

    def TopArtistsLong():
        scope = "user-top-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        
        range = "long_term"
        results = sp.current_user_top_artists(time_range=range, limit=limit)
        TopArtistsFile = open("TopArtistsLong.txt", mode="w", encoding='utf-8')
        for i, item in enumerate(results['items']):
            data = (i, item["name"])
            TopArtistsFile.write(str(data) + "\n")
        TopArtistsFile.close()

    TopArtistsLong()

    #def TopGenres():

        #scope = "user-top-read"

        #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        #range = "long_term"
        #results = sp.current_user_top_genres()


app = windows()

app.mainloop()




#function that reads the data from the top tracks text file one line at a time, uses each value in a search request to the API to return the genre of
#each song and then writes this data along with the song name to a seperate text file 