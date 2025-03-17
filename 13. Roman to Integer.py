class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Har bir Rim raqami va uning qiymatini belgilovchi lug‘at yaratiladi.
        roman_map = {
            'I': 1,  # I ning qiymati 1
            'V': 5,  # V ning qiymati 5
            'X': 10,  # X ning qiymati 10
            'L': 50,  # L ning qiymati 50
            'C': 100,  # C ning qiymati 100
            'D': 500,  # D ning qiymati 500
            'M': 1000  # M ning qiymati 1000
        }

        # 2. Umumiy yig‘indini (natijaviy butun son) 0 dan boshlaymiz.
        total = 0

        # 3. Avvalgi qiymatni (oldingi qaralgan raqamning qiymatini) saqlash uchun o'zgaruvchi; dastlab 0 ga tenglashtiramiz.
        prev = 0

        # 4. s stringini orqadan-to‘g‘ri (teskari tartibda) tekshiramiz.
        #    Misol uchun, s = "MCMXCIV" bo'lsa, bu "VICXMC M" kabi emas, balki eng so‘nggi belgidan to boshigacha ko‘rib chiqiladi.
        for ch in s[::-1]:
            # Hozirgi harfni roman_map lug‘atidan olib, qiymatini aniqlaymiz.
            value = roman_map[ch]

            # 5. Agar hozirgi raqamning qiymati oldingi (ya’ni, chap tomondagi) raqam qiymatidan kichik bo'lsa,
            #    bu holda ayirma holati sodir bo‘ladi. Misol uchun, "IV" uchun I ning qiymati (1) V (5) dan kichik,
            #    shuning uchun 1 ni ayiramiz.
            if value < prev:
                total -= value
            else:
                # Aks holda, qiymatni umumiy yig‘indiga qo‘shamiz.
                total += value

            # 6. Hozirgi qiymatni prev ga saqlaymiz, shunda keyingi iteratsiyada solishtirishda foydalanamiz.
            prev = value

        # 7. Natijada olingan yig‘indi, ya’ni butun son, qaytariladi.
        return total
