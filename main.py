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

#Title
titleLabel=tk.Label(root, text="This is an app for H3 streamers", font="Righteous", width=28)
#titleLabel.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
titleLabel_window = bg_canvas.create_window(25,20, anchor="nw", window=titleLabel)

#Template
templateLabel=tk.Label(root, text="Template: ", width=15)
#templateLabel.grid(row=0, column=2, padx=10, pady=10)
templateLabel_window = bg_canvas.create_window(300,23, anchor="nw", window=templateLabel)
templateEntry=tk.Entry(root, width=23)
templateEntry_window = bg_canvas.create_window(415,24, anchor="nw", window=templateEntry)
#templateEntry.grid(row=0, column=3, padx=10, pady=10)

#Red player
redLabel=tk.Label(root, text="Red player: ", width=15)
redLabel_window = bg_canvas.create_window(25,50, anchor="nw", window=redLabel)
#redLabel.grid(row=1, column=0, padx=10, pady=10)
redEntry=tk.Entry(root, width=23)
redEntry_window = bg_canvas.create_window(140,51, anchor="nw", window=redEntry)
#redEntry.grid(row=1, column=1, padx=10, pady=10)

redTownLabel=tk.Label(root, text="Picked town: ", width=15, height=2)
#redTownLabel.grid(row=2, column=0, padx=10, pady=10)
redTownLabel_window = bg_canvas.create_window(25,77, anchor="nw", window=redTownLabel)
redTown = tk.StringVar() #defining the value chosen from the dropdown
redTown.set(info.town_list[0])
redTownDrop=tk.OptionMenu(root, redTown, *info.town_list)#.grid(row=2, column=1, padx=10, pady=10)
redTownDrop.config(width=16)
redTownDrop_window = bg_canvas.create_window(140,79, anchor="nw", window=redTownDrop)

redMoneyLabel=tk.Label(root, text="Gold: ", width=15)
redMoneyLabel_window = bg_canvas.create_window(25,119, anchor="nw", window=redMoneyLabel)
#redMoneyLabel.grid(row=3, column=0, padx=10, pady=10)
redMoneyEntry=tk.Entry(root, width=23)
redMoneyEntry_window = bg_canvas.create_window(140,120, anchor="nw", window=redMoneyEntry)
#redMoneyEntry.grid(row=3, column=1, padx=10, pady=10)

#Blue player
blueLabel=tk.Label(root, text="Blue player: ", width=15)
redLabel_window = bg_canvas.create_window(300,50, anchor="nw", window=blueLabel)
#blueLabel.grid(row=1, column=2, padx=10, pady=10)
blueEntry=tk.Entry(root, width=23)
redEntry_window = bg_canvas.create_window(415,51, anchor="nw", window=blueEntry)
#blueEntry.grid(row=1, column=3, padx=10, pady=10)

blueTownLabel=tk.Label(root, text="Picked town: ", width=15, height=2)
blueTownLabel_window = bg_canvas.create_window(300,77, anchor="nw", window=blueTownLabel)
#blueTownLabel.grid(row=2, column=2, padx=10, pady=10)
blueTown = tk.StringVar() #defining the value chosen from the dropdown
blueTown.set(info.town_list[0])
blueTownDrop=tk.OptionMenu(root, blueTown, *info.town_list)#.grid(row=2, column=3, padx=10, pady=10
blueTownDrop.config(width=16)
blueTownDrop_window = bg_canvas.create_window(415,79, anchor="nw", window=blueTownDrop)

blueMoneyLabel=tk.Label(root, text="Gold: ", width=15)
blueMoneyLabel_window = bg_canvas.create_window(300,119, anchor="nw", window=blueMoneyLabel)
#blueMoneyLabel.grid(row=3, column=2, padx=10, pady=10)
blueMoneyEntry=tk.Entry(root, width=23)
redMoneyEntry_window = bg_canvas.create_window(415,120, anchor="nw", window=blueMoneyEntry)
#blueMoneyEntry.grid(row=3, column=3, padx=10, pady=10)

#Submit button
def submit():
    try:
        if int(blueMoneyEntry.get())!=(-1)*int(redMoneyEntry.get()):
            messagebox.showerror("Error!","Make sure that gold values are opposite")
        else:
            submitEntry=tk.Entry(root, width=88)
            submitEntry_window = bg_canvas.create_window(25,205, anchor="nw", window=submitEntry)
            submitEntry.insert(0, templateEntry.get() + " | " + redEntry.get() + " (red, " + redTown.get() + " , " + 
                         redMoneyEntry.get() +")" + " vs " + blueEntry.get() + " (blue, " + blueTown.get() + " , " + 
                         blueMoneyEntry.get() + ")")
            bg_canvas.delete('all')
            bg_canvas.config(width=576)                                                #PLACING TOWNS IMAGES ON THE CANVAS
            bg_canvas.config(height=60)
            bg_canvas.create_image(0,0,image=bg_plot, anchor='nw')
            redTownImage=tk.PhotoImage(file = redTown.get() + ".png")
            redTownImageLabel = tk.Label(root, image=redTownImage, borderwidth=0)
            redTownImageLabel.photo = redTownImage
            redTownImageLabel_window = bg_canvas.create_window(32,30, anchor='nw', window=redTownImageLabel)
            redNameShadow = bg_canvas.create_text(136,15, text=redEntry.get(), font=right20, 
                                            fill="black", width=250, justify=tk.CENTER)
            redName = bg_canvas.create_text(134,13, text=redEntry.get(), font=right20, 
                                            fill="white", width=250, justify=tk.CENTER)
            redGoldShadow = bg_canvas.create_text(157,47, text=redMoneyEntry.get(), font=right26, 
                                            fill="black", width=180, justify=tk.CENTER)
            redGold = bg_canvas.create_text(155,45, text=redMoneyEntry.get(), font=right26, 
                                            fill="white", width=180, justify=tk.CENTER)
            blueNameShadow = bg_canvas.create_text(464,15, text=blueEntry.get(), font=right20, 
                                            fill="black", width=250, justify=tk.CENTER)
            blueName = bg_canvas.create_text(462,13, text=blueEntry.get(), font=right20, 
                                            fill="white", width=250, justify=tk.CENTER)
            blueGoldShadow = bg_canvas.create_text(452,47, text=blueMoneyEntry.get(), font=right26, 
                                            fill="black", width=180, justify=tk.CENTER)
            blueGold = bg_canvas.create_text(450,45, text=blueMoneyEntry.get(), font=right26, 
                                            fill="white", width=180, justify=tk.CENTER)
            templateShadow = bg_canvas.create_text(290,47, text=templateEntry.get(), font=right20, 
                                            fill="black", width=180, justify=tk.CENTER)
            template = bg_canvas.create_text(288,45, text=templateEntry.get(), font=right20, 
                                            fill="white", width=180, justify=tk.CENTER)
            blueTownImage=tk.PhotoImage(file = blueTown.get() + ".png")
            blueTownImageLabel = tk.Label(root, image=blueTownImage, borderwidth=0)
            blueTownImageLabel.photo = blueTownImage
            blueTownImageLabel_window = bg_canvas.create_window(498,30, anchor='nw', window=blueTownImageLabel)
    except ValueError:
        messagebox.showerror("Error!","You've added wrong gold value")

   
    
submitButton=tk.Button(root, text="Submit", command=submit, width=20, height=2)#.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
submitButton_window= bg_canvas.create_window(216,155, anchor="nw", window=submitButton)

root.resizable(False,False)
root.mainloop()