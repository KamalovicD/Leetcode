from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # left va right chegaralar:
        # left = 1 (minimal bo'lishi mumkin bo'lgan qand miqdori)
        # right = max(candies) (hech qaysi bo'lak shu miqdordan oshishi mumkin emas)
        left, right = 1, max(candies)
        ans = 0  # Natijada maksimal har bir bolaning olishi mumkin bo'lgan qand miqdorini saqlash uchun

        # Binary search sikli: left <= right bo'lsa davom ettiramiz
        while left <= right:
            mid = (left + right) // 2  # mid - har bir bolaga taqsimlanishi kerak bo'lgan kandidate qand miqdori
            count = 0  # count - jami hosil qilinadigan bo'laklar sonini hisoblaydigan o'zgaruvchi

            # Har bir konfet yig'indisidan mid qismga bo'linadigan bo'laklar sonini qo'shamiz:
            for candy in candies:
                count += candy // mid
                # Agar count allaqachon k yoki undan yuqori bo'lsa, qo'shishni to'xtatamiz
                if count >= k:
                    break

            # Agar joriy mid qiymati bo'yicha jami bo'laklar soni k dan katta yoki teng bo'lsa,
            # demak mid qiymati har bir bola uchun berilishi mumkin va biz natijani yangilaymiz,
            # shuningdek, yanada kattaroq qiymatni sinab ko'rish uchun left ni oshiramiz.
            if count >= k:
                ans = mid
                left = mid + 1
            else:
                # Aks holda, bo'laklar soni yetarli emas, shuning uchun right ni pasaytiramiz.
                right = mid - 1

        # Natijada, ans qiymati maksimal har bir bolaga beriladigan konfetlar miqdorini bildiradi.
        return ans
