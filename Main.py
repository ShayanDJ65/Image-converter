import tkinter as tk 
import customtkinter as ct  
from tkinter import filedialog as fd 
import pyglet 
from PIL import Image,ImageTk
select_filetypes = [ ('Image file', '*.jpg'), ('Image file', '*.png'),('Image file', '*.jpeg'),('Image file', '*.tff') ] # filetypes for selection
def selectfile(): # function to select and show the image 
    global img_path
    global opened_img
    global photo
    img_path = fd.askopenfilename(filetypes=select_filetypes)
    opened_img = Image.open(img_path)
    opened_img.thumbnail((400,250))
    photo = ImageTk.PhotoImage(opened_img)
    directory_label.configure(text=img_path)
    image_lbl.configure(image=photo)
    Buttons_frame.grid(row=3, column = 1, columnspan = 3,sticky = "WE",pady=10)
def savefile(id): #func to save the image with selected format 
    global saved_file
    if id == 1:
        saved_file = fd.asksaveasfile(filetypes=[ ('Image file', '*.jpeg')])
    elif id ==2:
        saved_file = fd.asksaveasfile(filetypes=[ ('Image file', '*.jpeg')])
    elif id==3:
        saved_file = fd.asksaveasfile(filetypes=[ ('Image file', '*.png')])
    elif id == 4 :
        saved_file = fd.asksaveasfile(filetypes=[ ('Image file', '*.tff')])

#=======Main Window =============
root = ct.CTk()
root.geometry("650x500")
root.resizable(width=False, height=False)
ct.set_appearance_mode("dark") 
root.title("Simple Image Converter")
#==========================
title_frame = ct.CTkFrame(root)
Title_txt = ct.CTkLabel(root, text="Welcome to Simple Image Converter", text_color="White", text_font=("Excluded", 20, 'bold')) # title
# Title_txt.grid(row = 0, column = 0,pady=10, columnspan=5)
Title_txt.place(relx = 0.5,rely=0.05, anchor = tk.CENTER)
#==========================
openfile_btn = ct.CTkButton(root, text="Open an image", command = selectfile,width=120) # openfile button
openfile_btn.grid(row = 1, columnspan=2,pady=(80,10),column=0)
#==========================
directory_label = ct.CTkLabel(bg_color = "white",text_color="black",height=20,width=410,text="")
directory_label.grid(columnspan = 4,row = 1,column =1,padx=(145,0),pady = (70,2))
#==========================
Image_frame = ct.CTkFrame(root, width=500,height=230)
Image_frame.grid(row=2,column = 0,columnspan=4,pady=20)
image_lbl = ct.CTkLabel(Image_frame,text="",image = "",bg_color="#212225")
image_lbl.pack()
#===========Buttons Section ============#
Buttons_frame = ct.CTkFrame(root, width=650, height=200,fg_color="#212225")
Jpg_btn = ct.CTkButton(Buttons_frame, width = 80, height= 70, text="To JPG",text_font=("Excluded", 15, 'bold'),command= lambda: savefile(1))
Jpg_btn.grid(row = 0, column = 0, padx = (120,15),)
Jpeg_btn = ct.CTkButton(Buttons_frame, width = 80, height= 70, text="To JPEG",text_font=("Excluded", 15, 'bold'),command= lambda: savefile(2))
Jpeg_btn.grid(row = 0, column = 1, padx = 15)
Png_btn = ct.CTkButton(Buttons_frame, width = 80, height= 70, text="To PNG",text_font=("Excluded", 15, 'bold'),command= lambda: savefile(3))
Png_btn.grid(row = 0, column = 2, padx = 15)
Ttf_btn = ct.CTkButton(Buttons_frame, width = 80, height= 70, text="To TTF",text_font=("Excluded", 15, 'bold'),command= lambda: savefile(4))
Ttf_btn.grid(row = 0, column = 3, padx = (15,120))
#=======================================#
copyright_txt = ct.CTkLabel(root, text = "Designed by Shayan Hosseinzadeh",text_font=('Excluded',12,'bold'))
copyright_txt.place(relx = 0.5,anchor = tk.CENTER,rely=0.97)



root.mainloop()