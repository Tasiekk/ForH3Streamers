# -*- coding: utf-8 -*-
"""
Sebastian Uziuk
Program for Heroes 3 streamers that shows which template is played,who plays which castle, 
how many points they have and what color are they
"""
import tkinter as tk


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
redTownEntry=tk.Entry(root)
redTownEntry.grid(row=2, column=1, padx=10, pady=10)

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
blueTownEntry=tk.Entry(root)
blueTownEntry.grid(row=2, column=3, padx=10, pady=10)

blueMoneyLabel=tk.Label(root, text="Gold: ")
blueMoneyLabel.grid(row=3, column=2, padx=10, pady=10)
blueMoneyEntry=tk.Entry(root)
blueMoneyEntry.grid(row=3, column=3, padx=10, pady=10)

#Submit button
def submit():
    submitLabel=tk.Label(root, text = templateEntry.get() + " | " + redEntry.get() + " (red, " + redTownEntry.get() + " , " + 
                         redMoneyEntry.get() +") " + " vs " + blueEntry.get() + " (blue, " + blueTownEntry.get() + " , " + 
                         blueMoneyEntry.get() + ")") 
    submitLabel.grid(row=10,column=1, padx=10, pady=10)
    
submitButton=tk.Button(root, text="Done!", command=submit).grid(row=4, column=1, columnspan=2, padx=20, pady=10)


root.mainloop()