from copy import deepcopy
from typing import List


def parse_input(filename: str) -> tuple(List[int], List[List[List[int]]]):
    with open(filename, 'r') as input:
        nums = [int(num) for num in input.readline().split(",")]
        boards, board = [], [] 
        for line in input.readlines():
            line = line.rstrip('\n')
            if not line:
                boards.append(board)
                board = []
            else:
                row = [int(num) for num in line.split()]
                board.append(row)
        boards.append(board)
    return nums, boards[1:]


class Bingo():

    def __init__(self, nums: List[int], boards: List[List[List[int]]]) -> None:
        """
        :param nums: a set of random numbers
        :param boards: a random set of boards
        """
        self.nums = nums
        self.boards = boards
        self.first_winning_board = None
        self.last_winning_board = None
        self.first_result = None
        self.second_result = None
        
    def mark_number(self, number: int) -> None:
        """
        Currently don't know how to write a docstring for this function...
        """
        for i, board in enumerate(self.boards):
            new_board = [[-1 if num == number else num for num in row] for row in board]
            if self.has_complete_row(new_board) or self.has_complete_col(new_board):
                if not self.first_winning_board:
                    self.first_winning_board = new_board
                    self.first_result = self.calculate_final_score(number, new_board)
                elif len(self.boards) == 1:
                    self.last_winning_board = new_board, number
                    self.second_result = self.calculate_final_score(number, new_board)
                self.boards[i] = []
            else:
                self.boards[i] = new_board
        self.boards = [board for board in self.boards if board]
            

    def has_complete_row(self, board: List[List[int]]) -> bool:
        """ 
        Returns true if any row of the given board contains -1 values only. 
        Otherwise returns false.
        """
        for row in board:
            if row.count(-1) == 5:
                return True
        return False

    def has_complete_col(self, board: List[List[int]]) -> bool:
        """ 
        Returns true if any col of the given board contains -1 values only. 
        Otherwise returns false.
        """
        for i in range(len(board)):
            col = [row[i] for row in board]
            if col.count(-1) == 5:
                return True
        return False

    def calculate_final_score(self, num: int, board: List[List[int]]) -> int:
        """
        Returns the final score of the given board.
        """
        score = 0
        for row in board:
            for number in row:
                if number != -1:
                    score += number
        return num * score

    def play(self) -> int:
        """
        Plays the game by marking every number in 'self.nums' on all boards until the last winning board is found.
        """
        for num in self.nums:
            if not self.boards:
                return
            if not self.last_winning_board:
                self.mark_number(num)


if __name__ == '__main__':
    nums, boards = parse_input("input.txt")
    bingo = Bingo(nums, boards)
    bingo.play()
    print(bingo.first_result, bingo.second_result)
