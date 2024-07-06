# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
#imports pillow to allow an image to be place in a frame 
from PIL import  ImageTk, Image 
from stats import Stats
from profile import Profile
from recon import Recon
from logout import Logout 

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

import ast
import json 

import webbrowser

from io import BytesIO
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen
import urllib.request


#class for the home page 
class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        Titlefont = ctk.CTkFont("Gothham Circular", 28, "bold")
        TitlefontUnderline = ctk.CTkFont("Gothham Circular ", 18, "bold", underline=True)
        Bodyfont = ctk.CTkFont("Gotham Circular", 16, "bold")
        
        label = ctk.CTkLabel(self, text="Home Page")
        label.pack(padx=10, pady=10)
        
        
        from stats import Stats
        switch_window_button_right = ctk.CTkButton(self,text="Statistics Page",height=100, width=170,  command=lambda: controller.show_frame(Stats))
        switch_window_button_right.pack(side="bottom", anchor="e")
    


        #assigns the image in the folder to the variable named logo and sets the size of the image 
        logo = ctk.CTkImage(Image.open("D:\Code\Spotipy\SpotistatsLogo.png"), size= (650,100))

        #creates a label widget and places the image whithin this label 
        imageLabel = ctk.CTkLabel(self, image=logo, text= "")
        imageLabel.place(relx = 0.5, rely=0.1, anchor="center")

        #initialises the frame that will display the recently played results
        def RecentlyPlayed():
            #creates frame with a height of 700 pixels by 450 pixels 
            RecentlyDisplayedFrame = ctk.CTkFrame(self, height=700, width= 450)
            RecentlyDisplayedFrame.place(relx=0.1 ,rely=0.2, anchor= "nw")
            #creates a label to display the text "Recently Played"
            RecentlyDisplayedLabel = ctk.CTkLabel(RecentlyDisplayedFrame, text="Recently Played", font=TitlefontUnderline)
            RecentlyDisplayedLabel.place(relx=0.5, rely=0.1, anchor="center")
            
            #opens the text file created by the API request and reads the top 10 lines of the file 
            file1 = open("recently_played.txt", "r")
            specifiedLines = [0,1,2,3,4,5,6,7,8,9,10]
            #adds an index number to each item read from the text file and adds them to an array called songs
            songs = []
            for pos, items in enumerate (file1):
                if pos in specifiedLines:
                    songs.append(items)

            #creates the label for the results to be diplayed into 
            one = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            one.place(relx= 0.5, rely=0.3, anchor="center")


            #opens the text file with the results stored in and parses it to remove any unncessary characters such as punctuation 
            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                One = lines[0]
                x = str(One)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                #adds each line from the text file into the label on screen 
                one.configure(text =one.cget("text") + x +"\n") 


            two = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            two.place(relx= 0.5, rely=0.35, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Two = lines[1]
                x = str(Two)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                two.configure(text =two.cget("text") + x+"\n") 

            
            three = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            three.place(relx= 0.5, rely=0.4, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Three = lines[2]
                x = str(Three)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                three.configure(text =three.cget("text") + x+"\n") 

            
            four = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            four.place(relx= 0.5, rely=0.45, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Four = lines[3]
                x = str(Four)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                four.configure(text =four.cget("text") + x+"\n") 


            five = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            five.place(relx= 0.5, rely=0.5, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Five = lines[4]
                x = str(Five)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                five.configure(text =five.cget("text") + x+"\n")


            six = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            six.place(relx= 0.5, rely=0.55, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Six = lines[5]
                x = str(Six)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                six.configure(text =six.cget("text") + x+"\n") 


            seven = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            seven.place(relx= 0.5, rely=0.6, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Seven = lines[6]
                x = str(Seven)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                seven.configure(text =seven.cget("text") + x+"\n") 


            eight = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            eight.place(relx= 0.5, rely=0.65, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Eight = lines[7]
                x = str(Eight)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                eight.configure(text =eight.cget("text") + x+"\n") 


            nine = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            nine.place(relx= 0.5, rely=0.7, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Nine = lines[8]
                x = str(Nine)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                nine.configure(text =nine.cget("text") + x+"\n") 


            ten = ctk.CTkLabel(RecentlyDisplayedFrame, text="", font=Bodyfont)
            ten.place(relx= 0.5, rely=0.75, anchor="center")

            with open ("recently_played.txt") as open_file:
                lines = open_file.readlines()
                Ten = lines[9]
                x = str(Ten)
                x=x.replace("[", "")
                x=x.replace("]", "")
                x=x.replace("(", "")
                x=x.replace(")", "")
                x=x.replace("'", "")
                x=x.replace("\\n", "")
                x=x.replace("\\", "")
                x=x.replace(",", " ")
                ten.configure(text =ten.cget("text") + x+"\n") 

        RecentlyPlayed()


        def ProfileOverview():

            #creates the frame for the profile information 

            ProfileOverviewFrame = ctk.CTkFrame(self, height=300, width= 400)
            ProfileOverviewFrame.place(relx=0.9 ,rely=0.2, anchor= "ne")

            #creates the label which reads "Profile"

            ProfileOverviewLabel = ctk.CTkLabel(ProfileOverviewFrame, text="Profile", font=Titlefont)
            ProfileOverviewLabel.place(relx=0.5, rely=0.1, anchor="center")

            #defines and creates empty label widgets to be populated with user data 

            NameLabel = ctk.CTkLabel(ProfileOverviewFrame, text="Name: ", font= Bodyfont )
            NameLabel.place(relx=0.1, rely= 0.2, anchor="nw")

            ProfilePlanLabel = ctk.CTkLabel(ProfileOverviewFrame, text="Plan: ", font= Bodyfont )
            ProfilePlanLabel.place(relx=0.1, rely= 0.3, anchor="nw")

            FollowersLabel = ctk.CTkLabel(ProfileOverviewFrame, text="Followers: ", font= Bodyfont )
            FollowersLabel.place(relx=0.1, rely= 0.4, anchor="nw")

            ProfileCountryLabel = ctk.CTkLabel(ProfileOverviewFrame, text="Country: ", font= Bodyfont )
            ProfileCountryLabel.place(relx=0.1, rely= 0.5, anchor="nw")


           #opens the ProfileInfo text file and parses the data to find the correct line, uses this parsed info and passes it
           #into the correct label whithin the profile frame 
            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                country = lines[14]
                parsedCountry = str(country)
                parsedCountry = parsedCountry.replace("'", " ")
                ProfileCountryLabel.configure(text =ProfileCountryLabel.cget("text") + parsedCountry[13:15])

           #opens the ProfileInfo text file and parses the data to find the correct line, uses this parsed info and passes it
           #into the correct label whithin the profile frame             
            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                plan = lines[15]
                parsedPlan = str(plan)
                parsedPlan = parsedPlan.replace("'", " ")
                ProfilePlanLabel.configure(text =ProfilePlanLabel.cget("text") + parsedPlan[13:20])

           #opens the ProfileInfo text file and parses the data to find the correct line, uses this parsed info and passes it
           #into the correct label whithin the profile frame 
            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                followers = lines[13]
                parsedFollowers = str(followers)
                parsedFollowers = parsedFollowers.replace("'", " ")
                parsedFollowers = parsedFollowers.replace("}", " ")
                FollowersLabel.configure(text =FollowersLabel.cget("text") + parsedFollowers[9:])    


           #opens the ProfileInfo text file and parses the data to find the correct line, uses this parsed info and passes it
           #into the correct label whithin the profile frame 
            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                name = lines[0]
                parsedName = str(name)
                parsedName = parsedName.replace("'", " ")
                NameLabel.configure(text = NameLabel.cget("text") + parsedName[18:])    

            #code to add a clickable link to the users spotify account online/ in the application 

            

            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                profileUrl = lines[1]
                parsedUrl = str(profileUrl)
                parsedUrl = parsedUrl.replace("'", " ")
                parsedUrl = parsedUrl.replace("}", " ")
                parsedUrl = parsedUrl[30:]
                

            new = 1
            url = parsedUrl

            def callback():
                webbrowser.open(url, new=new)
                

            profileLink = ctk.CTkButton(ProfileOverviewFrame, text = "Spotify Profile", font=Bodyfont,command=callback)
            profileLink.place(relx=0.1, rely= 0.8, anchor="nw")
            
        

            # this section opens the profile info text file and parses the data to find the URL needed for the users profile picture
            with open ("Profileinfo.txt") as open_file:
                lines = open_file.readlines()
                image_url = lines[4]
                ParsedUrl = str(image_url)
                ParsedUrl = ParsedUrl.replace("'", " ")
                ParsedUrl = ParsedUrl.replace("}", " ")
                ParsedUrl = ParsedUrl.replace("{", " ")
                ParsedUrl = ParsedUrl.replace("[", " ")
                ParsedUrl = ParsedUrl[19:]
                

            img_url = ParsedUrl
            #the url from the file is used to send a request to the spotify servers to download the image 
            urllib.request.urlretrieve(img_url, "ProfilePic.png") 
            #the image that was downloaded is now placed whithin a label widget in the profile overview frame 
            ProfilePic = ctk.CTkImage(Image.open("ProfilePic.png"), size=(64,64))
            ProfilePicLabel = ctk.CTkLabel(ProfileOverviewFrame,text="", image=ProfilePic)
            ProfilePicLabel.place(relx= 0.7, rely= 0.2)



        ProfileOverview()
        




            




