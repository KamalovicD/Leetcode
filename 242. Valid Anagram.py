class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Agar 's' va 't' uzunliklari teng bo'lmasa, False qaytaramiz.
        if len(s) != len(t):
            return False

        # 2. 's' va 't' satrlaridagi harflarni sanaymiz.
        from collections import Counter
        s_count = Counter(s)
        t_count = Counter(t)

        # 3. Harflarning chastotalarini solishtiramiz.
        return s_count == t_count
