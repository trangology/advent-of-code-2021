from collections import defaultdict
from typing import List


DAYS = 80


def parse_input(filename: str) -> List[List['Point']]:
    with open(filename, 'r') as input:
        return [int(num) for num in input.readline().split(",")]


def count_lanternfishes(states: List[int]) -> int:
    day = 1
    number_of_zeros = 0
    new_states = states

    while day <= DAYS:

        new_states = list(map(lambda state: state - 1 if state > 0 else 6, new_states))

        if number_of_zeros > 0:
            for _ in range(number_of_zeros):
                new_states.append(8)

        number_of_zeros = new_states.count(0)
        day += 1

    return len(new_states)


def count_lanternfishes_optimally(states: List[int]) -> int:
    pass


if __name__ == '__main__':
    initial_states = parse_input('input.txt')
    result_one = count_lanternfishes(initial_states)
    result_two = count_lanternfishes_optimally(initial_states)
    print(result_one, result_two)
