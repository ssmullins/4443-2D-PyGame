## Simple Second Program
### Samuel Mullins
### Description:
### This small Tkinter program simply creates a very small Tkinter gui window that is populated by data from a json file passed in from the command line. The window is populated with text from the json file which in this case is player info. 
### Files:
|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [main.py](https://github.com/ssmullins/4443-2D-PyGame-Mullins/blob/master/Assignments/A04/main.py)        | Main file that launches the gui window             |
|   2   | [player_info.json](https://github.com/ssmullins/4443-2D-PyGame-Mullins/blob/master/Assignments/A04/player_info.json)
### Instructions:
I coded my program in Visual Code and ran it from the Git Bash shell.
You must make sure you are in the correct directory where your program is stored.
To run the program type the command 'python main.py {json file name here}' in your shell.
The only parameter to change for this program would be the file name you pass into it from the command line.
The data in the json file can be changed but the program does look for the keys {fname, lname, rank, screen_name, email, power-boost, available-boost} so those should not change.
### Example Command:
- 'python main.py player_info.json'
