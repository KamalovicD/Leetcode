from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 1. Berilgan nums massivining elementlar sonini olamiz.
        n = len(nums)

        # 2. Har bir indeks uchun chapdan (prefix) maksimal qiymatni saqlovchi massiv yaratiladi.
        prefix_max = [0] * n
        prefix_max[0] = nums[0]  # 0-indeks uchun, maksimal qiymat o'zi bilan teng.
        # 3. 1-indeksdan boshlab, har bir indexgacha bo'lgan maksimal qiymatni hisoblaymiz.
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # 4. Har bir indeks uchun o'ngdan (suffix) maksimal qiymatni saqlovchi massiv yaratiladi.
        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]  # Oxirgi indeks uchun, maksimal qiymat shunchaki nums[n-1].
        # 5. Oxiridan boshlab, har bir indexdan oxirigacha bo'lgan maksimal qiymatni hisoblaymiz.
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        # 6. Maksimal uchlik qiymatini saqlash uchun o'zgaruvchi, dastlab 0 (negativ natija chiqsa 0 qaytaramiz).
        max_val = 0

        # 7. Endi o'rta indeks j uchun qaror qabul qilamiz:
        #    j indexi bo'yicha, chap tomonda i < j va o'ng tomonda k > j shartini qanoatlantiradigan holatda,
        #    maksimal natija (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1] ga teng bo'ladi.
        for j in range(1, n - 1):
            current_val = (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1]
            max_val = max(max_val, current_val)

        # 8. Natijada, eng yuqori topilgan qiymat qaytariladi.
        return max_val
