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
 