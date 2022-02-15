from typing import List


def open_file(filename: str) -> List[int]:
    with open(filename, 'r') as input:
        measurements = [int(num) for num in input]
        return measurements


def count_measurements(measurements: List[int]) -> int:
    result = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            result += 1
    return result


if __name__ == '__main__':
    measurements = open_file('input.txt')
    result = count_measurements(measurements)
    print(result)
