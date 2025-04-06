class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Agar nums bo'sh bo'lsa, bo'sh ro'yxat qaytaramiz
        if not nums:
            return []

        # 1. Kiruvchi massivdagi sonlarni o'sish tartibida saralab chiqamiz.
        nums.sort()
        n = len(nums)

        # 2. Har bir indeks uchun DP massivi yaratamiz:
        #    dp[i] — nums[i] tugagani bilan tugaydigan, kriteriylarga mos bo'lgan eng katta
        #    kichik to'plamning uzunligi. Boshlang'ich qiymat sifatida har bir element o'z-o'zini tashkil qiladi (uzunlik 1).
        dp = [1] * n

        # 3. Qaysi oraliq indeks orqali hisob topilganini qayd etish uchun prev massiv.
        #    prev[i] — nums[i] elementidan oldin joylashgan barcha elementlar orasidan,
        #    u bilan bo'linishni saqlagan eng yaxshi oldingi elementning indeksi.
        prev = [-1] * n

        # 4. Eng katta kichik to'plam uzunligini va oxirgi elementining indeksini topish uchun:
        max_size = 0
        max_index = -1

        # 5. Har bir element uchun (0 dan n-1 gacha) boshqa elementlarni tekshiramiz:
        for i in range(n):
            for j in range(i):
                # Agar nums[i] nums[j] ga to'liq bo'linsa, ya'ni nums[i] % nums[j] == 0,
                # unda nums[i] ni dp[j] ga qo'shib, to'plamni kengaytirish mumkin.
                if nums[i] % nums[j] == 0:
                    # Agar nums[j] bilan kengaytirilsa, to'plam uzunligi oshsa, yangilaymiz:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            # Agar hozirgi to'plam uzunligi eng yuqori bo'lsa, uni xotirada saqlaymiz.
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # 6. prev massividan yordam olib, eng katta kichik to'plamni rekonstruksiya qilamiz.
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        result.reverse()  # Biz orqadan qo'shganmiz, shuning uchun natijani teskari aylantiramiz.

        return result
