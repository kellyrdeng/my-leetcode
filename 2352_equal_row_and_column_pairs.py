import numpy

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {} #row as a tuple -> freq
        cols = {} #col as a tuple -> freq

        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1

        for col in numpy.array(grid).T:
            cols[tuple(col)] = cols.get(tuple(col), 0) + 1

        intersection = rows.keys() & cols.keys()
        pairs = 0
        for pair in intersection:
            pairs += rows[pair] * cols[pair] #different ways to make pairs from the rows/cols

        return pairs
