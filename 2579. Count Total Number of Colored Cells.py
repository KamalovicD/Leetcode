class Solution:
    def coloredCells(self, n: int) -> int:
        # Ranglanadigan umumiy hujayralar soni hisoblanadi
        return 1 + 2 * n * (n - 1)
