# imports the tkinter module
import tkinter  
#imports the custom tkinter module as ctk to reduce length of name 
import customtkinter as ctk  



#class for the logout page 
class Logout(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Logout Page")
        label.pack(padx=10, pady=10)

        from profile_1 import Profile
        switch_window_button_left = ctk.CTkButton(self,text="Profile Page",height=100, width=170,  command=lambda: controller.show_frame(Profile))
        switch_window_button_left.pack(side="bottom", anchor="sw")

        from login import Login 
        logout_button = ctk.CTkButton(self, text="Logout", command=lambda: controller.show_frame(Login))
        logout_button.place(relx=0.5, rely=0.5, anchor= "center")
