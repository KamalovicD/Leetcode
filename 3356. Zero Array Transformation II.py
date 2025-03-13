from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)  # nums massivining uzunligi
        m = len(queries)  # queries massivining uzunligi

        # Bu yordamchi funksiya, berilgan prefix (ya'ni, birinchi k ta so'rov) yordamida
        # har bir indeksga qabul qilinishi mumkin bo'lgan maksimal kamaytirish miqdorini hisoblaydi.
        # Agar har bir indeks uchun bu maksimal miqdor nums[i] ga teng yoki katta bo'lsa,
        # unda shu prefix yetarli va funksiya True qaytaradi.
        def can_process(k: int) -> bool:
            # diff – farq (difference) massivi, uni range update (qator oraliq yangilash)
            # uchun ishlatamiz. Uni uzunligi n+1 ga teng (oxirgi chegarani ham belgilash uchun)
            diff = [0] * (n + 1)
            # Birinchi k ta query’ni qo‘shamiz:
            for i in range(k):
                l, r, val = queries[i]
                # [l, r] oraliqqa qiymat qo‘shish:
                diff[l] += val  # oraliq boshlanishi
                diff[r + 1] -= val  # oraliq tugashi (r+1 dan keyin elementlarga ta'sir qilmasligi uchun)

            # diff massividan haqiqiy "potentsial" masofani olish uchun prefix summadan foydalanamiz:
            current = 0
            for i in range(n):
                current += diff[i]
                # Agar har bir index uchun yig‘indimiz nums[i] dan kichik bo‘lsa,
                # demak shu indexni nolga yetkazish mumkin emas.
                if current < nums[i]:
                    return False
            return True

        # Endi ikkinchi bosqich:
        # Binary search yordamida, [0, m] oralig‘ida eng kichik k aniqlanmoqda,
        # shunda birinchi k ta query bajarilgandan so‘ng (optimal ravishda ajratilgan kamaytirish)
        # nums massivining barcha qiymatlari 0 ga teng bo‘ladi.

        low, high = 0, m
        while low < high:
            mid = (low + high) // 2
            # mid ta query yetarli bo‘lsa, yuqori chegarani qisqartiramiz, chunki
            # biz eng kichik k ni topmoqchimiz.
            if can_process(mid):
                high = mid
            else:
                low = mid + 1

        # Agar low qiymatida ham shart bajarilsa, demak biz minimal k ni topdik.
        # Aks holda, barcha query’larni qo‘llagan holda ham nolga yetkazish imkoni bo‘lmasa, -1 qaytaramiz.
        return low if low <= m and can_process(low) else -1
