from  typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []   # pivotdan kichik elementlar
        equal = []  # pivotga teng elementlar
        right = []  # pivotdan katta elementlar

        # Har bir element uchun uni mos ro'yxatga qo'shamiz.
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                equal.append(num)
            else:  # num > pivot
                right.append(num)

        # Hosil bo'lgan ro'yxatni ketma-ketlikda birlashtiramiz.
        return left + equal + right
