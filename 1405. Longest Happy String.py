from typing import List


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 1. Har bir harf uchun qolgan miqdorni va harfni juft sifatida saqlaymiz.
        #    counts = [[qolgan son, harf], ...]
        counts = [[a, 'a'], [b, 'b'], [c, 'c']]

        # 2. Natija uchun bo‘sh ro‘yxat.
        result = []

        # 3. Har doim qo‘shimcha harf qo‘shish imkoniyati qolguncha davom etamiz.
        while True:
            # 4. Qolgan harflarni ularning miqdoriga qarab kamayish tartibida saralaymiz.
            counts.sort(key=lambda x: x[0], reverse=True)

            # 5. Har bir iteratsiyada, shartlarga mos keladigan harfni aniqlash uchun flag (belgi)
            #    yordamida, agar hech qanday harfni qo‘shib bo‘lmasa, sikldan chiqamiz.
            added = False

            # 6. Eng ko‘p qolgan harfdan boshlab, uchta harf ustida aylanamiz.
            for i in range(3):
                # Agar tanlangan harf uchun qolgan miqdor 0 ga teng bo‘lsa, uni o'tkazib yuboramiz.
                if counts[i][0] <= 0:
                    continue

                # 7. Agar result ro‘yxatida oxirgi ikki harf bir xil bo‘lsa,
                #    misol uchun, "aa" bo‘lsa va agar biz yana 'a' qo‘shsak "aaa" hosil bo‘ladi.
                #    Shunday holatda ushbu harfni qo‘shishga ruxsat berilmaydi.
                if len(result) >= 2 and result[-1] == result[-2] == counts[i][1]:
                    continue

                # 8. Agar yuqoridagi holatlar bo'lmasa, biz ushbu harfni result ga qo‘shamiz.
                result.append(counts[i][1])
                # 9. Shu harfning qolgan miqdorini 1 taga kamaytiramiz.
                counts[i][0] -= 1
                added = True
                # 10. Har doim eng yaxshi (eng ko‘p mavjudligi) harfni qo‘shganimizdan keyin for siklidan chiqamiz.
                break

            # 11. Agar for sikli davomida hech qanday harf qo‘sha olmagan bo‘lsak,
            #    demak, qo‘shimcha harfni qo‘shish shartlari bajarilmaydi va sikl tugaydi.
            if not added:
                break

        # 12. Natijada hosil bo‘lgan listni satrga aylantirib, qaytaramiz.
        return "".join(result)
