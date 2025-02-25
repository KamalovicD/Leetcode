class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Rim raqamlarining har bir belgisining to'g'ri butun qiymatini aniqlash uchun lug'at tuzamiz.
        roman_values = {
            'I': 1,  # I belgisi 1 ga teng
            'V': 5,  # V belgisi 5 ga teng
            'X': 10,  # X belgisi 10 ga teng
            'L': 50,  # L belgisi 50 ga teng
            'C': 100,  # C belgisi 100 ga teng
            'D': 500,  # D belgisi 500 ga teng
            'M': 1000  # M belgisi 1000 ga teng
        }

        total = 0  # Yakuniy natijani jamlaydigan o'zgaruvchi, boshlanishida 0 ga teng
        i = 0  # String bo'ylab yurish uchun indeks; i hozirgi belgi pozitsiyasini bildiradi

        # 2. While tsikli yordamida string (s) bo'ylab iteratsiya qilamiz
        while i < len(s):
            # 3. Agar keyingi belgi mavjud bo'lsa va hozirgi belgi qiymati keyingi belgidan kichik bo'lsa,
            #    demak biz subtraction qoidasi (ayirish) holatini uchratdik.
            #    Masalan, "IV" da I (1) V (5) dan kichik, shuning uchun 5 - 1 = 4 bo'ladi.
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total += roman_values[s[i + 1]] - roman_values[s[i]]
                # Bu holatda biz ikki belgini ham ishlatdik, shuning uchun indeksni 2 ga oshiramiz.
                i += 2
            else:
                # 4. Aks holda, oddiy qo'shish amalini bajarib, joriy belgining qiymatini natijaga qo'shamiz.
                total += roman_values[s[i]]
                # Faqat bitta belgi ishlatilgani sababli indeksni 1 ga oshiramiz.
                i += 1

        # 5. Natija sifatida hisoblangan butun qiymat (total) ni qaytaramiz.
        return total
