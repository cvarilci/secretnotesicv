import base64
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pybase64
import os


window = tk.Tk()
window.title("SECRET NOTES")
window.config(padx=40, pady=40)

image = Image.open("topsecret.jpg")
resized_image = image.resize((75,75))
photo = ImageTk.PhotoImage(resized_image)
label = tk.Label(window, image=photo)
label.pack()

def decrypt():
    your_masterkey = enter_masterkey_entry.get()
    if your_masterkey == "007":
        your_textbox = enter_yoursecret_textbox.get("1.0", "end")
        decode_message = your_textbox.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")
        #print(decrypt)
        enter_yoursecret_textbox.delete("1.0", "end")
        enter_yoursecret_textbox.insert(END,decrypt)

    elif your_masterkey == "":
        messagebox.showerror("Decrypt", "Input Master Key")
    elif your_masterkey != "007":
        messagebox.showerror("Decrypt", "Invalid Master Key")

    enter_masterkey_entry.delete(0, "end")

def secrets():
    global window
    global your_masterkey
    global enter_yoursecret_textbox

    filename="topsecret.txt"
    with open(filename,"a") as file_object:
        your_title=enter_yourtitle_entry.get()
        your_masterkey=enter_masterkey_entry.get()
        #print(your_masterkey)
        file_object.write("\n"+your_title)

        #your_textbox = enter_yoursecret_textbox.get("1.0", "end")
        if your_masterkey=="007":
            your_textbox = enter_yoursecret_textbox.get("1.0", "end")
            encode_message=your_textbox.encode("ascii")
            base64_bytes=base64.b64encode(encode_message)
            encrypt=base64_bytes.decode("ascii")
            file_object.write("\n"+encrypt)
        elif your_masterkey=="":
            messagebox.showerror("Save & Encrypt","Input Master Key")
        elif your_masterkey!="007":
            messagebox.showerror("Save & Encrypt","Invalid Master Key")



        #file_object.write("\n"+your_textbox)

        enter_yourtitle_entry.delete(0,"end")
        enter_yoursecret_textbox.delete("1.0","end")
        enter_masterkey_entry.delete(0,"end")

enter_yourtitle_label=tk.Label(text="Enter your title")
enter_yourtitle_label.pack()

enter_yourtitle_entry=tk.Entry(width=30)
enter_yourtitle_entry.pack()

enter_yoursecret_label=tk.Label(text="Enter your secret text")
enter_yoursecret_label.pack()

enter_yoursecret_textbox= tk.Text(width=30,height=10)
enter_yoursecret_textbox.focus()
enter_yoursecret_textbox.pack()

enter_masterkey_label=tk.Label(text="Enter master key")
enter_masterkey_label.pack()

#enter_masterkey_entry=tk.Entry(width=30)
password=StringVar()
enter_masterkey_entry=tk.Entry(textvariable=password,width=30)
enter_masterkey_entry.pack()

save_cript_button=tk.Button(text="Save&Encrypt",command=secrets)
save_cript_button.pack()

decript_button=tk.Button(text="Decrypt",command=decrypt)
decript_button.pack()






window.mainloop()