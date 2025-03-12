from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 1. Quyidagi qator nums roʻyxatida 0 yoki undan katta birinchi element indeksini qaytaradi.
        #    Array tartiblanganligi sababli, shu indeksga qadar (chap tomondagi) barcha elementlar manfiy bo‘ladi.
        neg_count = bisect_left(nums, 0)

        # 2. Bu qator esa nums roʻyxatidagi 0 qiymatining oxirgi mavjud joylashuvi (ya'ni,
        #    0 dan kattalarni boshlash indeksi) ni topadi. Shu indekstdan oxirigacha bo‘lgan elementlar
        #    musbat sonlardir. Uning farqi ro'yhat uzunligidan olib, musbatlar sonini hisoblaymiz.
        pos_count = len(nums) - bisect_right(nums, 0)

        # 3. Natijada, musbat va manfiy sonlar sonidan kattasini qaytaramiz.
        return max(neg_count, pos_count)
