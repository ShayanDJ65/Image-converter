import tkinter as tk 
import customtkinter as ct  
from tkinter import filedialog as fd 
import pyglet 
from PIL import Image

selected_img = ""
filetypes = ( ('Image files', '*.jpg'), ('Image files', '*.png'),('Image files', '*.jpeg') )
def selectfile():
    global selected_img
    selected_img = fd.askopenfilename(filetypes=filetypes)
    directory_label.configure(text=selected_img)
    opened_img = Image.open(selected_img)

#=======Main Window =============
root = ct.CTk()
root.geometry("650x400")
root.resizable(width=False, height=False)
ct.set_appearance_mode("system") # light or dark deponds on user's default 
root.rowconfigure(2)
#================================
Title_txt = ct.CTkLabel(root, text="Welcome to Simple Image Converter", text_color="White", text_font=("Excluded", 20, 'bold')) # title
Title_txt.grid(row = 0, column = 2,sticky = "N")
openfile_btn = ct.CTkButton(root, text="Open an image", command = selectfile,width=120) # openfile button
openfile_btn.grid(row = 1, columnspan=2,pady=35, padx=10)
directory_label = ct.CTkLabel(bg_color = "white",text_color="black",height=20,width=400,text="")
directory_label.grid(columnspan = 3,row = 1,column =2)
Image_frame = ct.CTkFrame(root, width=500,height=200)
Image_frame.grid(row=2,column = 0,columnspan = 5)


root.mainloop()