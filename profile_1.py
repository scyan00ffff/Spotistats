# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
import urllib
import webbrowser
from PIL import ImageTk , Image
from itertools import islice 


#class for the profile page 
class Profile(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Profile")
        label.pack(padx=10, pady=10)

        from logout import Logout
        from recon import Recon
        switch_window_button_right = ctk.CTkButton(self,text="Logout Page",height=100, width=170,  command=lambda: controller.show_frame(Logout))
        switch_window_button_left = ctk.CTkButton(self,text="Recommendations",height=100, width=170,  command=lambda: controller.show_frame(Recon))
        switch_window_button_right.pack(side="bottom", anchor="e")
        switch_window_button_left.pack(side="bottom", anchor="sw")



        Titlefont = ctk.CTkFont("Gothham Circular", 18, "bold")
        TitlefontUnderline = ctk.CTkFont("Gothham Circular ", 25, "bold", underline=True)
        Bodyfont = ctk.CTkFont("Gotham Circular", 18,)

        MainFrame = ctk.CTkFrame(self,height=850, width=700)
        MainFrame.place(relx=0.5, rely=0.5, anchor="center")
        Title = ctk.CTkLabel(MainFrame, text="Profile", font=TitlefontUnderline)
        Title.place(relx=0.5,rely=0.1,anchor="center")


        NameLabel = ctk.CTkLabel(MainFrame, text="Name: ", font= Bodyfont )
        NameLabel.place(relx=0.1, rely= 0.2, anchor="nw")

        ProfilePlanLabel = ctk.CTkLabel(MainFrame, text="Plan: ", font= Bodyfont )
        ProfilePlanLabel.place(relx=0.1, rely= 0.25, anchor="nw")

        FollowersLabel = ctk.CTkLabel(MainFrame, text="Followers: ", font= Bodyfont )
        FollowersLabel.place(relx=0.1, rely= 0.3, anchor="nw")

        ProfileCountryLabel = ctk.CTkLabel(MainFrame, text="Country: ", font= Bodyfont )
        ProfileCountryLabel.place(relx=0.1, rely= 0.35, anchor="nw")

        TopSongsTitleLabel = ctk.CTkLabel(MainFrame, text="Top Songs: ", font=TitlefontUnderline)
        TopSongsTitleLabel.place(relx=0.1, rely= 0.55, anchor="sw")

        TopSongsLabel = ctk.CTkLabel(MainFrame, text="", font=Bodyfont)
        TopSongsLabel.place(relx=0.1, rely=0.6, anchor="nw")

        TopArtistsTitleLabel = ctk.CTkLabel(MainFrame, text="Top Artists: ", font=TitlefontUnderline)
        TopArtistsTitleLabel.place(relx=0.82, rely= 0.55, anchor="se")

        TopArtistsLabel = ctk.CTkLabel(MainFrame, text="", font=Bodyfont)
        TopArtistsLabel.place(relx=0.85, rely=0.6, anchor="ne")




            #adds metrics to the above defined labels 

        #opens the profile info file to select the Country from the file and display it in the relevant label widget whithin the profile frame     
        with open ("Profileinfo.txt") as open_file:
            lines = open_file.readlines()
            country = lines[14]
            parsedCountry = str(country)
            parsedCountry = parsedCountry.replace("'", " ")
            ProfileCountryLabel.configure(text =ProfileCountryLabel.cget("text") + parsedCountry[13:15])

        #opens the profile info file to select the ProfilePlan from the file and display it in the relevant label widget whithin the profile frame                           
        with open ("Profileinfo.txt") as open_file:
            lines = open_file.readlines()
            plan = lines[15]
            parsedPlan = str(plan)
            parsedPlan = parsedPlan.replace("'", " ")
            ProfilePlanLabel.configure(text =ProfilePlanLabel.cget("text") + parsedPlan[13:20])

        #opens the profile info file to select the Followers from the file and display it in the relevant label widget whithin the profile frame   
        with open ("Profileinfo.txt") as open_file:
            lines = open_file.readlines()
            followers = lines[13]
            parsedFollowers = str(followers)
            parsedFollowers = parsedFollowers.replace("'", " ")
            parsedFollowers = parsedFollowers.replace("}", " ")
            FollowersLabel.configure(text =FollowersLabel.cget("text") + parsedFollowers[9:])    

        #opens the profile info file to select the Name from the file and display it in the relevant label widget whithin the profile frame   
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
                

        profileLink = ctk.CTkButton(MainFrame, text = "Spotify Profile", font=Bodyfont,command=callback)
        profileLink.place(relx=0.1, rely= 0.42, anchor="nw")
            
        

            
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
      
        urllib.request.urlretrieve(img_url, "ProfilePic.png") 
            
        ProfilePic = ctk.CTkImage(Image.open("ProfilePic.png"), size=(64,64))
        ProfilePicLabel = ctk.CTkLabel(MainFrame,text="", image=ProfilePic)
        ProfilePicLabel.place(relx= 0.35, rely= 0.2)

        global limit 
        limit = 5

        #opens the toptartists file and retrieves the top x number of items, writing each one at a time to the label in the above frame 
        with open ("TopArtistsLong.txt") as open_file:
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
                TopArtistsLabel.configure(text =TopArtistsLabel.cget("text") + x + "\n")
        
        #opens the toptracks file and retrieves the top x number of items, writing each one at a time to the label in the above frame 
        with open ("TopTracksLong.txt") as open_file:
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
                TopSongsLabel.configure(text =TopSongsLabel.cget("text") + x + "\n")

