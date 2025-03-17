from typing import List
from collections import Counter  # Pythonning collections modulidan Counter funksiyasini import qilamiz

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # 1. Ro'yxatdagi har bir sonning necha marta uchrashishini hisoblash uchun Counter-dan foydalanamiz.
        #    Masalan, agar nums = [3,2,3,2,2,2] bo'lsa, biz quyidagi natijani olamiz:
        #    {3: 2, 2: 4}
        counts = Counter(nums)

        # 2. Endi har bir sonning takrorlanish sonini tekshiramiz.
        #    Juftlik qilib ajratish uchun, har bir sonning takrorlanish soni juft bo'lishi kerak.
        for count in counts.values():
            # Agar biror sonning uchrashish soni juft bo'lmasa, arrayni to'liq juft qilib ajratish iloji yo'q.
            if count % 2 != 0:
                return False

        # 3. Agar barcha sonlar juft miqdorda uchrashgan bo'lsa, arrayni shartga muvofiq juftliklarga ajratish mumkin.
        return True
