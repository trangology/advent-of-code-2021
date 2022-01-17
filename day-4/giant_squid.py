from typing import List


def parse_input(filename: str) -> tuple(List[int], List[List[List[int]]]):
    with open(filename, 'r') as input:
        nums = [int(_) for _ in input.readline().split(",")]
        boards, board = [], [] 
        for line in input.readlines():
            line = line.rstrip('\n')
            if not line:
                boards.append(board)
                board = []
            else:
                row = [int(_) for _ in line.split()]
                board.append(row)
    return nums, boards[1:]


class Bingo():

    def __init__(self, nums: List[int], boards: List[List[List[int]]]) -> None:
        """
        :param nums: a set of random numbers
        :param boards: a random set of boards
        :param winning_board: the board that wins the game
        """
        self.nums = nums
        self.boards = boards
        self.winning_board = None
        
    def mark_number(self, number: int) -> None:
        """
        Sets 'number' in all boards to -1.
        """
        for i, board in enumerate(self.boards):
            board = [[-1 if num == number else num for num in row] for row in board]
            self.boards[i] = board

    def has_complete_row(self, board: List[List[int]]) -> bool:
        """ 
        Returns true if any row of the given board is filled up by -1. 
        Otherwise returns false.
        """
        for row in board:
            if row.count(-1) == 5:
                return True
        return False

    def has_complete_col(self, board: List[List[int]]) -> bool:
        """ 
        Returns true if any col of the given board is filled up by -1. 
        Otherwise returns false.
        """
        for i in range(len(board)):
            col = [row[i] for row in board]
            if col.count(-1) == 5:
                return True
        return False

    def find_winning_board(self) -> bool:
        """ 
        Sets 'self.winning_board' to a board that has either a complete row or col, then returns true.
        Otherwise, returns false.
        """
        for board in self.boards:
            if self.has_complete_row(board) or self.has_complete_col(board):
                self.winning_board = board
                return True
        return False

    def calculate_score(self, num: int) -> int:
        """
        Returns the final score of self.winning_board.
        """
        score = 0
        for row in self.winning_board:
            for number in row:
                if number != -1:
                    score += number
        return num * score

    def play_and_get_result(self) -> int:
        """
        Plays the game by marking every number in 'self.nums' on all boards.
        Stops the game and returns the final score when a winning board is found.
        """
        for num in self.nums:
            self.mark_number(num)
            if self.find_winning_board():
                return self.calculate_score(num)
        return 0


if __name__ == '__main__':
    nums, boards = parse_input("input.txt")
    bingo = Bingo(nums, boards)
    print(bingo.play_and_get_result())
