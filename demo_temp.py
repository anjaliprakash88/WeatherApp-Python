from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=68d82bb461b060788079773451e4da1e").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("Weather App")
win.config(bg="pink")
win.geometry("500x570")


name_label = Label(win, text="WEATHER APP", font=("Time New Roman", 40, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


city_name = StringVar()
com = ttk.Combobox(win, text="WEATHER APP", values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)



w_label = Label(win, text="weather climate", font=("Time New Roman", 10, "bold"))
w_label.place(x=75, y=260, height=40, width=150)
w_label1 = Label(win, text=" ", font=("Time New Roman", 10, "bold"))
w_label1.place(x=275, y=260, height=40, width=150)



wd_label = Label(win, text="weather description", font=("Time New Roman", 8, "bold"))
wd_label.place(x=75, y=330, height=40, width=150)
wd_label1 = Label(win, text=" ", font=("Time New Roman", 8, "bold"))
wd_label1.place(x=275, y=330, height=40, width=150)


temp_label = Label(win, text="temperature", font=("Time New Roman", 8, "bold"))
temp_label.place(x=75, y=400, height=40, width=150)
temp_label1 = Label(win, text=" ", font=("Time New Roman", 8, "bold"))
temp_label1.place(x=275, y=400, height=40, width=150)


per_label = Label(win, text="temperature", font=("Time New Roman", 8, "bold"))
per_label.place(x=75, y=470, height=40, width=150)
per_label1 = Label(win, text=" ", font=("Time New Roman", 8, "bold"))
per_label1.place(x=275, y=470, height=40, width=150)




done_button = Button(win, text="Done", font=("Time New Roman", 15, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)


win.mainloop()