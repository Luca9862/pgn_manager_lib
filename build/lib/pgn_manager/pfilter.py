# Copyright (c) 2023, Luca Canali
#
#
# Author: [Luca Canali]

from pgn_manager.pmanager import _readPGN


#1--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player(pgn, player):
    """
    Filters a PGN file to only include games that the specified player plays in.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays in.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') or player in game.headers.get('Black'):
            games_filtered.append(game)
    return games_filtered

def filter_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player plays as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White'):
            games_filtered.append(game)
    return games_filtered

def filter_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player plays as Black.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black'):
            games_filtered.append(game)
    return games_filtered
#2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player_win(pgn, player):
    """
    Filters a PGN file to only include games that the specified player wins.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
            continue
        if player in game.headers.get('Black') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered

def filter_player_win_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player wins as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

def filter_player_win_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player wins as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player wins as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered
#3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player_lose(pgn, player):
    """
    Filters a PGN file to only include games that the specified player loses.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
            continue
        if player in game.headers.get('Black') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

def filter_player_lose_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player loses as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered

def filter_player_lose_black(pgn, player):
    """
    Filters a PGN file to only include games where the specified player loses as Black.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player loses as Black.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered
#4--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TODO:function review necessity (don't use)
'''
def filter_player_draws(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if (player in game.headers.get('White') or player in game.headers.get('Black')) and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered

def filter_player_draw_white(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered

def filter_player_draw_black(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered
'''
#5--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_for_eco(pgn, eco):
    """
    Filters a PGN file to only include games that use the specified ECO code.

    Args:
        pgn: The filename of the PGN file to filter.
        eco: The ECO code to filter for.

    Returns:
        A list of games that use the specified ECO code.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if eco == game.headers.get('ECO'):
            games_filtered.append(game)
    return games_filtered

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
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and eco == game.headers.get('ECO'):
            games_filtered.append(game)
    return games_filtered

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
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and eco == game.headers.get('ECO') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

#6--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_time_control(pgn, time): 
    """Filters a list of PGN games based on the specified time control.

    Args:
        pgn: A string or file containing the PGN games to be filtered.
        time: The time control to use to filter the games.

    Returns:
        A list of PGN games that match the specified time control.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if time == game.headers.get('Time'):
            games_filtered.append(game)
    return games_filtered