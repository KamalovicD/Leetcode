from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # 1. "inc" o'zgaruvchisi massivning monotonic oshishini (ya'ni har doim yoki teng holda oshishini)
        #    tekshirish uchun ishlatiladi. Dastlab, massiv monotonic oshuvchi deb faraz qilamiz.
        inc = True

        # 2. "dec" o'zgaruvchisi massivning monotonic kamayishini (ya'ni har doim yoki teng holda kamayishini)
        #    tekshirish uchun ishlatiladi. Dastlab, massiv monotonic kamayuvchi deb faraz qilamiz.
        dec = True

        # 3. Massiv elementlarini birinchi elementdan boshlab oxirigacha tekshiruvdan o'tkazamiz.
        #    Har bir elementning oldingi element bilan solishtiramiz.
        for i in range(1, len(nums)):
            # 4. Agar hozirgi element (nums[i]) oldingi element (nums[i-1])dan katta bo'lsa,
            #    demak massiv osmoyotganda (increasing) ko'rsatkichi to'g'ri bo'lsa-da,
            #    bu holat kamayish (decreasing) uchun mos emas. Shuning uchun "dec" ni False ga o'zgartiramiz.
            if nums[i] > nums[i - 1]:
                dec = False
            # 5. Agar hozirgi element (nums[i]) oldingi element (nums[i-1])dan kichik bo'lsa,
            #    demak massiv kamayishda bo'lishi kerak edi, lekin bu oshish (increasing) holatini buzadi.
            #    Shuning uchun "inc" ni False ga o'zgartiramiz.
            if nums[i] < nums[i - 1]:
                inc = False

        # 6. Agar massiv monoton bo'lishi uchun, u yoki monoton oshuvchi (inc True) yoki
        #    monoton kamayuvchi (dec True) bo'lishi kerak. Shuning uchun "inc or dec" shartini qaytaramiz.
        return inc or dec
