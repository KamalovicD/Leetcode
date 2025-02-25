from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 1. Natijaviy ishorani saqlovchi o'zgaruvchini belgilaymiz. Boshlanishda uni 1 ga tenglaymiz,
        #    chunki ko'paytma ishorasi 1 bilan ko'paytirish ta'sir ko'rsatmaydi.
        sign = 1

        # 2. Massivdagi har bir son ustida iteratsiya o'tkazamiz.
        for num in nums:
            # 3. Agar hozirgi son 0 ga teng bo'lsa,
            #    demak butun ko'paytma ham 0ga teng bo'ladi. Shuning uchun 0 qaytaramiz.
            if num == 0:
                return 0

            # 4. Agar hozirgi son manfiy bo'lsa, ishora qiymatini -1 ga ko'paytiramiz va shunday qilib
            #    jami ko'paytmaning ishorasiga ta'sir qilamiz.
            elif num < 0:
                sign *= -1

        # 5. Tsikl tugagach, yig'indaning ishorasi saqlanib qoladi va uni qaytaramiz.
        return sign
