from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. "numbers" ro'yxatini yaratamiz: ["1", "2", ..., "n"]
        numbers = [str(i) for i in range(1, n + 1)]

        # 2. "factorials" ro'yxatini hisoblaymiz:
        # factorials[i] – i! ni ifodalaydi, bu erda i 0 dan n-1 gacha bo‘ladi.
        # Masalan, agar n = 3 bo‘lsa: factorials = [1, 1, 2]
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i

        # 3. k ni 0-index asosiga moslashtiramiz:
        # Masalan, agar k 3 bo‘lsa, 0-index asosida bu 2 ga teng bo‘ladi.
        k -= 1

        # 4. Natija (permutatsiya) uchun bo‘sh ro‘yhat
        result = []

        # 5. So'nggi elementdan birinchi elementgacha (teskari tartibda) iteratsiya qilamiz:
        # Bu iteratsiya qadamida har bir pozitsiyadagi elementni tanlaymiz.
        for i in range(n - 1, -1, -1):
            # a) Hozirgi qadam uchun, i! permutatsiyalar nechta guruhga bo‘linadi.
            # Index = k // factorials[i] aniqlaydi, ya’ni k ning qaysi guruhiga tushayotganimizni bildiradi.
            index = k // factorials[i]

            # b) numbers ro’yxatidan index-dagi elementni olib, result ga qo‘shamiz
            result.append(numbers.pop(index))

            # c) k ni yangilaymiz: k = k % factorials[i]
            k %= factorials[i]

        # 6. Natija ro'yxatidagi elementlarni birlashtirib, string shaklida qaytaramiz.
        return ''.join(result)
