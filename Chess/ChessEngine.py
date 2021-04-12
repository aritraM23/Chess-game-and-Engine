"""This class is respnosible for storing all data of the chess game and analyses moves"""


class GameState():
    def __init__(self):
        #board is an 8*8 2d list, each element consisting of 2 characters with first character specifying color and second character specifying the peice
        #"--" denotes empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
    '''
    takes a move as a parameter and executes it except castling, en pessant and promotion
    '''
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        if len(self.moveLog) != 0:  #if o move then nomove to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    '''
    All moves considering Checks
    '''
    def getValidMoves(self):
        pass

    '''
    All moves without considering Checks
    '''

    def allPossibleMoves(self):
        pass

class Move():

        ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                       "5": 3, "6": 2, "7": 1, "8": 0}
        rowsToRanks = {v: k for k, v in ranksToRows.items()}
        filesToCols = {"a": 0, "b": 1, "c": 3, "d": 4,
                       "e": 5, "f": 6, "g": 7, "h": 8}
        colsToFiles = {v: k for k, v in filesToCols.items()}

        def __init__(self, startSq, endSq, board):
            self.startRow = startSq[0]
            self.startCol = startSq[1]
            self.endRow = endSq[0]
            self.endCol = endSq[1]
            self.pieceMoved = board[self.startRow][self.startCol]
            self.pieceCaptured = board[self.endRow][self.endCol]

        def getChessNotation(self):
            return self.getRankFile(self.startRow, self.startCol ) + self.getRankFile(self.endRow, self.endCol)

        def getRankFile(self, r, c):
            return self.colsToFiles[c] + self.rowsToRanks[r]



