class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {} #row as a tuple -> freq
        cols = {} #col as a tuple -> freq

        for row in grid:
            rows[tuple(row)] = rows.get(tuple(row), 0) + 1

        for col in range(len(grid)):
            col_list = []
            for row in range(len(grid)):
                col_list.append(grid[row][col])
            cols[tuple(col_list)] = cols.get(tuple(col_list), 0) + 1

        intersection = rows.keys() & cols.keys()
        pairs = 0
        for pair in intersection:
            pairs += rows[pair] * cols[pair]

        return pairs
