from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Operatsiyalarni qo'llash: har bir i uchun, agar nums[i] == nums[i+1] bo'lsa,
        # uni ikki baravar oshirib, keyingi elementni 0 ga o'zgartiramiz.
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # 2. Nol (0) bo'lmagan elementlarni to'playmiz
        result = [num for num in nums if num != 0]
        # 3. Nol elementlar sonini aniqlaymiz va ularni natijaviy ro'yxat oxiriga qo'shamiz.
        zeros_count = n - len(result)
        result.extend([0] * zeros_count)

        return result
