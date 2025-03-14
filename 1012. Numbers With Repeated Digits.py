class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # 1. n ni satrga aylantiramiz va uning uzunligini aniqlaymiz.
        # Bu, sonning nechta xonasiga (raqamiga) ega ekanligini aniqlashda yordam beradi.
        s = str(n)
        m = len(s)  # n xonasining soni

        # 2. Takrorlanmaydigan raqamlardan tashkil topgan sonlar umumiy sonini (unique_count) 0 dan boshlaymiz.
        unique_count = 0

        # 3. Kichikroq xonali sonlar bo‘yicha hisoblash:
        #    [1, n] oralig‘ida, m xonalikdan kichik sonlarning barchasida takrorlanmaydigan raqamli sonlarni hisoblaymiz.
        #    Masalan, agar n = 1000 (m = 4) bo‘lsa, avvalo 1-, 2- va 3-xonali sonlardagi takrorlanmaydigan kombinatsiyalarni qo‘shamiz.
        for i in range(1, m):  # i = sonning xonalari (1-xona, 2-xona, ..., m-1 xona)
            count_for_length = 9  # Eng birinchi raqam uchun 9 ta tanlov (0 bo‘lishi mumkin emas)
            for j in range(1, i):
                # Qolgan raqamlar uchun tanlovlar: har safar avvalgi tanlovdan farqli raqamlar qoladi.
                count_for_length *= (10 - j)
            unique_count += count_for_length
            # Shu yerda biz i xonalik sonlardagi barcha kombinatsiyalarni qo‘shamiz.

        # 4. Endi n bilan bir xil xonalik sonlar (m xonali) uchun takrorlanmaydigan raqamli sonlarni hisoblaymiz.
        seen = set()  # Qaysi raqamlar allaqachon tanlanganligini saqlash uchun.
        for i, ch in enumerate(s):
            digit = int(ch)
            # Agar i == 0 bo'lsa, birinchi xonada 0 bo‘lmasa kerak (chunki sonning boshida 0 bo‘lmaydi).
            start = 0 if i > 0 else 1
            # Hozirgi pozitsiyadan kichik raqamlarni sinab ko‘ramiz.
            for d in range(start, digit):
                if d in seen:
                    # Agar bu raqam allaqachon tanlangan bo'lsa, o‘tkazamiz.
                    continue
                # Qolgan pozitsiyalar uchun mumkin bo'lgan tanlovlarni hisoblaymiz.
                available = 10 - (i + 1)  # Hozirgi pozitsiyadan keyingi tanlov uchun qolgan raqamlar soni.
                ways = 1
                for k in range(m - i - 1):
                    ways *= (available - k)
                    # Har bir qolgan pozitsiya uchun, raqamlar ortib boradi.
                unique_count += ways  # Bu kombinatsiyalar n dan kichik bo'lgan sonlar sonini beradi.

            # Agar hozirgi raqam allaqachon tanlangan bo‘lsa, bundan keyingi kombinatsiyalarni hisoblash mumkin emas.
            if digit in seen:
                break
            seen.add(digit)
            # Agar biz so‘nggi raqamga yetib kelsak va barcha raqamlar unikal bo'lsa, n o‘zi ham takrorlanmas son sifatida hisoblanadi.
            if i == m - 1:
                unique_count += 1

        # 5. [1, n] oralig‘idagi sonlar soni n ga teng.
        #    Shuning uchun, takroriy raqamli sonlar soni = n - (takrorlanmaydigan raqamlardan tashkil topgan sonlar soni)
        return n - unique_count
