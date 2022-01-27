from collections import defaultdict
from copy import copy
from typing import List


def open_file(filename: str) -> List[str]:
    with open(filename, 'r') as input:
        report = [num.replace('\n', '') for num in input]
        return report


def calculate_gamma_and_epsilon_rates(report: List[str]) -> int:
    gamma_rate, epsilon_rate = '', ''
    num_length = len(report[0])

    for i in range(num_length):
        number_of_zeros = 0
        number_of_ones = 0
        for num in report:
            match num[i]:
                case '0':
                    number_of_zeros += 1
                case '1':
                    number_of_ones += 1
        if number_of_ones > number_of_zeros:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def calculate_oxygen_generator_rate(report: List[str]) -> int:
    '''
    Steps:
    1. Loop through positions of all numbers in the report, starting at index 0
    2. For each position:
        a. Initialize a new dictionary that has only 2 keys which are 0 and 1, 
        associated with 2 lists of numbers that start with 0 or 1
        b. Compare the length of 2 lists to get a new report of numbers that will be processed next
        c. If the new report has only 1 number, stop the loop by returning this number in decimal 
    '''

    num_length = len(report[0])
    new_report = copy(report)

    for i in range(num_length):
        counter = defaultdict(list)
        for num in new_report:
            if num[i] == '0':
                counter[0].append(num)
            else:
                counter[1].append(num)
        if len(counter[0]) > len(counter[1]):
            new_report = copy(counter[0])
        else:
            new_report = copy(counter[1])
        if len(new_report) == 1:
            return int(new_report[0], 2)


def calculate_CO2_scrubber_rate(report: List[str]) -> int:
    '''
    Follows the same steps as the `calculate_oxygen_generator_rate` function has.
    However, step 2.b should follow the requirement of how to determine the CO2 scrubber rate.
    '''

    num_length = len(report[0])
    new_report = copy(report)

    for i in range(num_length):
        counter = defaultdict(list)
        for num in new_report:
            if num[i] == '0':
                counter[0].append(num)
            else:
                counter[1].append(num)
        if len(counter[0]) <= len(counter[1]):
            new_report = copy(counter[0])
        else:
            new_report = copy(counter[1])
        if len(new_report) == 1:
            return int(new_report[0], 2)


if __name__ == '__main__':
    report = open_file('input.txt')
    result_one = calculate_gamma_and_epsilon_rates(report)
    result_two = calculate_oxygen_generator_rate(report) * calculate_CO2_scrubber_rate(report)
    print(result_one, result_two)
