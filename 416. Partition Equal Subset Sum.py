from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1. Berilgan massivdagi barcha raqamlarning yig'indisini hisoblaymiz.
        total_sum = sum(nums)

        # 2. Agar umumiy yig'indi toq son bo'lsa, uni ikki teng qismga bo'lish mumkin emas,
        #    shuning uchun darhol False qaytaramiz.
        if total_sum % 2 != 0:
            return False

        # 3. Har bir qism uchun kerakli yig'indini hisoblaymiz.
        #    Maqsad – massivdagi sonlarning yarim yig'indisiga teng bo'lgan kichik to'plamni topish.
        target = total_sum // 2

        # 4. Dinamik dasturlash (DP) yondashuvi uchun, 0 dan target gacha bo'lgan
        #    joriy yig'indeni hosil qilish mumkinligini saqlaydigan boolean massiv yaratamiz.
        dp = [False] * (target + 1)
        dp[0] = True  # Hech qanday element tanlanmasa ham, yig'indi 0 ga teng (bazaviy holat).

        # 5. Massivdagi har bir element ustida ketma-ket ishlaymiz.
        for num in nums:
            # Qolgan yig'indiga qo'shilishi mumkinligini tekshirish uchun orqadan (target dan pastga)
            # iteratsiya qilamiz. Bu ikkinchi marta qo'shilishning oldini olish uchun.
            for j in range(target, num - 1, -1):
                # Agar j-num yig'indiga oldin yetib borish mumkin bo'lgan bo'lsa,
                # demak hozirgi num ni qo'shgandan so'ng j yig'indisi ham mumkin.
                dp[j] = dp[j] or dp[j - num]

        # 6. Oxirida, target yig'indisini hosil qilish mumkinligini bildiruvchi dp[target]
        #    qiymati bizga javob beradi.
        return dp[target]
