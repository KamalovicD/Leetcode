from typing import List
from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Graﬁk uchun qo‘shimcha ro‘yxat (adjacency list) yaratamiz.
        #    Bu yerda, har bir tugun uchun uning qo‘shni tugunlari ro‘yhatini tuzamiz.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 2. Har bir tugunni tekshirish uchun visited ro‘yhatini yaratamiz.
        visited = [False] * n
        complete_count = 0  # To‘liq (complete) komponentlar soni

        # 3. Har bir tugun bo‘yicha, agar u hali tekshirilmagan bo‘lsa, uning tegishli komponentini DFS yoki BFS yordamida topamiz.
        for i in range(n):
            if not visited[i]:
                # Agar i tuguni hali tashrif buyurilmagan bo‘lsa, yangi komponentni BFS yordamida topamiz.
                queue = deque([i])
                visited[i] = True
                nodes = []  # Hozirgi komponentdagi tugunlarni saqlaymiz
                edge_count = 0  # Hozirgi komponentdagi (ya’ni, o'tilgan) qirralar sonini hisoblaysiz. (Eslatma: har bir qirra ikki marta hisoblanadi.)

                while queue:
                    cur = queue.popleft()
                    nodes.append(cur)
                    # current tugunning qo‘shni tugunlari ro‘yhatining uzunligi uning qirra sonini bildiradi.
                    edge_count += len(graph[cur])
                    for neighbor in graph[cur]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                # 4. Hozirgi komponentdagi tugunlar soni m:
                m = len(nodes)
                # Har bir qirra ikki marta hisoblanganligi sababli, haqiqiy qirralar soni:
                actual_edges = edge_count // 2

                # 5. To‘liq (complete) komponent aniqlash:
                #    Kompleт graﬁkda m tugun bo‘lsa, har bir tugun bir-biri bilan bog‘langan, shu bilan qirralar soni m*(m-1)//2 bo‘lishi kerak.
                if actual_edges == m * (m - 1) // 2:
                    complete_count += 1

        # 6. Natijada, to‘liq komponentlar sonini qaytaramiz.
        return complete_count
