from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 1. Dominant elementni aniqlash uchun, har bir elementning nechta marta uchrashganini hisoblaymiz.
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 2. Umumiy massiv uzunligi
        n = len(nums)

        # 3. Dominant element: massiv elementlari ichidan u element bo‘lib,
        #    uning chastotasi (soni) massiv uzunligining yarmidan ko‘p bo‘lishi kerak.
        overall = None
        for key, value in count.items():
            if value * 2 > n:
                overall = key
                break

        # 4. Dominant elementning umumiy chastotasi
        total = count[overall]

        # 5. Endi massivni ikkiga bo‘lish uchun to‘g‘ri ajratish indexini topamiz.
        #    Ajratish indexi i, 0 <= i < n-1 bo‘lishi shart.
        #    Bo‘limlarga bo‘lingan massivlarda ham dominant element (overall) yarmi ustida
        #    qatnashishi lozim.
        prefix_count = 0  # Avvalgi bo‘limda (prefix) overall elementining necha marta uchrashi.
        for i in range(n - 1):
            if nums[i] == overall:
                prefix_count += 1

            # 6. Ajratish indexi i uchun ikki bo‘lim haqida tekshiruv:
            #    - Birinchi bo‘lim (nums[0:i+1]) uzunligi = i + 1, bunda dominant element
            #      overall elementining chastotasi prefix_count bo‘lishi kerak.
            #      Shart: prefix_count * 2 > (i + 1)
            #
            #    - Ikkinchi bo‘lim (nums[i+1:n]) uzunligi = n - i - 1, bunda overall
            #      elementining chastotasi total - prefix_count bo‘ladi.
            #      Shart: (total - prefix_count) * 2 > (n - i - 1)
            #
            #    Agar har ikkala shart bajarilsa, u holda shu index bo‘yicha bo‘lish mumkin.
            if prefix_count * 2 > (i + 1) and (total - prefix_count) * 2 > (n - i - 1):
                return i

        # 7. Agar hech qanday to‘g‘ri ajratish indexi topilmasa, -1 qaytaramiz.
        return -1
