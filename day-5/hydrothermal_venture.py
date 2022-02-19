from collections import defaultdict
from typing import List


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def get_input(filename: str) -> List[List[tuple(int)]]:
    with open(filename, 'r') as input:
        lines_of_vents = []
        for line in input:
            p1, p2 = line.split(' -> ')
            x1, y1 = map(int, p1.split(','))
            x2, y2 = map(int, p2.split(','))
            lines_of_vents.append([Point(x1, y1), Point(x2, y2)])
        return lines_of_vents


def count_overlap_points(lines: List[List[tuple(int)]]) -> int:
    point_dict = defaultdict(int)

    for p1, p2 in lines:
        if p1 == p2:
            continue
        if p1.x == p2.x:
            lower, upper = min(p1.y, p2.y), max(p1.y, p2.y)
            for y in range(lower, upper + 1):
                point_dict[p1.x, y] += 1
        if p1.y == p2.y:
            lower, upper = min(p1.x, p2.x), max(p1.x, p2.x)
            for x in range(lower, upper + 1):
                point_dict[x, p1.y] += 1

    return len([1 for freq in point_dict.values() if freq >= 2])


if __name__ == '__main__':
    lines_of_vents = get_input('input.txt')
    result_one = count_overlap_points(lines_of_vents)
    print(result_one)
