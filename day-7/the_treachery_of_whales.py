import sys

from typing import List

def parse_input(filename: str) -> List[List['Point']]:
    with open(filename, 'r') as input:
        return [int(num) for num in input.readline().split(",")]


def calculate_fuel(positions: List[int]) -> int:
    min_fuel = sys.maxsize

    for i, pos in enumerate(positions):
        fuel = 0
        for j in range(i):
            fuel += abs(positions[j] - pos)
        for j in range(i+1, len(positions)):
            fuel += abs(positions[j] - pos)
        min_fuel = min(min_fuel, fuel)

    return min_fuel


if __name__ == '__main__':
    positions = parse_input('input.txt')
    result_one = calculate_fuel(positions)
    print(result_one)
