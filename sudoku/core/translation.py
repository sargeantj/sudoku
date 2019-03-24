"""Translate the list of numbers into a game."""


def numbers_to_game(numbers):
    """Translate the numbers into the game."""
    game = []
    row = []
    for index, value in enumerate(numbers):
        if ((index % 9) == 0) & (index != 0):
            game.append(row)
            row = []
        row.append(value)
    game.append(row)
    return game
