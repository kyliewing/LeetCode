#Your runtime beats 65.06% of python submissions.
#Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):     #Check the rows
            my_dict={}
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in my_dict:
                        return False
                    my_dict[board[i][j]]=board[i][j]  #Usage of HashTable
        
        for i in range(9):    #Check the columns
            my_dict={}
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in my_dict:
                        return False
                    my_dict[board[j][i]]=board[j][i]
        
        for col in range(0,9,3):   #Check the boxes
            for row in range(0,9,3): #Notice the usage of range
                my_dict={}
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j].isdigit():
                            if board[i][j] in my_dict:
                                return False
                            my_dict[board[i][j]]=board[i][j]
        return True
        
            
                
                    
        
        