from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        row = len(board)  # Number of rows
        col = len(board[0])  # Number of columns
        
        # A set to track the cells visited in the current path
        path = set()

        # Define the recursive Depth-First Search (DFS) function
        def dfs(r, c, i):
            # Base case: If the entire word is matched, return True
            if i == len(word):
                return True
            
            # Check for invalid moves:
            # 1. Out of bounds (r or c is outside the board)
            # 2. Current cell does not match the corresponding character in the word
            # 3. Current cell is already visited in the current path
            if (r < 0 or c < 0 or r >= row or c >= col or 
                board[r][c] != word[i] or (r, c) in path):
                return False
            
            # Add the current cell to the path (mark it as visited)
            path.add((r, c))
            
            # Recursively search in all four directions
            # Must wrap the expression in parentheses to avoid syntax errors
            res = (dfs(r + 1, c, i + 1) or  # Down
                   dfs(r - 1, c, i + 1) or  # Up
                   dfs(r, c - 1, i + 1) or  # Left
                   dfs(r, c + 1, i + 1))    # Right
            
            # Backtrack: Remove the current cell from the path
            # This ensures other paths can reuse this cell
            path.remove((r, c))
            
            # Return whether any direction found a valid path
            return res
        
        # Iterate through every cell in the board as a starting point
        for r in range(row):  # Iterate over all rows
            for c in range(col):  # Iterate over all columns
                # Start DFS from the current cell
                if dfs(r, c, 0):  # If DFS finds a valid path for the word, return True
                    return True

        # If no valid path is found after exploring all cells, return False
        return False
