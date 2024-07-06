# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  
#imports pillow to allow an image to be place in a frame 
from PIL import  ImageTk, Image 
#imports hashing algorithms to use for passwords
import hashlib
#imports library to allow for checking of characters 
import re 
#imports pages needed to switch to 
from homepage import HomePage
#imports time library to allow for loading times
import time 

#class for the login page 
class Login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        

        def SignUpEvent():
            SignUpUsername = username.get()
            username.delete(first_index=0, last_index=20)
            SignUpPassword = password.get()
            password.delete(first_index=0, last_index=20)

            HashingPassword = hashlib.sha256(SignUpPassword.encode())
            global HashPassword
            HashPassword = HashingPassword.hexdigest()

            HasNumber = any(chr.isdigit() for chr in SignUpPassword)
            
            UsernameTaken = 0
            for line in open("Credentials.txt", "r").readlines():
                CredentialsInfo = line.split()
                if SignUpUsername == CredentialsInfo[0]:
                    UsernameTaken = 1
                  
            
            print("Username taken: ", UsernameTaken)


            if len(SignUpPassword) < 8:
                  errorMessage.configure(text="Password is too short!")
            elif SignUpPassword.islower() == True:
                errorMessage.configure(text= "Password must include an uppercase character!")
            elif HasNumber == False:
                errorMessage.configure(text="Password must contain a number!")
            elif SignUpUsername == "":
                errorMessage.configure(text="Username cannot be blank!")
            elif UsernameTaken == 1:
                errorMessage.configure(text="Username already taken! Try login instead!")
            else:
                credentials = open("Credentials.txt", "a")
                credentials.write(SignUpUsername + " ")
                credentials.write(HashPassword + "\n")
                credentials.close()
                
                controller.show_frame(HomePage)

        #Procedure that controls what happens when the user enters their details into the entry boxes and presses the login button. 
        #is called when the login button is pressed, data is extracted from the text entry widgets, hashed and compared with stored values 
        def LoginEvent():
            
            #gets the text that has been entered into the entry boxes 
            LoginUsername = username.get()
            username.delete(first_index=0, last_index=20)
            LoginPassword = password.get()
            password.delete(first_index=0, last_index=20)

            #hashes the value that was entered using the SHA256 hashing algorithm 
            HashingPassword = hashlib.sha256(LoginPassword.encode())
            global HashPassword
            HashPassword = HashingPassword.hexdigest()

            #opens the credentials file and compares the hashed password value to each line of the credentials file to see if a match is found 
            #if a match is found the user is redirected to the homepage, if not the user is told to try again 
            for line in open("Credentials.txt", "r").readlines():
                CredentialsInfo = line.split()
                if LoginUsername == CredentialsInfo[0] and HashPassword == CredentialsInfo[1]:
                    controller.show_frame(HomePage)
                    
                else:
                    errorMessage.configure(text="Incorrect Credentials!")




        title = ctk.CTkLabel(self, text="Login")
        title.pack(padx=10, pady=10)

        #assigns the image in the folder to the variable named logo and sets the size of the image 
        logo = ctk.CTkImage(Image.open("D:\Code\Spotipy\SpotistatsLogo.png"), size= (650,100))
        
        #creates a label widget and places the image whithin this label 
        imageLabel = ctk.CTkLabel(self, image=logo, text= "")
        imageLabel.place(relx = 0.5, rely=0.2, anchor="center")

        #creates the username entry box 
        username = ctk.CTkEntry(self, placeholder_text="Username", width=350)
        username.place(relx=0.5, rely=0.35, anchor="center")

        #creates the password entry box
        password = ctk.CTkEntry(self, placeholder_text="Password", width=350)
        password.place(relx=0.5, rely=0.39, anchor="center")

        #creates the login button 
        loginButton = ctk.CTkButton(self, text="Login", command= LoginEvent)
        loginButton.place(relx=0.5, rely=0.43, anchor="center")

        #creates the sign up button 
        signupButton = ctk.CTkButton(self, text= "Sign up", fg_color="transparent",  text_color="#1db954", command=SignUpEvent)
        signupButton.place(relx=0.5, rely=0.46, anchor="center" )

        #creates the error message label
        errorMessage = ctk.CTkLabel(self, text="", text_color="red")
        errorMessage.place(relx=0.5, rely=0.5, anchor="center")

        #creates success message label
        SuccessMessage = ctk.CTkLabel(self, text="", text_color="Green")
        SuccessMessage.place(relx=0.5, rely= 0.52, anchor="center")







            


    