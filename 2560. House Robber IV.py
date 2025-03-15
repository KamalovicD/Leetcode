from  typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # 1. Qidiruv doirasini aniqlaymiz:
        #    - Pastki chegaramiz (lo) eng kichik uy ichida bo‘lgan pul miqdori.
        #    - Yuqori chegaramiz (hi) esa eng katta uy ichidagi pul miqdori.
        lo, hi = min(nums), max(nums)

        # 2. Tekshiruvchi funksiya: berilgan "cap" (qobiliyat / capability) bilan,
        #    biz tanlab olinadigan uylardan kamida k ta tanlash mumkinmi?
        #    Qoidamiz: Rob adjacent bo‘lmagan uylardan pul o‘g‘irlaydi va faqat
        #    pul miqdori cap (yaʼni, "capability") yoki undan kam bo‘lgan uylardan tanlaydi.
        def canRob(cap):
            count = 0  # tanlangan uylardagi son
            i = 0  # massiv indeksini yuritamiz
            while i < len(nums):
                # Agar uydagi pul miqdori "cap" ga teng yoki kichik bo‘lsa,
                # demak bu uyni tanlamiz va keyingi qo‘shni uyga o‘tkazib yuboramiz.
                if nums[i] <= cap:
                    count += 1
                    i += 2  # Tanlangani uchun keyingi qo‘shni uyga o'tmaslik uchun 2 indeksni oshiramiz.
                else:
                    i += 1  # Aks holda uyni o'tamiz va faqat indexni 1 ga oshiramiz.
            # Agar tanlash imkoni bor uylardan soni k ga teng yoki ko‘p bo‘lsa, qaytaramiz.
            return count >= k

        # 3. Binary Search:
        #    Maqsadimiz, imkoniyati eng kichik (ya’ni minimal "capability") qiymatini topish.
        ans = hi  # Javobni yuqori chegaradan boshlaymiz.
        while lo <= hi:
            mid = (lo + hi) // 2  # "capability" ni taxminiy qiymati.
            # Agar mid qiymat bilan k ta yoki undan ko'proq uyni tanlash mumkin bo'lsa,
            # demak bu qiymat variant bo'lib, biz yanada kichikroq (kamroq pul talab qiluvchi)
            # variantni qidirishni davom ettiramiz.
            if canRob(mid):
                ans = mid
                hi = mid - 1
            else:
                # Aks holda, bu qiymat yetarli emas va biz qidiruvni yuqoriga yo'naltiramiz.
                lo = mid + 1

        return ans
