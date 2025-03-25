from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Qo'shimcha yordamchi funksiya:
        # Bu funksiya berilgan ro'yxat (rects) ustida
        # "cut" (kesish) joylarini aniqlashga harakat qiladi.
        # get_start – to'rtburchakning boshlanish koordinatasini (x yoki y)
        # beradi, get_end – to'rtburchakning tugash koordinatasini (x yoki y)
        # beradi.
        # Agar ro'yxatda kamida ikki "bo'sh" joy (ya'ni, gap, kesish uchun mos joy)
        # aniqlansa, bu yo'nalishda uchta bo'limga ajratish mumkin.
        def valid_partition(rects, get_start, get_end):
            m = len(rects)
            prefix_max = [0] * m
            # Birinchi elementning tugash koordinatasini prefix_max ga joylaymiz.
            prefix_max[0] = get_end(rects[0])
            # Har bir to'rtburchakka qarab, 0-dan shu indeksgacha bo'lgan maksimal tugash koordinatasini
            # hisoblaymiz.
            for i in range(1, m):
                prefix_max[i] = max(prefix_max[i - 1], get_end(rects[i]))
            gaps = 0
            # To'rtburchaklar saralangan holda, har bir qo'shni juftlik orasida "bo'sh" (kesish uchun mos joy)
            # borligini tekshiramiz. Bu yerda gap shart – avvalgi qismning maksimal tugash koordinatasi
            # (prefix_max[i]) keyingi to'rtburchakning boshlanish koordinatasidan (get_start(rects[i+1]))
            # kichik yoki teng bo'lishi kerak.
            for i in range(m - 1):
                if prefix_max[i] <= get_start(rects[i + 1]):
                    gaps += 1
                    # Agar ikki xil gap topilsa, demak biz uchta bo'limga ajratish mumkinligini anglatadi.
                    if gaps >= 2:
                        return True
            return False

        # 1. Vertikal kesishlarni tekshiramiz.
        #    Biz to'rtburchaklarni ularning x bo'yicha boshlanish koordinatasiga qarab saralaymiz.
        #    Bu orqali agar chapda joylashgan to'rtburchaklar guruhi butunlay chap tomonda qolsa
        #    va o'ng tomondagi to'rtburchaklar shu guruhdan ajralib tursa, ular orasida kesish chizig'i
        #    uchun "bo'sh" joy aniqlanishi mumkin.
        rects_by_x = sorted(rectangles, key=lambda r: r[0])  # r[0] - boshlanish x
        vertical_possible = valid_partition(rects_by_x, lambda r: r[0], lambda r: r[2])
        # Bu yerda:
        #   - get_start: r[0] (to'rtburchakning chap tomonidagi x)
        #   - get_end: r[2] (to'rtburchakning o'ng tomonidagi x)

        # 2. Gorizontal kesishlarni tekshiramiz.
        #    Shu yo'nalishda, to'rtburchaklarni y bo'yicha, ya'ni pastki qism (starty) bo'yicha saralaymiz.
        #    Pastga qarab joylashgan to'rtburchaklar qat'iy pastda bo'lib, yuqoridagi to'rtburchaklardan
        #    ajralishi kerak.
        rects_by_y = sorted(rectangles, key=lambda r: r[1])  # r[1] - boshlanish y (quyi qirra)
        horizontal_possible = valid_partition(rects_by_y, lambda r: r[1], lambda r: r[3])
        # Bu yerda:
        #   - get_start: r[1] (to'rtburchakning quyi qirrasidagi y)
        #   - get_end: r[3] (to'rtburchakning yuqori qirrasidagi y)

        # Agar vertikal yoki gorizontal bo'linish mumkin bo'lsa, True qaytaramiz.
        return vertical_possible or horizontal_possible
