class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on.
    """
    
    def __init__(self):
        # Initialize an empty 3x3 board represented as a list of 9 '*'
        self.board = ['*' for _ in range(9)]
    
    def make_move(self, player: str, position: int) -> bool:
        """Attempts to place a player's move at a specified position.
        
        Args:
            player - a string, either 'X' or 'O', representing the player
            position - an integer between 0 and 8 representing the position on the board
        
        Returns:
            True if the move was successful, False otherwise (e.g., if the position is already taken).
        """
        if 0 <= position < 9 and self.board[position] == '*':
            self.board[position] = player
            return True
        return False
    
    def has_won(self, player: str) -> bool:
        """Checks if the specified player has won.
        
        Args:
            player - a string, either 'X' or 'O', representing the player
            
        Returns:
            True if the player has won, False otherwise.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        return any(all(self.board[pos] == player for pos in combo) for combo in winning_combinations)
    
    def game_over(self) -> bool:
        """Checks if the game is over (either a player has won or the board is full).
        
        Returns:
            True if the game is over, False otherwise.
        """
        return self.has_won('X') or self.has_won('O') or all(spot != '*' for spot in self.board)
    
    def clear(self) -> None:
        """Clears the board for a new game."""
        self.board = ['*' for _ in range(9)]
    
    def __str__(self):
        """Returns a string representation of the board."""
        return "\n".join(
            " ".join(self.board[i:i+3]) for i in range(0, 9, 3)
        )
 
def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""
    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise
        Args:
            maybe_int - string to check if it's an int
        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False
    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0
    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")
        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )
        if brd.make_move(players[turn], int(move)):
            turn = not turn
    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)
    assert brd.game_over() == False
    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)
    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True
    brd.clear()
    assert brd.game_over() == False
    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)
    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True
    print("All tests passed!")
    # uncomment to play!
    # play_tic_tac_toe()