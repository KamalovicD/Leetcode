from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # 1. Avval massivni tartibga solish orqali eng kichik elementdan eng kattaga o‘tish tartibini hosil qilamiz.
        arr.sort()

        # 2. Birinchi ikki element orasidagi farqni hisoblaymiz va uni 'diff' o‘zgaruvchisiga saqlaymiz.
        diff = arr[1] - arr[0]

        # 3. Qolgan elementlar bo‘ylab iteratsiya o‘tkazamiz:
        #    Har bir element va uning oldingisidagi element orasidagi farqni hisoblaymiz.
        #    Agar birorta farq 'diff' ga teng bo‘lmasa, massiv arifmetik progressiya emas.
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        # 4. Agar barcha farqlar teng bo‘lsa, massiv arifmetik progressiya hisoblanadi.
        return True
