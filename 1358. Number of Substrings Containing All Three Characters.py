import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)  # Satr uzunligini aniqlaymiz
        # Har bir a, b, c belgilarining uchrashuv indekslarini saqlash uchun lug'at
        occ = {'a': [], 'b': [], 'c': []}

        # 1. Satrni boshidan oxirigacha yurib, har bir belgi uchun uning indeksini ro'yxatga qo'shamiz.
        for i, ch in enumerate(s):
            occ[ch].append(i)

        result = 0  # Natijani saqlash uchun o'zgaruvchi

        # 2. Har bir indeks i (substringning boshlanish indeksi) uchun:
        for i in range(n):
            pos = -1  # Bu o'zgaruvchi uchta belgidan eng kech uchrashuv indeksini saqlaydi.
            for ch in ['a', 'b', 'c']:
                # 3. Binary search yordamida occ[ch] ro'yxatidan i ga teng yoki undan katta eng kichik indeksni qidiramiz.
                j = bisect.bisect_left(occ[ch], i)
                # Agar i dan keyin ushbu belgidan uchrashuv topilmasa:
                if j == len(occ[ch]):
                    pos = None  # Bu shart bajarilmasa, ya'ni substringda barcha harflar mavjud emas.
                    break
                # 4. Har bir belgi uchun i dan so'nggi uchrashuvni olish va
                # maksimal (ya'ni, kechroq) indeksni saqlash:
                pos = max(pos, occ[ch][j])
            # Agar pos None bo'lmasa, demak i dan boshlab substringda hamma uchta belgi mavjud
            if pos is not None:
                # 5. Endi, substring boshlanishi i bo'lib, uchtalik belgining eng oxirgi paydo bo'lishi pos bo'lsa,
                # unda i dan boshlab oxirgi indeksgacha (n-1) bo'lgan hamma substringlar shartga javob beradi.
                # Ularning soni: n - pos.
                result += (n - pos)

        return result  # Umumiy valid substringlar sonini qaytaramiz.
