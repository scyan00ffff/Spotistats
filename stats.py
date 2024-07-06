# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
from itertools import islice 


#class for the stats page 
class Stats(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Statistics Page")
        label.pack(padx=10, pady=10)

        from homepage import HomePage
        from recon import Recon
        switch_window_button_right = ctk.CTkButton(self,text="Recommendations",height=100, width=170,  command=lambda: controller.show_frame(Recon))
        switch_window_button_left = ctk.CTkButton(self,text="Home Page",height=100, width=170,  command=lambda: controller.show_frame(HomePage))
        switch_window_button_right.pack(side="bottom", anchor="e")
        switch_window_button_left.pack(side="bottom", anchor="sw")

        



        def SwitchTimePeriod(switchTimePeriodValue):
            print("Time period selected: ", switchTimePeriodValue)


        
        Titlefont = ctk.CTkFont("Gothham Circular", 18, "bold")
        TitlefontUnderline = ctk.CTkFont("Gothham Circular ", 18, "bold", underline=True)
        Bodyfont = ctk.CTkFont("Gotham Circular", 16, "bold")

        #TIME LISTENED FRAME 
        #creates a new frame for all of the time listened data which will go into it 
        TimeListenedFrame =ctk.CTkFrame(self, height=150, width = 1220 )
        TimeListenedFrame.place(relx=0.5, rely=0.1, anchor="center")

        #each of the next two lines creates a new empty label ready for data to be added and places them within the time listened frame
        TimeListenedLabel = ctk.CTkLabel(TimeListenedFrame, text="Time Listened", font=TitlefontUnderline)
        TimeListenedLabel.place(relx=0.11, rely=0.05, anchor="nw")

        HoursListenedFrame =ctk.CTkFrame(TimeListenedFrame, height=75, width = 200 )
        HoursListenedFrame.place(relx=0.2, rely=0.6, anchor="center")

        HoursListenedLabel = ctk.CTkLabel(HoursListenedFrame, text="Hours",font=Titlefont)
        HoursListenedLabel.place(relx=0.1, rely=0.05, anchor="nw")

        MinutesListenedFrame =ctk.CTkFrame(TimeListenedFrame, height=75, width = 200 )
        MinutesListenedFrame.place(relx=0.5, rely=0.6, anchor="center")

        MinutesListenedLabel = ctk.CTkLabel(MinutesListenedFrame, text="Minutes",font=Titlefont)
        MinutesListenedLabel.place(relx=0.1, rely=0.05, anchor="nw")

        TotalStreamsFrame =ctk.CTkFrame(TimeListenedFrame, height=75, width = 200 )
        TotalStreamsFrame.place(relx=0.8, rely=0.6, anchor="center")

        StreamsLabel = ctk.CTkLabel(TotalStreamsFrame, text="Streams",font=Titlefont)
        StreamsLabel.place(relx=0.1, rely=0.05, anchor="nw")

        #creates a segmented button with three values that can be adjusted to change the time perdiod of the results and places it in the top corner of the frame
        switchTimePeriodValue = ctk.StringVar(value="4 Weeks")
        switchTimePeriodbutton = ctk.CTkSegmentedButton(TimeListenedFrame, values=["1 Week", "4 Weeks", "6 Months"], command=SwitchTimePeriod, variable=switchTimePeriodValue)
        switchTimePeriodbutton.place(relx= 0.9, rely = 0.1, anchor= "ne")

        #TOP TRACKS FRAME // Creates the frame for all of the statistics to be displayed in 
        #creates the frame for widgets to go whithin 
        TopTracksFrame = ctk.CTkFrame(self, height = 500, width =600)
        TopTracksFrame.place(relx=0.51, rely=0.2)
        #creates the title label for the frame 
        TopTracksLabel = ctk.CTkLabel(TopTracksFrame, text="Top Tracks", font=TitlefontUnderline)
        TopTracksLabel.place(relx=0.5, rely=0.1, anchor="center")
        #creates an empty label which will later be filled with the top tracks data
        TracksLabel = ctk.CTkLabel(TopTracksFrame, text="", font=Bodyfont)
        TracksLabel.place(relx= 0.5, rely=0.6, anchor="center")


        #change value to change number of tracks/artists outputted 
        global limit 
        limit = 10
        #opens the toptracks file and retrieves the top x number of items, writing each one at a time to the top tracks label in the above frame 
        with open ("TopTracksShort.txt") as open_file:
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
                TracksLabel.configure(text =TracksLabel.cget("text") + x + "\n") 


        #function that adds functionality to the previously created segmented button, controls which data is outputted to the label widget depending on the button selection
        def TimePeriodSelection(TimePeriodValue):

            #if the segemented value button is on 4 weeks the data will be retrieved from the toptracksshort file therefore ensuring data is selected from the correct time period 
            if TimePeriodValue == "4 Weeks":
                TracksLabel.configure(text="")

                with open ("TopTracksShort.txt") as open_file:
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
                            TracksLabel.configure(text =TracksLabel.cget("text") + x + "\n") 
            
            elif TimePeriodValue == "6 Months":
                TracksLabel.configure(text="")

                with open ("TopTracksMed.txt") as open_file:
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
                        TracksLabel.configure(text =TracksLabel.cget("text") + x + "\n") 

            elif TimePeriodValue == "1 Year":
                TracksLabel.configure(text="")

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
                        TracksLabel.configure(text =TracksLabel.cget("text") + x + "\n") 

        TimePeriodValue = ctk.StringVar(value="4 Weeks")
        TimePeriodButton = ctk.CTkSegmentedButton(TopTracksFrame , values= ["4 Weeks", "6 Months", "1 Year"], command=TimePeriodSelection, variable=TimePeriodValue)
        TimePeriodButton.place(relx= 0.95, rely=0.05, anchor="ne")




        #TOP ARTISTS FRAME 

        TopArtistsFrame = ctk.CTkFrame(self, height=500, width=600)
        TopArtistsFrame.place(relx= 0.18, rely=0.2)

        TopArtistsLabel = ctk.CTkLabel(TopArtistsFrame, text="Top Artists", font=TitlefontUnderline)
        TopArtistsLabel.place(relx=0.5, rely=0.1, anchor="center")

        ArtistsLabel = ctk.CTkLabel(TopArtistsFrame, text="", font=Bodyfont)
        ArtistsLabel.place(relx= 0.5, rely=0.6, anchor="center")

        with open ("TopArtistsShort.txt") as open_file:
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
                ArtistsLabel.configure(text =ArtistsLabel.cget("text") + x + "\n") 

        def ArtistTimePeriodSelection(TimePeriodValue):


            if TimePeriodValue == "4 Weeks":
                ArtistsLabel.configure(text="")

                with open ("TopArtistsShort.txt") as open_file:
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
                            ArtistsLabel.configure(text =ArtistsLabel.cget("text") + x + "\n") 
            
            elif TimePeriodValue == "6 Months":
                ArtistsLabel.configure(text="")

                with open ("TopArtistsMed.txt") as open_file:
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
                        ArtistsLabel.configure(text =ArtistsLabel.cget("text") + x + "\n") 

            elif TimePeriodValue == "1 Year":
                ArtistsLabel.configure(text="")

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
                        ArtistsLabel.configure(text =ArtistsLabel.cget("text") + x + "\n") 

        TimePeriodValue = ctk.StringVar(value="4 Weeks")
        TimePeriodButton = ctk.CTkSegmentedButton(TopArtistsFrame , values= ["4 Weeks", "6 Months", "1 Year"], command=ArtistTimePeriodSelection, variable=TimePeriodValue)
        TimePeriodButton.place(relx= 0.95, rely=0.05, anchor="ne")



