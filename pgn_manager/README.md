# pgn_manager

pgn manager is a library for managing and manipulating pgn files.

## Installation

You can install this library using `pip`:

```shell
pip install pgn_manager

## pgn_manager: example of use
from pgn_manager.pmanager import _readPGN
games = _readPGN(PGN_path

## pmanager functions
_createCSV(path, *columns):
    """
    The function creates a CSV file in the desired path and with the desired column names.

    Args:
        a: PGN path
        b: Names of column

    Returns:
        csv file

    """

_readPGN(pgn_path):
    """
    The function creates a list that contains all the games in the PGN file.

    Args:
        a: PGN path

    Returns:
        A list that contains chess.pgn.game objects.

    """

_createID(game):
    """
    A function that creates a unique ID for a chess game.

    Args:
        a: chess.pgn.game

    Returns:
        ID created with the SHA-256 function

    """


writeMatchesIntoCsv(pgn_file, csv_file):
    """
    A function that writes the games from a PGN file to a CSV file.

    Args:
        a: PGN file
        b: CSV file

    Returns:
        csv file

    """


merge_pgn(pgn_file, pgn_destination):
    """
    The function that merges two PGN files in the second PGN/argument

    Args:
        a: PGN file
        b: PGN file

    Returns:
        pgn_destination

    """


split_pgn(pgn_file, path_destination):
    """
    The function splits the games in the PGN file and creates a PGN for each game in the desired path

    Args:
        a: PGN file
        b: path

    Returns:
        pgn

    """