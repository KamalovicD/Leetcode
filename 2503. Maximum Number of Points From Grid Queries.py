from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # Harakatlanish uchun 4 yo'nalish: pastga, yuqoriga, o'ngga, chapga.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Har bir query natijalarini o'z indekslari bilan saqlaymiz, so'ng ularni sort qilamiz.
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [0] * len(queries)

        # visited: Qaysi hujayralar ko'rib chiqilganligini belgilash uchun.
        visited = [[False] * n for _ in range(m)]
        # h: minimal qiymatga ega hujayralarni saqlovchi min-heap (ustunlikli qator).
        h = []

        # Boshlanish nuqtasi: chap yuqori burchak (0,0) har doim ro'yxatga qo'shamiz.
        heapq.heappush(h, (grid[0][0], 0, 0))
        visited[0][0] = True

        # count: hozirgacha topilgan va to'g'ri shartga javob beruvchi hujayralar (ya'ni,
        # queries[i] dan kichik bo'lgan hujayralar) soni.
        count = 0

        # Har bir query uchun:
        for q, idx in sorted_queries:
            # Heapdagi eng kichik qiymatli hujayra qiymati q dan kichik bo'lsa, u holda u hujayrani "erkin"
            # deb hisoblaymiz va uning qo'shni hujayralarini heapga qo'shamiz.
            while h and h[0][0] < q:
                val, i, j = heapq.heappop(h)
                count += 1  # Bu hujayrani birinchi marta ziyorat qilamiz
                # Hujayraning 4 ta qo'shnisini tekshiramiz
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(h, (grid[ni][nj], ni, nj))
            # Joriy query uchun natijani saqlaymiz
            res[idx] = count

        return res
