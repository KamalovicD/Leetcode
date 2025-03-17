class Solution:
    def reverse(self, x: int) -> int:
        # 1. 32-bitli butun son chegaralari
        INT_MAX = 2 ** 31 - 1  # 2147483647
        INT_MIN = -2 ** 31  # -2147483648

        # 2. Sonning belgisi (sign) aniqlanadi:
        # Agar x manfiy bo'lsa, sign -1 bo'ladi; aks holda 1.
        sign = 1 if x >= 0 else -1

        # 3. x ni musbat (absolyut qiymat) shaklga o'tkazamiz.
        x = abs(x)

        # 4. Teskari sonni ifodalash uchun o'zgaruvchi (rev) boshlang'ich qiymati 0.
        rev = 0

        # 5. Har bir raqamni ajratamiz va teskari son hosil qilamiz:
        while x:
            # 5.1. Oxirgi raqamni olamiz (pop):
            pop = x % 10
            # x dan oxirgi raqamni o'chiramiz:
            x //= 10

            # 5.2. Overflow (chegaradan chiqish) tekshiruvi:
            # Agar hozirgi teskari sonni 10 ga ko'paytirishdan keyin
            # INT_MAX dan oshib ketishi ehtimoli bo'lsa, 0 qaytaramiz.
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0

            # 5.3. Yangi raqamni teskari songa qo'shamiz:
            rev = rev * 10 + pop

        # 6. Belgini qaytaramiz va natijani hosil qilamiz:
        return sign * rev
