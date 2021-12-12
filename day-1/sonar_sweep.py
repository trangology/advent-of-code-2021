from typing import List


def open_file(filename: str) -> List[int]:
    f = open(filename, 'r')
    input = [_ for _ in f]
    return input


def solve(measurements: List[int]) -> int:
    result = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            result += 1
    return result


if __name__ == '__main__':
    measurements = open_file('input.txt')
    result = solve(measurements)
    print(result)
