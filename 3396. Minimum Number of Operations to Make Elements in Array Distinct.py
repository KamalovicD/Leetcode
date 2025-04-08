from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)  # Massivdagi elementlar sonini olamiz.

        # Maksimal amallar soni: agar 3 ta elementni olib tashlasak, massiv bo‘sh bo‘lishi mumkin.
        # (n + 2) // 3 – bu n elementni 3 ga bo‘lganda kerak bo‘ladigan amallar sonini beradi.
        max_ops = (n + 2) // 3

        # Har bir mumkin bo'lgan amal soni (ops) uchun tekshiramiz:
        for ops in range(max_ops + 1):
            start = 3 * ops  # Har amalda boshidan olib tashlangan elementlar soni.

            # Agar start indeksi massiv uzunligidan katta yoki teng bo‘lsa,
            # demak biz butun massivni olib tashlaganmiz (yoki massiv bo‘sh) → u holda javobni qaytaramiz.
            if start >= n:
                return ops

            # Qolgan massiv: boshidan 3 * ops ta element olib tashlangandan keyingi elementlar.
            remaining = nums[start:]

            # Agar qolgan massivdagi barcha elementlar bir xil bo‘lmasa (distinct bo‘lsa),
            # ya'ni elementlar soni to‘plam (set) uzunligiga teng bo‘lsa,
            # demak barcha elementlar farq qiladi → javobni qaytaramiz.
            if len(set(remaining)) == len(remaining):
                return ops

        # Agar hech qaysi holatda false chiqmasa (teorematik holda) maksimal amallar sonini qaytaramiz.
        return max_ops
