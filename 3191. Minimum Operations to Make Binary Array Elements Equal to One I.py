from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 1. Natija sifatida bajarilgan operatsiyalar sonini saqlash uchun o'zgaruvchi.
        ops = 0
        n = len(nums)

        # 2. 0-indexdan boshlab, oxirgi 2 ta elementni hisobga olmaguncha (n-2 qadar) ro'yxatni aylanamiz.
        #    Sababi, faqat 3 ta ketma‐ket elementni tanlab "flip" qilish mumkin,
        #    shuning uchun ro'yxatning oxirgi 2 indexda operatsiya qo‘llab bo‘lmaydi.
        for i in range(n - 2):
            # 3. Agar hozirgi element 0 bo'lsa, bu joyda chiroq o'chirilgan bo'lib, uni yoqish uchun operatsiya kerak.
            if nums[i] == 0:
                # 4. 3 ta ketma‐ket elementni "flip" qilamiz:
                #    - Agar 0 bo'lsa, 1 ga aylantiramiz (1 - 0 = 1)
                #    - Agar 1 bo'lsa, 0 ga aylantiramiz (1 - 1 = 0)
                for j in range(i, i + 3):
                    # Flip operatsiyasini bajarish:
                    nums[j] = 1 - nums[j]
                # 5. Operatsiyalar sonini 1 ga oshiramiz.
                ops += 1

        # 6. Sikl tugagach, natijani tekshiramiz: agar barcha elementlar 1 ga teng bo'lsa,
        #    to'g'ri operatsiyalar sonini qaytaramiz; aks holda -1 qaytaramiz.
        if all(num == 1 for num in nums):
            return ops
        else:
            return -1
