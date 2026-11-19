class Solution:
    def specialGrid(self, n):
        def solve(n):
            if n == 0:
                return [[0]]
            small = solve(n - 1)
            size = len(small)
            offset = size * size
            grid = [[0] * (2 * size) for _ in range(2 * size)]
            for i in range(size):
                for j in range(size):
                    grid[i][j + size] = small[i][j]
                    grid[i + size][j + size] = small[i][j] + offset
                    grid[i + size][j] = small[i][j] + 2 * offset
                    grid[i][j] = small[i][j] + 3 * offset
            return grid
        return solve(n)