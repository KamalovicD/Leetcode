from heapq import heappop, heappush
from collections import defaultdict
import sys

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # 1. Graflarni saqlash uchun qo'shni ro‘yxatni yaratamiz
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # 2. Dijkstra algoritmi uchun zarur bo'lgan o'zgaruvchilar
        min_time = [sys.maxsize] * n  # Har bir cho'qqiga eng qisqa yo'lni saqlash
        min_time[0] = 0  # Boshlang‘ich nuqtadan o‘ziga borish masofasi 0
        ways = [0] * n  # Har bir cho'qqiga borish yo‘llari soni
        ways[0] = 1  # 0-cho'qqiga borishning bitta yo'li bor (o'zidan o'ziga)

        # 3. Prioritet navbat (Min-Heap)
        heap = [(0, 0)]  # (hozircha eng qisqa vaqt, cho'qqi)

        while heap:
            curr_time, node = heappop(heap)  # Eng yaqin cho'qqini olish

            # Agar allaqachon eng qisqa yo'lni hisoblab bo'lsak, davom etamiz
            if curr_time > min_time[node]:
                continue

            # 4. Qo'shni cho'qqilarni tekshiramiz
            for neighbor, travel_time in graph[node]:
                new_time = curr_time + travel_time

                if new_time < min_time[neighbor]:  # Yangi eng qisqa yo'l topildi
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Shu yo‘ldan nechta variant borligini saqlaymiz
                    heappush(heap, (new_time, neighbor))

                elif new_time == min_time[neighbor]:  # Agar xuddi shu masofada boshqa yo‘l bo‘lsa
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
