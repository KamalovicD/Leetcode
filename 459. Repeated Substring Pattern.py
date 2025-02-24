class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 1. Agar satr uzunligi 1 ga teng bo'lsa, u takrorlanuvchi substrdan iborat bo'lishi mumkin emas.
        if len(s) == 1:
            return False

        # 2. 's' satrini o'ziga qo'shamiz va birinchi va oxirgi harflarni o'chiramiz.
        ss = (s + s)[1:-1]

        # 3. Agar 's' yangi hosil bo'lgan satr ichida mavjud bo'lsa, True qaytaramiz.
        return s in ss
