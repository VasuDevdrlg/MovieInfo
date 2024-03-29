import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import movieapi as m

def download_and_resize(url, width=150):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.thumbnail((width, width))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error downloading/resizing image: {e}")
        return None

def search_movie():
    movie_name = entry_movie_name.get()
    year=entry_yr.get()
    movie_details = m.movieinfo(movie_name,year)

    for key, value in movie_details.items():
        if key=="Poster":
            continue
        textboxes[key].config(state='normal')
        textboxes[key].delete(1.0, tk.END)
        textboxes[key].insert(tk.END, value)
        textboxes[key].config(state='disabled')

    updated_img = download_and_resize(movie_details["Poster"])
    if updated_img:
        image.config(image=updated_img)
        image.image = updated_img

root = tk.Tk()
root.title("Movie Infograbber")

title = tk.Label(root, text="Movie Infograbber", font=("Arial", 15), bg="orange", fg="black")
title.pack(pady=10)

img_frame = tk.Frame(root, width=100, height=50)
img_frame.pack(side="top")
url ="https://t3.ftcdn.net/jpg/02/54/97/90/240_F_254979077_fT8mZRi2Vqpo5hh6A4RAr9sDWWhts17O.jpg"
img = download_and_resize(url)
if img:
    image = tk.Label(root, image=img)
    image.pack()
else:
    print("Failed to load image.")

label_movie_name = tk.Label(root, text="Enter Movie Name:")
label_movie_name.pack()
entry_movie_name = tk.Entry(root)
entry_movie_name.pack()
label_yr = tk.Label(root, text="Enter Year:")
label_yr.pack()
entry_yr = tk.Entry(root)
entry_yr.pack()

search_button = tk.Button(root, text="Search", command=search_movie, bg="green", fg="white")
search_button.pack(pady=5)

textboxes = {}
details_frame = ttk.LabelFrame(root, text="Movie Details", padding=10)
details_frame.pack(pady=10)

essential_details = ["Title","Director", "Release Year", "Genre", "IMDb Rating", "Box Office"]

for detail in essential_details:
    label = ttk.Label(details_frame, text=detail + ":")
    label.grid(column=0, row=essential_details.index(detail), padx=5, pady=5)
    textbox = tk.Text(details_frame, height=1, width=30, state='disabled', bg="lightyellow")
    textbox.grid(column=1, row=essential_details.index(detail), padx=5, pady=5)
    textboxes[detail] = textbox

root.mainloop()
