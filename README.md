# pgn_manager

pgn manager is a library for managing and manipulating pgn files.

## Installation

You can install this library using `pip`:

pip install pgn_manager
or
pip install pgn-manager

Example of use [_readPGN(path)]:

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
