from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0  # Topilgan eng uzun "nice" subarray uzunligini saqlaydi.
        current_mask = 0  # Joriy oynada (window) qo‘shilgan elementlarning bitlarini jamlaydigan o‘zgaruvchi.
        left = 0  # Oyna (window) boshlanish indeksini bildiradi.

        # Massiv ustida o‘ng indeks "right" bo‘yicha iteratsiya qilamiz.
        for right in range(n):
            # Agar yangi qo‘shilayotgan element nums[right] ning bitlari
            # joriy current_mask bilan kesishsa (ya'ni, current_mask & nums[right] != 0),
            # demak, u yerda konflikt bor va oyna ichidan ba'zi elementlarni chiqarish kerak.
            while (current_mask & nums[right]) != 0:
                # current_mask ni yangilaymiz: oyna boshidagi (left indeksidagi) elementning bitlarini olib tashlaymiz.
                # Bitni olib tashlash uchun, current_mask ni nums[left] ning bit invertsi bilan va (&) qilamiz.
                current_mask &= ~nums[left]
                left += 1  # Oyna’shni chap tomon ko‘chiramiz.

            # Endi konflikt qolmaganligi sababli, yangi elementning bitlarini o‘ynaga qo‘shamiz.
            current_mask |= nums[right]

            # Oynaning yangi uzunligini hisoblaymiz, "right - left + 1":
            max_len = max(max_len, right - left + 1)

            # Maksimal uzunligi 30 ga yetishi mumkin (har bir raqam 30 bitdan iborat bo'lishi mumkin),
            # shuning uchun 30 ga yetganda bu maksimal yechim bo‘ladi.
            if max_len == 30:
                return 30

        return max_len
