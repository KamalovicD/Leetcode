from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n * n  # Matritsa elementlari soni: 1 dan n^2 gacha
        freq = [0] * (total + 1)  # 1-indeksli massiv: freq[i] - i sonining nechta marta uchrashi

        # Har bir satr va har bir elementni ko‘rib chiqamiz
        for row in grid:
            for num in row:
                freq[num] += 1  # num ni uchrash sonini oshiramiz

        # Repeating son (takroriy) va missing son (yo'q) ni aniqlaymiz.
        repeated = -1
        missing = -1
        for i in range(1, total + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i

        return [repeated, missing]
