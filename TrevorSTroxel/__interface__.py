import os
import tkinter as tk 
from tkinter import *
from tkinter.filedialog import askopenfilename
from __Generate_Hotfix import test1, test2, test3, test4
#reference: https://www.geeksforgeeks.org/python-gui-tkinter/

#This is used as a referencesto look and see what are the names of the game folders
FileNames = ["Alisma", "CohtmlPlugin", "Config", "Content", "Dandelion", "DatasmithContent", "Engine", "Game", "GbxAI", "GbxBlockingVolumes", "GbxGameSystemCore", "GbxJira","GbxSharedBlockoutAssets","GbxSpawn","Geranium","Hibiscus","HoudiniEngine","Ixora","MediaCompositing","OakGame","Paper2D","WwiseEditor"] #stores folder names

#the user is able to choose a json file
def filechoice():
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    raw_path = os.path.splitext(file)[0] #Removes the files extention, as we dont need it
    i = 0
    index = 0
    while index <= 0:
        Find = "/" + FileNames[i] 
        i+=1   
        if Find in raw_path:
            index = raw_path.find(Find) 
    True_Path = raw_path[index::] #this is the data we need to pass in information
#Creates a new window for the user to see and for the commands to be used


def NeWindow(func):
    i = 0
    Nwindow = Tk()

    #used to grab the values the then entry textvariables, so that for any function I can call them and reuse them
    def get_val(func):
        if func == test1:
            a,b,c,d,e,f = entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()
            test1(a,b,c,d,e,f)
        elif func == test2:
            None
        elif func == test3:
            None
        elif func == test4:
            None
    #generics we can reuse for any task I have created
    entry1=StringVar(Nwindow)
    entry2=StringVar(Nwindow)
    entry3=StringVar(Nwindow)
    entry4=StringVar(Nwindow)
    entry5=StringVar(Nwindow)
    entry6=StringVar(Nwindow)

    #attempting to use generics to make my life easier
    #this will change a lot later on, but for now i will try to get it to work
    if func == test1: #creates a mod file of you to use
        Nwindow.title("Mod Header")
        text1 = 'Name of the hotfix file: '
        text2 = 'The actual mod name: '
        text3 = 'Author(s) name: '
        text4 = 'Discription: '
        text5 = 'Version of this mod: '
        text6 = 'The catagory in which this mods fits to: '
        
        b1text = 'Create Mod Header'
        b1command = lambda: get_val(func)
        i = 1
    elif func == test2: #this will be more fleshed out later, but for now it I am trying to get the interfce to work
        Nwindow.title("Look Through File information")
        Button(Nwindow, text = "Choose file", command = lambda: filechoice)
        #will have new buttons added after the user clicks the file
    elif func == test3:
        None
    elif func == test4:
        None

    #Now these cn be used dynamically, so that I can change them to whatever i need them to be
    # I will have another seperation statement in here so that I can add the amount of things as i need them
    #not the best solution, bit it will have to do
    if i == 1:
        Label(Nwindow, text= text1).grid(row=0)
        Label(Nwindow, text= text2).grid(row=1)
        Label(Nwindow, text= text3).grid(row=2)
        Label(Nwindow, text= text4).grid(row=3)
        Label(Nwindow, text= text5).grid(row=4)
        Label(Nwindow, text= text6).grid(row=5)
        Entry(Nwindow, textvariable = entry1).grid(row = 0, column = 1)
        Entry(Nwindow, textvariable = entry2).grid(row = 1, column = 1)
        Entry(Nwindow, textvariable = entry3).grid(row = 2, column = 1)
        Entry(Nwindow, textvariable = entry4).grid(row = 3, column = 1)
        Entry(Nwindow, textvariable = entry5).grid(row = 4, column = 1)
        Entry(Nwindow, textvariable = entry6).grid(row = 5, column = 1)
        Button(Nwindow, text=b1text, command = b1command ).grid(row = 6)
    
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hot Fix Generator")
    # window.geometry("500x500")
    Button(text="1. Mod Header", font=("Times New Roman", 18), command = lambda: NeWindow(test1))
    Button(text="2. Choose File", font=("Times New Roman", 18), command = lambda: NeWindow(test2))
    Button(text="3. Find All References", font=("Times New Roman", 18), command = lambda: NeWindow(test3))
    Button(text="4. Make Regular Hotfix", font=("Times New Roman", 18), command = lambda: NeWindow(test4))

    #this will pack everything so that I do not have to do it every time
    for c in sorted(window.children):
        window.children[c].pack()
    window.mainloop()