from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 1. Agar massivda bironta element k dan kichik bo'lsa,
        #    uni k ga oshirish imkonsiz, chunki amallar faqat kamaytirish mumkin.
        if any(num < k for num in nums):
            return -1

        # 2. Takrorlanmas (unique) qiymatlarni olish:
        distinct_values = set(nums)

        # 3. Javob – k dan katta bo‘lgan distinct (takrorlanmas) qiymatlarning soni:
        #    Har bir bunday qiymat uchun bir amal talab etiladi.
        operations = sum(1 for value in distinct_values if value > k)

        return operations
