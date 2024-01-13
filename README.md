# pgn_manager

pgn manager is a library for managing and manipulating pgn files.

## Installation

You can install this library using `pip`:

`pip install pgn_manager`

or

`pip install pgn-manager`

Example of use [_readPGN(path)] and [split_pgn(path)]:

```shell
from pgn_manager import _readPGN
import csv

def main(filename):
    csv_columns = ["eco_code", "percentage_of_use %", "percentage_of_win %", "number_of_use", "number_of_wins"]
    csv_data = []
    games = _readPGN(filename)
    wins = 0
    loses = 0
    draws = 0


from pgn_manager import merge_pgn, split_pgn, writeMatchesIntoCsv

#This function is utilized in the implementation of a graphical interface. It takes as input the path of the PGN file and a destination folder.

def on_button_split():
    text1 = str(text_box_search_file_pgn_split.get(1.0, 'end-1c')) #PGN path
    text2 = str(text_box_path_pgn_split.get(1.0, 'end-1c')) #Destination folder
    if text1 == '' or text2 == '':
        messagebox.showerror('Error', 'Fields cannot be empty.')
        return
    split_pgn(text1, text2)
    messagebox.showinfo('Success!', 'split completed')
