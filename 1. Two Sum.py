class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Bo'sh lug‘at (dictionary) yaratamiz. Bu erda elementlarni saqlaymiz.

        # Har bir sonni ko‘rib chiqamiz
        for i, num in enumerate(nums):
            complement = target - num  # Juft kerakli sonni hisoblaymiz

            if complement in num_map:  # Agar bu son avval ro‘yxatda uchragan bo‘lsa
                return [num_map[complement], i]  # Juftlikni topdik, indekslarini qaytaramiz

            num_map[num] = i  # Hozirgi sonni lug‘atga qo‘shamiz

        return []  # (Bu joy aslida ishlamaydi, chunki doimo javob bor)
