from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 1. nums massivida nechta element borligini topamiz.
        n = len(nums)

        # 2. Eng yuqori uchlik qiymatini saqlash uchun max_val degan o'zgaruvchini manfiy cheksiz qiymati bilan boshlaymiz.
        max_val = float('-inf')

        # 3. Birinchi indeks uchun sikl: i 0-indekstdan boshlab to oxirgi elementgacha.
        for i in range(n):
            # 4. Ikkinchi indeks uchun sikl: j i dan keyingi elementlardan boshlanadi.
            for j in range(i + 1, n):
                # 5. Uchinchi indeks uchun sikl: k j dan keyingi elementlardan boshlanadi.
                for k in range(j + 1, n):
                    # 6. Har bir uchlik uchun qiymatni hisoblaymiz:
                    #    (nums[i] - nums[j]) * nums[k]
                    current_value = (nums[i] - nums[j]) * nums[k]

                    # 7. Agar hisoblangan qiymat hozirgi max_val dan katta bo'lsa, uni max_val ga yozamiz.
                    if current_value > max_val:
                        max_val = current_value

        # 8. Natijada, agar topilgan eng katta qiymat manfiy bo'lsa, 0 qaytaramiz, aks holda uni qaytaramiz.
        return max_val if max_val > 0 else 0
