class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. 32-bit integer chegaralari
        MAX_INT = 2**31 - 1   # 2147483647
        MIN_INT = -2**31      # -2147483648

        # 2. Edge case: dividend == MIN_INT va divisor == -1
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT  # Bu holatda natija 2^31 bo'lib, 32-bit chegarani oshadi.

        # 3. Belgini aniqlaymiz:
        # Agar dividend va divisor bir xil belgi bo'lsa, natija musbat, aks holda manfiy.
        sign = 1 if (dividend >= 0) == (divisor >= 0) else -1

        # 4. Faqat musbat qismini hisoblash uchun absolyut qiymatlarga o'tamiz.
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0  # Natijaviy bo‘lish natijasi

        # 5. Dividend yetarli katta bo‘lguncha, divisorning mos ko‘paytmasini topamiz.
        while dividend_abs >= divisor_abs:
            # temp: divisor_abs ning hozirgi ko‘paytmali qiymati
            # multiple: shu ko‘paytmaga mos karrani ifodalaydi (qaysi marta ayirayotganimiz)
            temp = divisor_abs
            multiple = 1
            # Bit shifting yordamida temp ni ikki baravar oshirib boramiz
            # (ya'ni temp ni chapga siljitamiz) shundayki, dividend_abs dan yuqori bo'lmasin.
            while dividend_abs >= (temp << 1):
                temp <<= 1       # temp = temp * 2 (lekin bu yerda multiplication emas, bit shifting)
                multiple <<= 1   # multiple = multiple * 2
            # Topilgan maksimal ko‘paytma temp ni dividend_abs dan ayiramiz,
            # va quotient ga ham shu multiple ni qo‘shamiz.
            dividend_abs -= temp
            quotient += multiple

        # 6. Belgini natijaga qo‘shamiz.
        quotient = sign * quotient

        # 7. Chegaralarni tekshiramiz: agar quotient 32-bit cheklovdan chiqqan bo'lsa, uni clamp qilamiz.
        if quotient < MIN_INT:
            return MIN_INT
        if quotient > MAX_INT:
            return MAX_INT

        return quotient