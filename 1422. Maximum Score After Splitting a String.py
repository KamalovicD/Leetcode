class Solution:
    def maxScore(self, s: str) -> int:
        # 1. Dastlab, satrdagi barcha "1" lar sonini hisoblaymiz.
        ones_total = s.count('1')

        # 2. Maksimal ballni (javobni) saqlash uchun o‘zgaruvchi, boshlang‘ich qiymatini 0 deb belgilaymiz.
        max_score = 0

        # 3. Chap bo‘lakdagi "0" lar sonini hisoblash uchun o‘zgaruvchi.
        zeros_count = 0

        # 4. Boshlanishda, butun satr "o‘ng bo‘lak" deb hisoblanadi, shuning uchun "1" larning sonini to‘liq o‘ng bo‘lakdagi "1" lar soniga tenglaymiz.
        ones_in_right = ones_total

        # 5. Satrni birinchi belgidan oxirgi belgidan avvalgacha aylantiramiz (oxirgi bo‘lak bo‘sh bo‘lishi mumkinligidan oldini olish uchun,
        #    ya'ni ikkala bo‘lak ham bo‘sh bo‘lmasligi uchun i = len(s)-1 gacha).
        for i in range(len(s) - 1):
            # 6. Agar joriy belgi "0" bo‘lsa, chap bo‘lakga qo‘shamiz va uning hisobini 1 ga oshiramiz.
            if s[i] == '0':
                zeros_count += 1
            # 7. Agar joriy belgi "1" bo‘lsa, demak endi u o‘ng bo‘lakka kirmaydi, shuning uchun o‘ng bo‘lakdagi "1" lar sonini
            #    1 ga kamaytiramiz.
            else:
                ones_in_right -= 1

            # 8. Joriy ajratishda ball — chap bo‘lakdagi "0" lar soni va o‘ng bo‘lakdagi "1" lar sonining yig‘indisidir.
            current_score = zeros_count + ones_in_right

            # 9. Agar joriy hisoblangan ball bizda saqlanayotgan maksimal balldan katta bo‘lsa, uni yangilaymiz.
            if current_score > max_score:
                max_score = current_score

        # 10. Eng yuqori ballni qaytaramiz.
        return max_score
