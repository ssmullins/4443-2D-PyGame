import tkinter as tk
import sys
import os
import pprint as pp
import json

fpath = "player_info.json"

if os.path.isfile(fpath):
    f = open(fpath,"r")
    data = f.read()
    f.close()
else:
    print("Error: File doesn't exixt!")

player = json.loads(data)

#pp.pprint(player)
#print(type(player))

# GUI window is a subclass of the basic tkinter Frame object
class playerFrame(tk.Frame):
    def __init__(self, master,fname,lname,rank,email,powerb, availableb):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create text box with Player Info text
        fName = tk.Label(self, text=f"First: {fname}")
        lName = tk.Label(self, text=f"Last: {lname}")
        rank = tk.Label(self,text=f"Rank: {rank}")
        email = tk.Label(self,text=f"Email: {email}")
        pBoost = tk.Label(self,text=f"Power-Boost: {powerb}")
        aBoost = tk.Label(self,text=f"Available-Boost:{availableb}")
        # Place text box into frame
        fName.grid(row=0, column=0)
        lName.grid(row=1, column=0)
        rank.grid(row=2, column=0)
        email.grid(row=3, column=0)
        pBoost.grid(row=4, column=0)
        aBoost.grid(row=5, column=0)

# Spawn window
if __name__ == "__main__":
    # Create main window object
    root = tk.Tk()
    
    for k,v in player.items():
    # Set title of window
        if k == "screen_name":
            SN = ""
            SN = v
            root.title(SN)
    # Instantiate playerFrame object
        if k == "fname":
            FN = ""
            FN = v
        if k == "lname":
            LN = ""
            LN = v
        if k == "rank":
            R = ""
            R = v
        if k == "email":
            E = ""
            E = v
        if k == "power-boost":
            PB = ""
            PB = v
        if k == "available-boost":
            AB = ""
            AB = v
    player_frame = playerFrame(root, FN, LN , R , E, PB, AB)
    # Start GUI
    player_frame.mainloop()