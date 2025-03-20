from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.comp_and = [(1 << 31) - 1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int, w: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            new_val = self.comp_and[rx] & self.comp_and[ry] & w
            self.parent[ry] = rx
            self.comp_and[rx] = new_val
        else:
            self.comp_and[rx] &= w


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for u, v, w in edges:
            dsu.union(u, v, w)

        result = []
        for s, t in query:
            if dsu.find(s) != dsu.find(t):
                result.append(-1)
            else:
                result.append(dsu.comp_and[dsu.find(s)])

        return result
