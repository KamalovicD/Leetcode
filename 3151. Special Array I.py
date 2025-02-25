from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # 1. Agar arrayda faqat bitta element bo'lsa, uni maxsus array deb hisoblaymiz,
        #    chunki hech qanday qo'shni elementlar yo'q.
        if len(nums) <= 1:
            return True

        # 2. Arraydagi har bir qo'shni juftlik ustida yurib chiqamiz:
        #    Biz 1-indeksdan boshlab, har bir element va uning oldingi elementining qoldig'ini (% 2)
        #    hisoblaymiz. Agar ular teng bo'lsa, demak ikkala element ham bir xil parityaga ega.
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False

        # 3. Agar barcha qo'shni elementlar pariteleri farq qilsa, array maxsus hisoblanadi.
        return True
