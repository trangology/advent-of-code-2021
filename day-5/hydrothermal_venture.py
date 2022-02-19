from collections import defaultdict
from typing import List


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y


def get_input(filename: str) -> List[List[tuple(int)]]:
    with open(filename, 'r') as input:
        lines_of_vents = []

        for line in input:
            p1, p2 = line.split(' -> ')
            x1, y1 = map(int, p1.split(','))
            x2, y2 = map(int, p2.split(','))

            # prioritize the point with smaller x-coordinate first
            (x1, y1), (x2, y2) = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))

            lines_of_vents.append([Point(x1, y1), Point(x2, y2)])

        return lines_of_vents


def count_overlap_points(lines: List[List[tuple(int)]]) -> int:
    points_dict = defaultdict(int)

    for p1, p2 in lines:

        # skip if 2 points have the same x and y coordinates
        if p1 == p2:
            continue

        # check if the line between the two points is at a 45 degree angle to the horizontal
        if abs(p1.x - p2.x) == abs(p1.y - p2.y):
            x, y = p1.x, p1.y
            points_dict[x, y] += 1
            if p1.y > p2.y:
                for _ in range(p1.x, p2.x + 1):
                    x, y = x + 1, y - 1
                    points_dict[x, y] += 1
            else:
                for _ in range(p1.x, p2.x + 1):
                    x, y = x + 1, y + 1
                    points_dict[x, y] += 1

        # check if the line between the two points is vertical
        if p1.x == p2.x:
            for y in range(p1.y, p2.y + 1):
                points_dict[p1.x, y] += 1

        # check if the line between the two points is horizontal
        if p1.y == p2.y:
            for x in range(p1.x, p2.x + 1):
                points_dict[x, p1.y] += 1

    return len([1 for freq in points_dict.values() if freq >= 2])


if __name__ == '__main__':
    lines_of_vents = get_input('input.txt')
    result_two = count_overlap_points(lines_of_vents)
    print(result_two)
