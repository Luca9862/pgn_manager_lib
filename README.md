# pgn_manager

pgn manager is a library for managing and manipulating pgn files.
Library has two modules: pmanager and pfilter
## Installation

You can install this library using `pip`:

```shell
pip install pgn_manager
or
pip install pgn-manager

## pgn_manager: example of use
from pgn_manager.pmanager import _readPGN
#or
from pgn_manager import _readPGN
from pgn_manager.pfilter import filter_white
games = _readPGN(PGN_path)

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

##pfilter functions
def filter_player(pgn, player):
    """
    Filters a PGN file to only include games that the specified player plays in.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays in.
    """

def filter_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player plays as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White.
    """

def filter_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player plays as Black.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White.
    """

def filter_player_win(pgn, player):
    """
    Filters a PGN file to only include games that the specified player wins.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins.
    """

def filter_player_win_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player wins as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins as White.
    """

def filter_player_win_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player wins as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins as White.
    """

def filter_player_lose(pgn, player):
    """
    Filters a PGN file to only include games that the specified player loses.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses.
    """

def filter_player_lose_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player loses as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses as White.
    """

def filter_player_lose_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player loses as Black.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses as Black.
    """

def filter_for_eco(pgn, eco):
    """
    Filters a PGN file to only include games that use the specified ECO code.

    Args:
        pgn: The filename of the PGN file to filter.
        eco: The ECO code to filter for.

    Returns:
        A list of games that use the specified ECO code.
    """

def filter_for_white_player_eco(pgn, eco, player):
    """
    Filters a PGN file to only include games where the specified player plays as White and the specified ECO code is used.

    Args:
        pgn: The filename of the PGN file to filter.
        eco: The ECO code to filter for.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White and the specified ECO code is used.
    """

def filter_for_white_player_eco_win(pgn, eco, player):
    """
    Filters a list of chess games in PGN format to return only the games in which a specified player (as White)
    has played a game with a specific ECO code (opening code) and won.
    Args:
        pgn: The filename of the PGN file to filter.
        eco: The ECO code to filter for.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White and the specified ECO code is used.
    """