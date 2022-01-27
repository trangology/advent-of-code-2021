from typing import List


def open_file(filename: str) -> List[int]:
    with open(filename, 'r') as input:
        commands = []
        for line in input:
            command, unit = line.split(' ')
            commands.append((command, int(unit)))
        return commands


def calculate_part_one(commands: List[int]) -> int:
    horizontal_position = 0
    depth = 0
    for option, unit in commands:
        match option:
            case 'forward':
                horizontal_position += unit
            case 'up':
                depth -= unit
            case 'down':
                depth += unit
    return horizontal_position*depth


def calculate_part_two(commands: List[int]) -> int:
    aim = 0
    horizontal_position = 0
    depth = 0
    for option, unit in commands:
        match option:
            case 'forward':
                horizontal_position += unit
                depth += aim * unit 
            case 'up':
                aim -= unit
            case 'down':
                aim += unit
    return horizontal_position * depth


if __name__ == '__main__':
    commands = open_file('input.txt')
    result_one = calculate_part_one(commands)
    result_two = calculate_part_two(commands)
    print(result_one, result_two)
