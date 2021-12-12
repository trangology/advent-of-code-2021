from typing import List


def open_file(filename: str) -> List[int]:
    f = open(filename, 'r')
    commands = []
    for line in f:
        command, unit = line.split(' ')
        commands.append((command, int(unit)))
    return commands


def calculate(commands: List[int]) -> int:
    horizontal_position = 0
    depth = 0
    for command, unit in commands:
        match command:
            case 'forward':
                horizontal_position += unit
            case 'up':
                depth -= unit
            case 'down':
                depth += unit
    return horizontal_position*depth


if __name__ == '__main__':
    commands = open_file('input.txt')
    result = calculate(commands)
    print(result)
