from collections import defaultdict
from typing import List


points_dict = defaultdict(int)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


def get_input(filename: str) -> List[List['Point']]:
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


def count_overlap_points_in_a_diagonal(p1: 'Point', p2: 'Point') -> None:
    '''
    Algorithm for drawing a diagonal:
    a. The total number of points are `x2 - x1 + 1`
    b. The starting point can be added to the dictionary without any calculation
    c. For remaining points, we need to calculate the x and y coordinates:
        - The `x` coordinates should always start from `x1` and end with `x2`
        - If `y1` > `y2` we continuously decrease the `y` coordinates by 1, starting from `y1`
        Otherwise, we increase the `y` coordinates by 1, starting from `y1`
    '''
    # Add the starting point to the dictionary
    x, y = p1.x, p1.y
    points_dict[(x, y)] += 1

    # Add remaining points to the dictionary
    if p1.y > p2.y:
        for _ in range(p1.x, p2.x):
            x, y = x + 1, y - 1
            points_dict[(x, y)] += 1
    else:
        for _ in range(p1.x, p2.x):
            x, y = x + 1, y + 1
            points_dict[(x, y)] += 1


def count_overlap_points_in_a_column(p1: 'Point', p2: 'Point') -> None:
    for y in range(p1.y, p2.y + 1):
        points_dict[(p1.x, y)] += 1


def count_overlap_points_in_a_row(p1: 'Point', p2: 'Point') -> None:
    for x in range(p1.x, p2.x + 1):
        points_dict[(x, p1.y)] += 1


def count_overlap_points(lines: List[List['Point']]) -> int:

    for p1, p2 in lines:

        # Skip if 2 points have the same x and y coordinates
        if p1 == p2:
            continue

        # Check if the line between the two points is a diagonal (for part 2 only)
        if abs(p1.x - p2.x) == abs(p1.y - p2.y):
           count_overlap_points_in_a_diagonal(p1, p2)

        # Check if the line between the two points is vertical
        if p1.x == p2.x:
            count_overlap_points_in_a_column(p1, p2)

        # Check if the line between the two points is horizontal
        if p1.y == p2.y:
            count_overlap_points_in_a_row(p1, p2)

    return len([1 for freq in points_dict.values() if freq >= 2])


if __name__ == '__main__':
    lines_of_vents = get_input('input.txt')
    result = count_overlap_points(lines_of_vents)
    print(result)