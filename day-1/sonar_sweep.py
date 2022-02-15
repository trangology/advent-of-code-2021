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


def count_sliding_window_measurements(measurements: List[int]) -> int:
    result = 0
    for i in range(len(measurements)-3):
        sum_one = measurements[i] + measurements[i+1] + measurements[i+2]
        sum_two = measurements[i+1] + measurements[i+2] + measurements[i+3]
        if sum_two > sum_one:
            result += 1
    return result


if __name__ == '__main__':
    measurements = open_file('input.txt')
    result_one = count_measurements(measurements)
    result_two = count_sliding_window_measurements(measurements)
    print(result_one, result_two)
