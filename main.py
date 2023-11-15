# -*- coding: utf-8 -*-
"""
Sebastian Uziuk
Program for Heroes 3 streamers that shows which template is played,who plays which castle, 
how many points they have and what color are they
"""
import tkinter as tk
import info
from tkinter import messagebox
from tkinter import font
from tkinter import *


#Creating the GUI environment
root = tk.Tk()
root.title("For Heroes 3 Streamers")
root.iconbitmap('h3forstreamers.ico')

#Font settings
right26=font.Font(family="Righteous", size=23, slant="italic")
right20=font.Font(family="Righteous", size=16)

#Background image
bg = tk.PhotoImage(file="h3background.png")
bg_plot = tk.PhotoImage(file="h3background_plot.png")
bg_canvas = tk.Canvas(root, width=576, height=240)
bg_canvas.grid(row=0, column=0, rowspan=6, columnspan=4)
bg_canvas.create_image(0,0,image=bg, anchor='nw')


def newGame():
    bg_canvas.delete('all')
    bg_canvas.config(width=576)                                                #PLACING TOWNS IMAGES ON THE CANVAS
    bg_canvas.config(height=240)
    bg_canvas.create_image(0,0,image=bg, anchor='nw')
    #Title
    titleLabel= bg_canvas.create_text(150,30, text="Complete the game information:", font=font.Font(family="Righteous", size=10), 
                                    fill="white", width=350, justify=tk.CENTER)
    #titleLabel=tk.Label(root, text="Complete the game information:", font="Righteous", width=24)
    #titleLabel.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    #titleLabel_window = bg_canvas.create_window(25,20, anchor="nw", window=titleLabel)
    
    #Template
    templateLabel=tk.Label(root, text="Template: ", width=15)
    #templateLabel.grid(row=0, column=2, padx=10, pady=10)
    templateLabel_window = bg_canvas.create_window(300,23, anchor="nw", window=templateLabel)
    templateEntry=tk.Entry(root, width=23)
    try:
        templateEntry.insert(0, PlayerInfo[6])
    except Exception:
        pass
    templateEntry_window = bg_canvas.create_window(415,24, anchor="nw", window=templateEntry)
    #templateEntry.grid(row=0, column=3, padx=10, pady=10)
    
    #Red player
    redLabel=tk.Label(root, text="Red player: ", width=15)
    redLabel_window = bg_canvas.create_window(25,50, anchor="nw", window=redLabel)
    #redLabel.grid(row=1, column=0, padx=10, pady=10)
    redEntry=tk.Entry(root, width=23)
    try:
        redEntry.insert(0, PlayerInfo[0])
    except Exception:
        pass
    redEntry_window = bg_canvas.create_window(140,51, anchor="nw", window=redEntry)
    #redEntry.grid(row=1, column=1, padx=10, pady=10)
    redTownLabel=tk.Label(root, text="Picked town: ", width=15, height=2)
    #redTownLabel.grid(row=2, column=0, padx=10, pady=10)
    redTownLabel_window = bg_canvas.create_window(25,77, anchor="nw", window=redTownLabel)
    redTown = tk.StringVar() #defining the value chosen from the dropdown
    try:
        redTown.set(PlayerInfo[2])
    except Exception:
        redTown.set(info.town_list[0])
    redTownDrop=tk.OptionMenu(root, redTown, *info.town_list)#.grid(row=2, column=1, padx=10, pady=10)
    redTownDrop.config(width=16)
    redTownDrop_window = bg_canvas.create_window(140,79, anchor="nw", window=redTownDrop)
    
    redMoneyLabel=tk.Label(root, text="Gold: ", width=15)
    redMoneyLabel_window = bg_canvas.create_window(25,119, anchor="nw", window=redMoneyLabel)
    #redMoneyLabel.grid(row=3, column=0, padx=10, pady=10)
    redMoneyEntry=tk.Entry(root, width=23)
    try:
        redMoneyEntry.insert(0, PlayerInfo[1])
    except Exception:
        pass
    redMoneyEntry_window = bg_canvas.create_window(140,120, anchor="nw", window=redMoneyEntry)
    #redMoneyEntry.grid(row=3, column=1, padx=10, pady=10)
    
    #Blue player
    blueLabel=tk.Label(root, text="Blue player: ", width=15)
    redLabel_window = bg_canvas.create_window(300,50, anchor="nw", window=blueLabel)
    #blueLabel.grid(row=1, column=2, padx=10, pady=10)
    blueEntry=tk.Entry(root, width=23)
    try:
        blueEntry.insert(0, PlayerInfo[3])
    except Exception:
        pass
    redEntry_window = bg_canvas.create_window(415,51, anchor="nw", window=blueEntry)
    #blueEntry.grid(row=1, column=3, padx=10, pady=10)
    
    blueTownLabel=tk.Label(root, text="Picked town: ", width=15, height=2)
    blueTownLabel_window = bg_canvas.create_window(300,77, anchor="nw", window=blueTownLabel)
    #blueTownLabel.grid(row=2, column=2, padx=10, pady=10)
    blueTown = tk.StringVar() #defining the value chosen from the dropdown
    try:
        blueTown.set(PlayerInfo[5])
    except Exception:
        blueTown.set(info.town_list[0])
    blueTownDrop=tk.OptionMenu(root, blueTown, *info.town_list)#.grid(row=2, column=3, padx=10, pady=10
    blueTownDrop.config(width=16)
    blueTownDrop_window = bg_canvas.create_window(415,79, anchor="nw", window=blueTownDrop)
    
    blueMoneyLabel=tk.Label(root, text="Gold: ", width=15)
    blueMoneyLabel_window = bg_canvas.create_window(300,119, anchor="nw", window=blueMoneyLabel)
    #blueMoneyLabel.grid(row=3, column=2, padx=10, pady=10)
    blueMoneyEntry=tk.Entry(root, width=23)
    try:
        blueMoneyEntry.insert(0, PlayerInfo[4])
    except Exception:
        pass
    redMoneyEntry_window = bg_canvas.create_window(415,120, anchor="nw", window=blueMoneyEntry)
    #blueMoneyEntry.grid(row=3, column=3, padx=10, pady=10)
    
    #Responsible size of text of nick name players
    def size_text(nickName):
        if int(250/len(nickName)) >= 16:
            return 16
        else:
            return int(250/len(nickName))
    
    #Submit button
    def submit():
        try:
            if len(blueMoneyEntry.get())!=0 and len(redMoneyEntry.get())!=0:
                if int(blueMoneyEntry.get())!=(-1)*int(redMoneyEntry.get()):
                    messagebox.showerror("Error!","Make sure that gold values are opposite")
            elif len(blueMoneyEntry.get())==0 and len(redMoneyEntry.get())==0:
                messagebox.showerror("Error!","You've not added gold value")
            else:
                submitEntry=tk.Entry(root, width=88)
                submitEntry_window = bg_canvas.create_window(25,205, anchor="nw", window=submitEntry)
               # submitEntry.insert(0, templateEntry.get() + " | " + redEntry.get() + " (red, " + redTown.get() + " , " + 
               #redMoneyEntry.get() +")" + " vs " + blueEntry.get() + " (blue, " + blueTown.get() + " , " + 
                #             blueMoneyEntry.get() + ")")
                bg_canvas.delete('all')
                bg_canvas.config(width=576)                                                #PLACING TOWNS IMAGES ON THE CANVAS
                bg_canvas.config(height=60)
                bg_canvas.create_image(0,0,image=bg_plot, anchor='nw')
                redTownImage=tk.PhotoImage(file = redTown.get() + ".png")
                redTownImageLabel = tk.Label(root, image=redTownImage, borderwidth=0)
                redTownImageLabel.photo = redTownImage
                redTownImageLabel_window = bg_canvas.create_window(32,30, anchor='nw', window=redTownImageLabel)
                redNameShadow = bg_canvas.create_text(136,15, text=redEntry.get(), font=font.Font(family="Righteous", size=size_text(redEntry.get())), 
                                                fill="black", width=250, justify=tk.CENTER)
                redName = bg_canvas.create_text(134,13, text=redEntry.get(), font=font.Font(family="Righteous", size=size_text(redEntry.get())), 
                                                fill="white", width=250, justify=tk.CENTER)
                redGoldShadow = bg_canvas.create_text(157,47, text=redMoneyEntry.get(), font=right26, 
                                                fill="black", width=180, justify=tk.CENTER)
                if len(redMoneyEntry.get())==0:
                    redGold_text=str(int(blueMoneyEntry.get())*(-1))
                else:
                    redGold_text=redMoneyEntry.get()
                redGold = bg_canvas.create_text(155,45, text=redGold_text, font=right26, 
                                                fill="white", width=180, justify=tk.CENTER)
                blueNameShadow = bg_canvas.create_text(464,15, text=blueEntry.get(), font=font.Font(family="Righteous", size=size_text(blueEntry.get())), 
                                                fill="black", width=250, justify=tk.CENTER)
                blueName = bg_canvas.create_text(462,13, text=blueEntry.get(), font=font.Font(family="Righteous", size=size_text(blueEntry.get())), 
                                                fill="white", width=250, justify=tk.CENTER)
                blueGoldShadow = bg_canvas.create_text(452,47, text=blueMoneyEntry.get(), font=right26, 
                                                fill="black", width=180, justify=tk.CENTER)
                if len(blueMoneyEntry.get())==0:
                    blueGold_text=str(int(redMoneyEntry.get())*(-1))
                else:
                    blueGold_text=blueMoneyEntry.get()
                blueGold = bg_canvas.create_text(450,45, text=blueGold_text, font=right26, 
                                                fill="white", width=180, justify=tk.CENTER)
                templateShadow = bg_canvas.create_text(290,47, text=templateEntry.get(), font=right20, 
                                                fill="black", width=180, justify=tk.CENTER)
                template = bg_canvas.create_text(288,45, text=templateEntry.get(), font=right20, 
                                                fill="white", width=180, justify=tk.CENTER)
                blueTownImage=tk.PhotoImage(file = blueTown.get() + ".png")
                blueTownImageLabel = tk.Label(root, image=blueTownImage, borderwidth=0)
                blueTownImageLabel.photo = blueTownImage
                blueTownImageLabel_window = bg_canvas.create_window(498,30, anchor='nw', window=blueTownImageLabel)
                #This variable information about Player for default value to change if we choose button "Edit"
                global PlayerInfo
                PlayerInfo=["","","","","","",""]
                PlayerInfo[0]=redEntry.get()
                PlayerInfo[1]=redMoneyEntry.get()
                PlayerInfo[2]=redTown.get()
                PlayerInfo[3]=blueEntry.get()
                PlayerInfo[4]=blueMoneyEntry.get()
                PlayerInfo[5]=blueTown.get()
                PlayerInfo[6]=templateEntry.get()
                #Button to change information abuot game:
                global photo
                photo=tk.PhotoImage(file="h3background_button_edit.png")
                #bg_canvas.create_image(0,0, anchor="nw", image=photo)
                editButton=tk.Button(root, text="reset", image= photo, command=newGame, borderwidth=0)
                editButton_window=bg_canvas.create_window(270,0, anchor="nw", window=editButton)
                
        except ValueError:
            messagebox.showerror("Error!","You've added wrong gold value")
        
       
        
    submitButton=tk.Button(root, text="Submit", command=submit,width=20, height=2)#.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
    submitButton_window= bg_canvas.create_window(216,155, anchor="nw", window=submitButton)
    
    titleLabel_PS= bg_canvas.create_text(250,220, text="P.S.: If you want change informations about plyers after submit, you must click in 'VS'", font=font.Font(family="Righteous", size=10), 
                                    fill="white", width=450, justify=tk.CENTER)
    
    root.resizable(False,False)
    root.mainloop()
    
#Title
titleLabel= bg_canvas.create_text(300,100, text="Hello Player. \n Welcome in app for Heroes 3's streamers!", font=font.Font(family="Righteous", size=25), 
                                fill="white", width=350, justify=tk.CENTER)

NewGameButton=tk.Button(root, text="New Game", command=newGame, width=20, height=2)
NewGameButton_window=bg_canvas.create_window(216,170, anchor="nw", window=NewGameButton)    
  
root.resizable(False,False)
root.mainloop()