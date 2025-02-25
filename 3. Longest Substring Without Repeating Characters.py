class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Belgilarning o'ziga xosligini tekshirish uchun to'plam (set) dan foydalanamiz
        char_set = set()

        # Ko'rsatkichlar uchun ikki o'zgaruvchi: chap va o'ng
        l = 0

        # Eng uzun substring uzunligini saqlovchi o'zgaruvchi
        result = 0

        # O'ng ko'rsatkich orqali satr bo'ylab yurgizamiz
        for r in range(len(s)):
            # Agar belgi to'plamda mavjud bo'lsa, chap ko'rsatkichni oldinga suramiz va to'plamdan belgi o'chiramiz
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # Yangi belgi to'plamga qo'shiladi
            char_set.add(s[r])
            # Eng uzun substring uzunligini yangilaymiz
            result = max(result, r - l + 1)

        return result
