from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Dastlab, ikkala massiv orasida kichigini nums1 deb qabul qilamiz.
        # Shunday qilib, binary search jarayonida kichikroq massiv bo‘yicha qidiruv olib boriladi.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # m - nums1 uzunligi, n - nums2 uzunligi.
        m, n = len(nums1), len(nums2)

        # Binary search uchun boshlang‘ich chegaralar.
        low, high = 0, m

        # Massivlar yig‘indisidagi yarmiy nuqtani (half point) topamiz.
        # Agar jami elementlar soni juft bo‘lsa, chap bo‘limda jami (m+n)//2 ta element bo‘ladi.
        # Agar toq bo‘lsa, chap bo‘limda (m+n+1)//2 ta element bo‘ladi.
        half = (m + n + 1) // 2

        # Binary search yordamida nums1 massivida bo‘linish nuqtasini (partition) topamiz.
        while low <= high:
            # i - nums1 uchun bo‘linish indeksi.
            i = (low + high) // 2
            # nums2 uchun bo‘linish indeksi shunday aniqlanadiki:
            # chap bo‘limdagi jami elementlar soni half ga teng bo‘lsin.
            j = half - i

            # nums1 ning chap bo‘limidagi eng o‘ng elementini aniqlaymiz:
            # Agar i == 0 bo‘lsa, demak chap bo‘lim bo‘sh, shuning uchun -infinity (cheksiz kichik) qiymat olamiz.
            leftA = nums1[i - 1] if i != 0 else float('-inf')
            # nums1 ning o‘ng bo‘limidagi birinchi elementini aniqlaymiz:
            # Agar i == m bo‘lsa, demak o‘ng bo‘lim bo‘sh, shuning uchun infinity (cheksiz katta) qiymat olamiz.
            rightA = nums1[i] if i != m else float('inf')

            # Xuddi shu tarzda, nums2 uchun chap va o‘ng bo‘lim chegaralarini aniqlaymiz.
            leftB = nums2[j - 1] if j != 0 else float('-inf')
            rightB = nums2[j] if j != n else float('inf')

            # Hozir, to‘g‘ri bo‘linish shartini tekshiramiz:
            # Fenomen: chap bo‘limning eng katta elementi (leftA va leftB)
            # o‘ng bo‘limning eng kichik elementlaridan (rightA va rightB) kichik yoki teng bo‘lishi kerak.
            if leftA <= rightB and leftB <= rightA:
                # Agar jami elementlar soni juft bo‘lsa, median o‘ng va chap bo‘limning chegaralari o‘rtasidagi arifmetik o‘rtacha:
                if (m + n) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                else:
                    # Agar jami elementlar soni toq bo‘lsa, median – chap bo‘limdagi maksimal element.
                    return max(leftA, leftB)
            elif leftA > rightB:
                # Agar nums1 ning chap bo‘limidagi element (leftA) nums2 ning o‘ng bo‘limidagi element (rightB)
                # dan katta bo‘lsa, nums1 bo‘yicha bo‘linish nuqtasini chapga (kichik indekslarga) siljitamiz.
                high = i - 1
            else:
                # Aks holda, nums1 bo‘yicha bo‘linish nuqtasini o‘ngga (katta indekslarga) siljitamiz.
                low = i + 1

        # Agar bo‘linish nuqtasi aniqlanmasa, hech qanday yechim topilmagan deb qaytaramiz (amaldagi masalada bunday holat yuz bermaydi).
        raise ValueError("Input arrays are not valid.")
