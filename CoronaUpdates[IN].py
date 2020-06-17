#!/usr/bin/python3
import requests 
from bs4 import BeautifulSoup
from tkinter import * 
import subprocess
import tkinter.font as tkFont

#Initates the request
link="https://www.mohfw.gov.in/"
req = requests.get(link)

#This part determines the status code of the request. 200 meaning that it was a success
def checkstatuscode():
    if req.status_code==200:
        statuscode="The request was successful!"
        color = "green"
    else:
        statuscode="Error!"
        color = "red"
    label4 = Label(root, text=statuscode, font=fontStyle, fg=color)
    label4.grid(column=1, row=1)
#This function defines the variables of the active,inactive and deathcases and passes them to label to be displayed
def getupdate():
    #This part outputs the number of active cases
    activecases = str(active)
    for x0 in activecases:
        activecases = activecases.replace("'", "")
        activecases = activecases.replace("[", "")
        activecases = activecases.replace("]", "")
    label1 = Label(root, text="Active cases : " + activecases, font=fontStyle)
    label1.grid(column=0, row=1)
    #This part outputs the number of inactive cases
    inactivecases = str(inactive)
    for x1 in inactivecases:
        inactivecases = inactivecases.replace("'", "")
        inactivecases = inactivecases.replace("[", "")
        inactivecases = inactivecases.replace("]", "")
    label2 = Label(root, text="Inactive cases : " + inactivecases, font=fontStyle)
    label2.grid(column=0, row=2)
    #This part outputs the total number of cases
    ac = int(activecases)
    inac = int(inactivecases)
    totalcases = ac + inac
    label3 = Label(root, text="Total Cases : " + str(totalcases), font=fontStyle)
    label3.grid(column=0,row=3)
    #This part outputs the number of death cases
    deathcases = str(deaths)
    for x2 in deathcases:
        deathcases = deathcases.replace("'", "")
        deathcases = deathcases.replace("[", "")
        deathcases = deathcases.replace("]", "")
    label4 = Label(root, text="Deaths : " + deathcases, font=fontStyle)
    label4.grid(column=0, row=4)
    
#This part is what grabs the html elements of the page
soup = BeautifulSoup(req.content, 'html.parser')
for element in soup.find_all('li', class_="bg-blue")[0].find_all("strong"):
    active = element.find_all(text=True)
for element1 in soup.find_all('li', class_="bg-green")[0].find_all("strong"):
    inactive = element1.find_all(text=True)
for element2 in soup.find_all('li', class_="bg-red")[0].find_all("strong"):
    deaths = element2.find_all(text=True)
    
#This is the tkinter part - responsible for the GUI
root = Tk()

#Determines the font of the label
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

#The get update button
Button1 = Button(root, text="Get updates",command=getupdate, fg="black", bg="#dcdcdc")
Button1.grid(row=0,column=0)

Button2 = Button(root, text="Check status code", command=checkstatuscode, fg="black", bg="#dcdcdc")
Button2.grid(row=0,column=1)

#Implements fullscreen when opening
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

#Determines the title screen
root.title("Corona Updates")

#The icon of the app(show in the titlebar)
#Bug : For some reason the dekstop entry doesn't work when the below lines are un-commented. The below code makes the icon work just fine. But icon here and desktop entries cannot be used simultaneously together
#img = PhotoImage(file='toxic2.png')
#root.call('wm', 'iconphoto', root._w, img)
#Credits for the icon : "Icon made by Freepik from www.flaticon.com"

root.mainloop()
