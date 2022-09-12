import os
from os.path import exists
from tkinter import *
from tkinter import filedialog

app = Tk(screenName= "J Cleaner", baseName="J Cleaner")
global ent_Words, ent_Types, file_Loc    #Remove words

def cleanFiles():
    lab_Clean = Label(app, text="Cleaning filenames...", fg="green")
    lab_Clean.grid(row=9, column=0)

    global ent_Words
    badWords = str(ent_Words.get()).split(", ")     #Convert inputted list to array of bad word strings.
    print(str(badWords))

    global ent_Types
    types = str(ent_Types.get()).split(", ")    #Convert file types to array of string types.

    global file_Loc
    for fileN in os.listdir(str(file_Loc)):                 #For each file in directory,
        for type in types:
            if(type in str(fileN)):                           #If filename contains a permitted file type,
                fileN = fileN.lower().replace("." + type, "")       #Remove file type from filename.
                for word in badWords:                           #For each word in bad-words list,
                    if word in str(fileN).lower():                                      #If filename contrains bad word,
                        newName = fileN.lower().replace(word, "").replace("  ", " ")    #Remove bad word and potential double-space.
                        if(str(newName[len(newName) - 1]) == " "):                      #If last character is space, remove it.
                            newName = newName[0:len(newName) - 1]                       #Reduce length by 1 to remove space.
                        print("Removed word \'" + word + "\' from \'" + fileN + "\' to: \'" + newName + "\'")

                        if(exists(file_Loc + "/" + newName + "." + type)):                  #If filename already exists, count upward till it's unique.
                            i = 1
                            while exists(file_Loc + "/" + newName + " " + str(i) + "." + type):
                                i += 1

                            os.rename(file_Loc + "/" + fileN + "." + type, file_Loc + "/" + newName + " " + str(i) + "." + type)
                        else:
                            os.rename(file_Loc + "/" + fileN + "." + type, file_Loc + "/" + newName + "." + type)

                        fileN = newName

def locateFiles():
    global file_Loc
    file_Loc = filedialog.askdirectory(title="Collection Location")

    lab_Clean = Label(app, text="File Location: " + file_Loc, fg="blue")
    lab_Clean.grid(row=3, column=0)

    lab_TypeDesc = Label(app, text=
    """Enter file types to modify. Seperate by comma.  
    Ex: \'pdf, mp3, jpg, png, docx, xls\'""")
    lab_TypeDesc.grid(row=4, column=0)

    global ent_Types
    ent_Types = Entry(app, width=50)
    ent_Types.grid(row=5, column=0)

    lab_Desc = Label(app, text=
        """Enter words to remove from filenames. Seperate by comma. 
        Ex: \'cache, temp, draft\' (Case-sensitive)""")
    lab_Desc.grid(row=6, column=0)

    global ent_Words
    ent_Words = Entry(app, width=50)
    ent_Words.grid(row=7, column=0)

    but_Clean = Button(app, text="Clean Files", command=cleanFiles)
    but_Clean.grid(row=8, column=0)

#Create label widget..
lab_Title = Label(app, text="J's Filename Cleaner")
lab_Subtitle1 = Label(app, text=
    """J Cleaner is a free application used to easily rename 
    mass sets of filenames for better organization.""")

#Create button widgets.
but_Loc = Button(app, text="File Location", command=locateFiles)

#Grid setup
lab_Title.grid(row=0, column=0)
lab_Subtitle1.grid(row=1, column=0)
but_Loc.grid(row=2, column=0)

app.mainloop()  #Keeps the GUI running.
