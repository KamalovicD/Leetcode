class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indekslash

    def update(self, idx, delta):
        # Berilgan indeksga delta qo'shamiz
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        # 1 dan idx gacha bo'lgan summani qaytaradi
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos1 = [0] * n
        pos2 = [0] * n

        # nums1 dagi har bir elementning indeksini saqlaymiz
        for i, v in enumerate(nums1):
            pos1[v] = i
        # nums2 dagi har bir elementning indeksini saqlaymiz
        for i, v in enumerate(nums2):
            pos2[v] = i

        # Har bir element uchun (pos1, pos2, qiymat) ni saqlaymiz
        elements = []
        for v in range(n):
            elements.append((pos1[v], pos2[v], v))

        # Chap hisoblagichlarni hisoblash
        # Elementlarni pos1 bo'yicha tartiblaymiz
        elements_left = sorted(elements, key=lambda x: x[0])
        fenwick_left = FenwickTree(n)
        left_counts = [0] * n
        for elem in elements_left:
            p1, p2, v = elem
            # Fenwick daraxtida p2 dan oldingi elementlar soni
            sum_le = fenwick_left.query(p2)
            left_counts[v] = sum_le
            # Fenwick daraxtiga yangi elementni qo'shamiz (1-based)
            fenwick_left.update(p2 + 1, 1)

        # O'ng hisoblagichlarni hisoblash
        # Elementlarni pos1 bo'yicha teskari tartiblaymiz
        elements_right = sorted(elements, key=lambda x: -x[0])
        fenwick_right = FenwickTree(n)
        right_counts = [0] * n
        current_size = 0  # Fenwick daraxtidagi elementlar soni
        for elem in elements_right:
            p1, p2, v = elem
            converted_c = p2 + 1  # 1-based konvertatsiya
            # Fenwick daraxtida p2 dan keyingi elementlar soni
            sum_le = fenwick_right.query(converted_c)
            right_counts[v] = current_size - sum_le
            # Fenwick daraxtiga yangi elementni qo'shamiz
            fenwick_right.update(converted_c, 1)
            current_size += 1

        # Yakuniy natijani hisoblash
        total = 0
        for v in range(n):
            total += left_counts[v] * right_counts[v]
        return total