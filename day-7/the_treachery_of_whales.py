import sys

from typing import List

def parse_input(filename: str) -> List[int]:
    with open(filename, 'r') as input:
        return [int(num) for num in input.readline().split(",")]


def calculate_fuel_one(positions: List[int]) -> int:
    min_fuel = sys.maxsize

    for i, pos in enumerate(positions):
        fuel = 0
        for j in range(len(positions)):
            fuel += abs(positions[j] - pos)
        min_fuel = min(min_fuel, fuel)

    return min_fuel


def calculate_fuel_two(positions: List[int]) -> int:
    min_fuel = sys.maxsize

    for i, pos in enumerate(positions):
        fuel = 0
        for j in range(len(positions)):
            supplement = abs(positions[j] - pos)
            fuel += (supplement + 1) * supplement // 2
        min_fuel = min(min_fuel, fuel)

    return min_fuel


if __name__ == '__main__':
    positions = parse_input('input.txt')
    result_one = calculate_fuel_one(positions)
    result_two = calculate_fuel_two(positions)
    print(result_one, result_two)
