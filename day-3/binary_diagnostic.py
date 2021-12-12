from typing import List


def open_file(filename: str) -> List[str]:
    f = open(filename, 'r')
    report = [num.replace('\n', '') for num in f]
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
    return gamma_rate*epsilon_rate


if __name__ == '__main__':
    report = open_file('input.txt')
    result = calculate_gamma_and_epsilon_rates(report)
    print(result)
