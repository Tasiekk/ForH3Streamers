# -*- coding: utf-8 -*-
"""
Sebastian Uziuk
Program for Heroes 3 streamers that shows which template is played,who plays which castle, 
how many points they have and what color are they
"""
import tkinter as tk
import info

#Creating the app environment
root = tk.Tk()
root.title("For Heroes 3 Streamers")

#App

#Title
titleLabel=tk.Label(root, text="This is an app for H3 streamers", font="Righteous")
titleLabel.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

#Template
templateLabel=tk.Label(root, text="Template: ")
templateLabel.grid(row=0, column=2, padx=10, pady=10)
templateEntry=tk.Entry(root)
templateEntry.grid(row=0, column=3, padx=10, pady=10)

#Red player
redLabel=tk.Label(root, text="Red player: ")
redLabel.grid(row=1, column=0, padx=10, pady=10)
redEntry=tk.Entry(root)
redEntry.grid(row=1, column=1, padx=10, pady=10)

redTownLabel=tk.Label(root, text="Picked town: ")
redTownLabel.grid(row=2, column=0, padx=10, pady=10)
redTown = tk.StringVar() #defining the value chosen from the dropdown
redTown.set(info.town_list[0])
redTownDrop=tk.OptionMenu(root, redTown, *info.town_list).grid(row=2, column=1, padx=10, pady=10)

redMoneyLabel=tk.Label(root, text="Gold: ")
redMoneyLabel.grid(row=3, column=0, padx=10, pady=10)
redMoneyEntry=tk.Entry(root)
redMoneyEntry.grid(row=3, column=1, padx=10, pady=10)

#Blue player
blueLabel=tk.Label(root, text="Blue player: ")
blueLabel.grid(row=1, column=2, padx=10, pady=10)
blueEntry=tk.Entry(root)
blueEntry.grid(row=1, column=3, padx=10, pady=10)

blueTownLabel=tk.Label(root, text="Picked town: ")
blueTownLabel.grid(row=2, column=2, padx=10, pady=10)
blueTown = tk.StringVar() #defining the value chosen from the dropdown
blueTown.set(info.town_list[0])
blueTownDrop=tk.OptionMenu(root, blueTown, *info.town_list).grid(row=2, column=3, padx=10, pady=10)

blueMoneyLabel=tk.Label(root, text="Gold: ")
blueMoneyLabel.grid(row=3, column=2, padx=10, pady=10)
blueMoneyEntry=tk.Entry(root)
blueMoneyEntry.grid(row=3, column=3, padx=10, pady=10)

#Submit button
def submit():
    submitEntry=tk.Entry(root)
    submitEntry.grid(row=10,column=0, padx=100, pady=10, ipadx=150, columnspan=4)
    submitEntry.insert(0, templateEntry.get() + " | " + redEntry.get() + " (red, " + redTown.get() + " , " + 
                         redMoneyEntry.get() +")" + " vs " + blueEntry.get() + " (blue, " + blueTown.get() + " , " + 
                         blueMoneyEntry.get() + ")")
    
    
submitButton=tk.Button(root, text="Submit", command=submit).grid(row=4, column=1, columnspan=2, padx=20, pady=10)


root.mainloop()