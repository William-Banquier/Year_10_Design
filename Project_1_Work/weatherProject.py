# #Start by getting API data
# import requests as r
# weatherDataREQUEST = r.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid={APIKEY}&units=metric")

# #Use json to organize data
# import json
# weatherDataJSON = json.loads(weatherDataREQUEST.text)
# from rich import print


# print("The temperature is", weatherDataJSON['main']['temp'], "degrees celcius in", weatherDataJSON['name'])

# print("Right now the city has", weatherDataJSON['weather'][0]['description'])


# print(weatherDataJSON)

#Imports
import tkinter.font as font
from rich import print
import requests as r
import json

from tkinter import *

#Basic Setup
root = Tk()

root.wm_attributes("-topmost", True)
root.wm_attributes("-transparent", True)
root.config(bg='systemTransparent')
# root.tk.call('tk', 'scaling', 2.0)
root.title("Weather Finder")

#API key
apiKey = "201e7478e7be199c5d4c38e10ff2db01"



#Create Functions
def findWeatherData() -> dict: 
    location = inputLocation.get("1.0",END)
    if location == None: return
    weatherDataREQUEST = r.get("http://api.openweathermap.org/data/2.5/weather?q="+location.strip()+"&appid="+apiKey+"&units=metric")
    weatherDataJSON = json.loads(weatherDataREQUEST.text)
   
    
    try:
       print(weatherDataJSON)
       print(weatherDataJSON['main'])
    except: return

    currentInfomation['text'] = ("The temperature is "+ str(weatherDataJSON['main']['temp'])+ " degrees celcius in "+ str(weatherDataJSON['name'])+" "+str(weatherDataJSON['sys']['country'])+ (" At the moment "+str(weatherDataJSON["name"])+" "+str(weatherDataJSON['sys']['country'])+" has "+ str(weatherDataJSON['weather'][0]['description'])))
    
    print(weatherDataJSON)

    return weatherDataJSON


myFont = font.Font(family='sf pro text')

title = Label(root, text="Weather Finder (Version - 0.0)")
title.grid(column=0, row=0, ipadx = 40, columnspan = 5)
title.config(height = 5, foreground="white")
title.config(bg = 'systemTransparent', font=myFont)




currentInfomation = Label(root, wraplength= 350, justify="left",  text="The weather data goes here...")
currentInfomation.grid(column=0, row=1, columnspan=3)
print(currentInfomation['text'])
currentInfomation.config(bg = 'systemTransparent', foreground="white")


explanationOfSoftware = Label(root, wraplength= 350, justify="left",  text="Please write your city in the text box, then after that please press the confirm button.")
explanationOfSoftware.grid(column=4, row=1, columnspan=1)
explanationOfSoftware.config(bg = 'systemTransparent', foreground="white")



inputText = Label(root, text = "Please write the CITY below")
inputText.grid(column = 0, row = 2, columnspan = 2)
inputText.config(bg = 'systemTransparent', foreground="white")


inputLocation = Text(root, height=1, width=28)
inputLocation.grid(column = 0, row = 3, columnspan = 2)
inputLocation.config(foreground="White")
#Having background systemTransparent breaks the program
inputLocation.config(bg = '#BBBBBB')




confirmation = Button(root, text = "Confirm Location", command = findWeatherData)
confirmation.grid(column = 2, row = 3, columnspan = 2)
confirmation.config(fg='white', highlightbackground="systemTransparent")#bg = 'systemTransparent',



root.mainloop()

