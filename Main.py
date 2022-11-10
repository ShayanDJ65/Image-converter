import tkinter as tk 
import customtkinter as ct  
from tkinter import filedialog as fd 
import pyglet 
from PIL import Image,ImageTk
filetypes = ( ('Image files', '*.jpg'), ('Image files', '*.png'),('Image files', '*.jpeg') )
def selectfile():
    global img_path
    global opened_img
    global photo
    img_path = fd.askopenfilename(filetypes=filetypes)
    opened_img = Image.open(img_path)
    opened_img.thumbnail((500,500))
    photo = ImageTk.PhotoImage(opened_img)
    directory_label.configure(text=img_path)
    image_lbl.configure(image=photo)
#=======Main Window =============
root = ct.CTk()
root.geometry("650x500")
root.resizable(width=False, height=False)
ct.set_appearance_mode("system") # light or dark deponds on user's default 
#==========================
Title_txt = ct.CTkLabel(root, text="Welcome to Simple Image Converter", text_color="White", text_font=("Excluded", 20, 'bold')) # title
Title_txt.grid(row = 0, column = 2,pady=10)
#==========================
openfile_btn = ct.CTkButton(root, text="Open an image", command = selectfile,width=120) # openfile button
openfile_btn.grid(row = 1, columnspan=2,pady=35, padx=20)
#==========================
directory_label = ct.CTkLabel(bg_color = "white",text_color="black",height=20,width=410,text="")
directory_label.grid(columnspan = 2,row = 1,column =2)
#==========================
Image_frame = ct.CTkFrame(root, width=500,height=230)
Image_frame.grid(row=2,column = 0,columnspan=5,padx = 60)
image_lbl = tk.Label(Image_frame,text="",image = "")
image_lbl.pack()
#==========================
root.mainloop()