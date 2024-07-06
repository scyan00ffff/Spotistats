# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import threading
from multiprocessing import Process
import time
import random
from itertools import islice 



#class for the reconmendations page 
class Recon(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Recommendations Page ")
        label.pack(padx=10, pady=10)


        from profile_1 import Profile
        from stats import Stats
        switch_window_button_right = ctk.CTkButton(self,text="Profile Page",height=100, width=170,  command=lambda: controller.show_frame(Profile))
        switch_window_button_left = ctk.CTkButton(self,text="Statistics Page",height=100, width=170,  command=lambda: controller.show_frame(Stats))
        switch_window_button_right.pack(side="bottom", anchor="e", fill="none")
        switch_window_button_left.pack(fill = "none", side="bottom", anchor="w")

        Titlefont = ctk.CTkFont("Gothham Circular", 18, "bold")
        TitlefontUnderline = ctk.CTkFont("Gothham Circular ", 18, "bold", underline=True)
        Bodyfont = ctk.CTkFont("Gotham Circular", 16, "bold")

        def StartThread():
            thread = threading.Thread(target=UserReconmmendations)
            thread.start()

        #creates the recommendations frame and all widgets whithin 
        ReconmendationsFrame = ctk.CTkFrame(self, height= 750, width= 700 )
        ReconmendationsFrame.place(relx= 0.5, rely= 0.4, anchor= 'center')
        ReconendationsTitle = ctk.CTkLabel(ReconmendationsFrame, text='Recommendations:', font=TitlefontUnderline )
        ReconendationsTitle.place(relx=0.5, rely=0.05, anchor='center')
        ReconmendationsLabel = ctk.CTkLabel(ReconmendationsFrame, text='', font=Bodyfont)
        ReconmendationsLabel.place(relx= 0.5, rely=0.54, anchor='center')

        #creates the generate results frame and adds all the widgets whithin the frame 
        GenerateResultsFrame = ctk.CTkFrame(self, height=130, width=300)
        GenerateResultsFrame.place(relx=0.85, rely=0.05, anchor="ne")
        GenerateResultsTitle = ctk.CTkLabel(GenerateResultsFrame, text="Historical Recommendations:", font=TitlefontUnderline)
        GenerateResultsTitle.place(relx=0.5, rely=0.1, anchor="center")
        GetReconmmendationsButton = ctk.CTkButton(GenerateResultsFrame, text="Generate", font= Titlefont, height=40, width =100, command= StartThread)
        GetReconmmendationsButton.place(relx= 0.5, rely= 0.4, anchor="center")
        ProgressBar = ctk.CTkProgressBar(GenerateResultsFrame, indeterminate_speed=2.5)
        ProgressBar.set(0)
        ProgressBar.place(relx= 0.5, rely= 0.65, anchor="center")
        CompletedLabel = ctk.CTkLabel(GenerateResultsFrame, text="", font= Bodyfont, text_color="#2CC985")
        CompletedLabel.place(relx= 0.5, rely=0.7, anchor="center")

        #creates the seed frame and adds all the widgets whithin this frame 
        SeedFrame = ctk.CTkFrame(self, height= 130, width=300 )
        SeedFrame.place(relx=0.85, rely= 0.2, anchor='ne')
        SeedFrameTitle = ctk.CTkLabel(SeedFrame, text= "Based on: ", font= TitlefontUnderline)
        SeedFrameTitle.place(relx=0.5, rely=0.1, anchor='center')
        Track = ctk.CTkLabel(SeedFrame, text='Track: ', font=Bodyfont)
        Track.place(relx = 0.1, rely=0.3, anchor='nw')

        #creates the add playlist frame and adds all the widgets whithin the frame
        AddPlaylistFrame = ctk.CTkFrame(self, height=130, width=300)
        AddPlaylistFrame.place(relx= 0.85, rely=0.35, anchor="ne")
        AddPlaylistTitle = ctk.CTkLabel(AddPlaylistFrame, text= "Add to Playlist:", font=TitlefontUnderline)
        AddPlaylistTitle.place(relx=0.5,rely=0.1, anchor='center')
        CompletedPlaylistLabel = ctk.CTkLabel(AddPlaylistFrame, text= "", font = Bodyfont, text_color="#2CC985")
        CompletedPlaylistLabel.place(relx= 0.5, rely= 0.7, anchor='center')

        #creates the search frame and adds all the widgets whithin the frame 
        SearchFrame = ctk.CTkFrame(self, height=130, width=300)
        SearchFrame.place(relx=0.15, rely=0.05, anchor='nw')
        SearchTitle = ctk.CTkLabel(SearchFrame, text= "Search for Recommendations:", font=TitlefontUnderline)
        SearchTitle.place(relx=0.5, rely=0.1, anchor="center")
        SearchBar = ctk.CTkEntry(SearchFrame, height= 30, width= 200, placeholder_text="Enter Song: " )
        SearchBar.place(relx= 0.5, rely= 0.35, anchor="center")
        
        #creates the searched seed frame and adds all the widgets whithin the frame 
        SearchedSeedFrame = ctk.CTkFrame(self, height= 130, width=300 )
        SearchedSeedFrame.place(relx=0.15, rely= 0.2, anchor='nw')
        SearchedSeedFrameTitle = ctk.CTkLabel(SearchedSeedFrame, text= "Based on: ", font= TitlefontUnderline)
        SearchedSeedFrameTitle.place(relx=0.5, rely=0.1, anchor='center')
        SearchedTrack = ctk.CTkLabel(SearchedSeedFrame, text='Track: ', font=Bodyfont)
        SearchedTrack.place(relx = 0.1, rely=0.3, anchor='nw')

        #creates the seached add playlist frame and adds all the widgets whithin the frame 
        SearchedAddPlaylistFrame = ctk.CTkFrame(self, height=130, width=300)
        SearchedAddPlaylistFrame.place(relx= 0.15, rely=0.35, anchor="nw")
        SearchedAddPlaylistTitle = ctk.CTkLabel(SearchedAddPlaylistFrame, text= "Add to Playlist:", font=TitlefontUnderline)
        SearchedAddPlaylistTitle.place(relx=0.5,rely=0.1, anchor='center')
        SearchedCompletedPlaylistLabel = ctk.CTkLabel(SearchedAddPlaylistFrame, text= "", font = Bodyfont, text_color="#2CC985")
        SearchedCompletedPlaylistLabel.place(relx= 0.5, rely= 0.7, anchor='center')


            
        def UserReconmmendations():

            CompletedLabel.configure(text="")
            ReconmendationsLabel.configure(text="")
            Track.configure(text='Track: ')
            ProgressBar.place(relx= 0.5, rely= 0.85, anchor="center")
            ProgressBar.set(0)




            def UpdateProgressBar():
                ProgressBar.step()
                
            #function that opens a text file containing the users recently played data, searches the API for each one in turn and returns the 
            #trackID of each song which is then stored in a seperate file 
            def TracksID():

                ClearFile = open("TrackId.txt", mode="w")
                ClearFile.close()

                with open("TopTracksLong.txt") as open_file:
                    #reads each line from the tracks text file 
                    lines = open_file.readlines()
                    count = 0
                    for line in lines:
                        count += 1
                        TrackName = line
                        TrackName = str(TrackName)
                        TrackName = TrackName.replace("("," ")
                        TrackName = TrackName.replace(")"," ")
                        TrackName = TrackName.replace("'"," ")
                        TrackName = TrackName[5:]
                        UpdateProgressBar() 
                        #print(TrackName)
                        
                        #sends search request to the API t return the track ID of each song from the text file 
                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))
                        results = sp.search(TrackName)
                        TrackId = results['tracks']['items'][0]['id']
                        TrackIdFile = open("TrackId.txt", mode="a", encoding='utf-8')
                        TrackIdFile.write(str(TrackId + "\n"))
            
            def ArtistsID():

            
                ClearFile = open("ArtistId.txt", mode="w")
                ClearFile.close()


                with open("TopArtistsLong.txt") as open_file:

                    lines = open_file.readlines()
                    count = 0
                    for line in lines:
                        count += 1
                        ArtistName = line
                        ArtistName = str(ArtistName)
                        ArtistName = ArtistName.replace("("," ")
                        ArtistName = ArtistName.replace(")"," ")
                        ArtistName = ArtistName.replace("'"," ")
                        ArtistName = ArtistName[5:]
                        UpdateProgressBar()
                        #print(ArtistName)

                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))
                        results = sp.search(ArtistName)
                        ArtistId = results['tracks']['items'][0]['id']
                        ArtistIdFile = open("ArtistId.txt", mode="a", encoding='utf-8')
                        ArtistIdFile.write(str(ArtistId + "\n"))
            
            def TopGenres():
                
                Clearfile = open("TopGenres.txt", mode="w")
                Clearfile.close()

                with open("TopArtistsLong.txt") as open_file:

                    lines = open_file.readlines()
                    count = 0
                    for i in lines[0:15]:
                        count += 1
                        ArtistName = i
                        ArtistName = str(ArtistName)
                        ArtistName = ArtistName.replace("("," ")
                        ArtistName = ArtistName.replace(")"," ")
                        ArtistName = ArtistName.replace("'"," ")
                        ArtistName = ArtistName[5:]
                        UpdateProgressBar()
                        

                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))

                        results = sp.search(ArtistName)
                        track = results['tracks']['items'][0]
                        artist= sp.artist(track["artists"][0]["external_urls"]["spotify"])
                        ArtistGenre = artist['genres']
                        TopGenresFile = open("TopGenres.txt", mode='a', encoding='utf-8')
                        TopGenresFile.write(str(ArtistGenre))
                        
            #overall function to return random recoomendations based on the users past listening data
            def Reconmendations():

                time.sleep(16)
                global ArtistSeed
                global TrackSeed
                #selects a random trackseed for the algorithm
                TrackIDFile = open('TrackId.txt' ,'r').read().splitlines()
                TrackSeed = random.choice(TrackIDFile)
                #selects a random Artistseed for the algorithm
                ArtistIDFile = open('ArtistId.txt', 'r').read().splitlines()
                ArtistSeed = random.choice(ArtistIDFile)   
                #selects a random Genreseed for the algorithm
                GenreFile = open('TopGenres.txt', 'r').read().splitlines()
                GenreSeed = random.choice(GenreFile)
                
                sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))

                #sends a request to the API utilising its built in methods for song recomendations with the randomly selected seed values 
                results = sp.recommendations(seed_tracks=[TrackSeed])
                ReconmendationsFile = open("ReconmendationsFile.txt", mode="w", encoding="utf-8")
                for i, item in enumerate(results['tracks']):
                    data = (i, item['name'])
                    ReconmendationsFile.write(str(data) + "\n")
                ReconmendationsFile.close()

            TracksThread = threading.Thread(target=TracksID)
            TracksThread.start()

            GenresThread = threading.Thread(target=TopGenres)
            GenresThread.start()

            ArtistsThread = threading.Thread(target=ArtistsID)
            ArtistsThread.start()
            
            ReconmendationThread = threading.Thread(target=Reconmendations)
            ReconmendationThread.start()
            ReconmendationThread.join()

            
            CompletedLabel.configure(text="Recommendations Ready!")
            ProgressBar.place_forget()

            limit = 15
            with open ("ReconmendationsFile.txt") as open_file:
                lines = open_file.readlines()
                for line in enumerate((islice(lines, limit))):
                    tracks= ( "%s: %s" % (line) )
                    x = str(tracks[4:])
                    x=x.replace("[", "")
                    x=x.replace("]", "")
                    x=x.replace("(", "")
                    x=x.replace(")", "")
                    x=x.replace("'", "")
                    x=x.replace("\\n", "")
                    x=x.replace("\\", "")
                    x=x.replace(",", " ")
                    ReconmendationsLabel.configure(text =ReconmendationsLabel.cget("text") + x + "\n") 

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))


            TrackData = sp.track(TrackSeed, market='US')
            global TrackName1
            TrackName1 = TrackData['name']

            Track.configure(text=Track.cget('text') + str(TrackName1))

        #subroutine triggered by the create button to genereate a playlist of the songs outputted to the recommendatios panel 

        def CreatePlaylist():

            #creates a playlist for the tracks to be inputted into 
            Clearfile = open("RecommendationIDs.txt", mode="w")
            Clearfile.close()
            
            scope = 'playlist-modify-private'
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
            results = sp.current_user()
            userID = results['id']

            RecommnedationPlaylist = sp.user_playlist_create(user=userID, name=f"Based on: {TrackName1}", public=False, description=f"Generated using Spotistats application based on the song: {TrackName1}")

            #converts the song names into the song ID's so they can be added to the playlist 
            with open("ReconmendationsFile.txt") as open_file:

                lines = open_file.readlines()
                count = 0
                for line in lines:
                        count += 1
                        TrackName = line
                        TrackName = str(TrackName)
                        TrackName = TrackName.replace("("," ")
                        TrackName = TrackName.replace(")"," ")
                        TrackName = TrackName.replace("'"," ")
                        TrackName = TrackName[5:]

                
                        
                        
                        #searches for the song ID and adds it to a text file with 20 others 
                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
                        results = sp.search(TrackName)
                        TrackId = results['tracks']['items'][0]['id']
                        RecommendationIDFile = open("RecommendationIDs.txt", mode="a", encoding='utf-8')
                        RecommendationIDFile.write(str(TrackId) + "\n")

                        
            #opens the previous text file and converts it into a list to be inputted to the 'add_tracks' function 
            file = open('RecommendationIDs.txt', 'r')
            data = file.read()
            TrackIds = data.replace('\n', ' ').split()
            #adds the list of tracks to the playlist created earlier 
            PlaylistID = RecommnedationPlaylist['id']
            sp.user_playlist_add_tracks(user=userID, playlist_id=PlaylistID, tracks=TrackIds)

            CompletedPlaylistLabel.configure(text="Playlist Created!") 
            
            

        #creates the button to trigger the above function 
        AddPlaylistButton = ctk.CTkButton(AddPlaylistFrame, text="Create", font=Titlefont, height=40, width=100, command= CreatePlaylist)
        AddPlaylistButton.place(relx=0.5, rely=0.4, anchor='center')

        def SearchRecommendations():
            #configure and wipe all text files and variables ready for new values

            ReconmendationsLabel.configure(text="")

            SearchedTrack.configure(text='Track: ')

            ClearSearchedFile = open("SearchedTrackIdFile.txt", "w")
            ClearSearchedFile.close()

            ClearRecommendationsFile = open("ReconmendationsFile.txt", "w")
            ClearRecommendationsFile.close()

            SearchedName = SearchBar.get()
            SearchBar.configure(placeholder_text="Enter Song/Artist")

            #turn the users entered value into its spotify ID and append to a text file 

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))
            searchedIDresults = sp.search(SearchedName)
            TrackId = searchedIDresults['tracks']['items'][0]['id']
            SearchedTrackIdFile = open("SearchedTrackIdFile.txt", mode="a", encoding='utf-8')
            SearchedTrackIdFile.write(str(TrackId + "\n"))
            SearchedTrackIdFile.close()
    
            #make the TrackSeed variable into the item stored int the Spotify ID text file 

            SearchedTrackIDFile = open('SearchedTrackIdFile.txt' ,'r').read().splitlines()
            SearchedTrackSeed = SearchedTrackIDFile[0]
            print(SearchedTrackSeed)

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))

            #search for recommendations using spotifys recommendation algorithm and store these in a text file 

            searchedresults = sp.recommendations(seed_tracks=[SearchedTrackSeed])
            SearchedReconmendationsFile = open("SearchedRecommendationsFile.txt", mode="w", encoding="utf-8")
            for i, item in enumerate(searchedresults['tracks']):
                searcheddata = (i, item['name'])
                SearchedReconmendationsFile.write(str(searcheddata) + "\n")
            SearchedReconmendationsFile.close()

            #open the text file and parse the values to get rid of unnecesary characters, append these parsed lines to the recommendations frame on the GUI

            limit = 15
            with open ("SearchedRecommendationsFile.txt") as open_file:
                lines = open_file.readlines()
                for line in enumerate((islice(lines, limit))):
                    tracks= ( "%s: %s" % (line) )
                    x = str(tracks[4:])
                    x=x.replace("[", "")
                    x=x.replace("]", "")
                    x=x.replace("(", "")
                    x=x.replace(")", "")
                    x=x.replace("'", "")
                    x=x.replace("\\n", "")
                    x=x.replace("\\", "")
                    x=x.replace(",", " ")
                    ReconmendationsLabel.configure(text =ReconmendationsLabel.cget("text") + x + "\n") 

            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url))

            # retrieve the name of the track the user searched for

            SearchedTrackData = sp.track(SearchedTrackSeed, market='US')
            global SearchedTrackName1
            SearchedTrackName1 = SearchedTrackData['name']

            #change the value of the "Based on" frame to display the song used to generate the results

            SearchedTrack.configure(text=SearchedTrack.cget('text') + str(SearchedTrackName1))

            #create the button to trigger the search algorithm

        SearchButton = ctk.CTkButton(SearchFrame, height=40, width=100, text="Search", command=SearchRecommendations, font=Titlefont)
        SearchButton.place(relx=0.5, rely=0.7, anchor="center")

        def CreateSearchedPlaylist():

            #creates a playlist for the tracks to be inputted into 
            Clearfile = open("SearchedRecommendationIDs.txt", mode="w")
            Clearfile.close()
            
            scope = 'playlist-modify-private'
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
            results = sp.current_user()
            userID = results['id']

            SearchedRecommnedationPlaylist = sp.user_playlist_create(user=userID, name=f"Based on: {SearchedTrackName1}", public=False, description=f"Generated using Spotistats application based on the song: {SearchedTrackName1}")

            #converts the song names into the song ID's so they can be added to the playlist 
            with open("SearchedRecommendationsFile.txt") as open_file:

                lines = open_file.readlines()
                count = 0
                for line in lines:
                        count += 1
                        TrackName = line
                        TrackName = str(TrackName)
                        TrackName = TrackName.replace("("," ")
                        TrackName = TrackName.replace(")"," ")
                        TrackName = TrackName.replace("'"," ")
                        TrackName = TrackName[5:]

                
                        
                        
                        #searches for the song ID and adds it to a text file with 20 others 
                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
                        results = sp.search(TrackName)
                        TrackId = results['tracks']['items'][0]['id']
                        SearchedRecommendationIDFile = open("SearchedRecommendationIDs.txt", mode="a", encoding='utf-8')
                        SearchedRecommendationIDFile.write(str(TrackId) + "\n")

                        
            #opens the previous text file and converts it into a list to be inputted to the 'add_tracks' function 
            file = open('SearchedRecommendationIDs.txt', 'r')
            data = file.read()
            TrackIds = data.replace('\n', ' ').split()
            #adds the list of tracks to the playlist created earlier 
            PlaylistID = SearchedRecommnedationPlaylist['id']
            sp.user_playlist_add_tracks(user=userID, playlist_id=PlaylistID, tracks=TrackIds)

            SearchedCompletedPlaylistLabel.configure(text="Playlist Created!") 
            
            

        #creates the button to trigger the above function 
        SearchedAddPlaylistButton = ctk.CTkButton(SearchedAddPlaylistFrame, text="Create", font=Titlefont, height=40, width=100, command= CreateSearchedPlaylist)
        SearchedAddPlaylistButton.place(relx=0.5, rely=0.4, anchor='center')






