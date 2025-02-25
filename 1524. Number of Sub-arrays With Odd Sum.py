from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Modul qiymati: javob juda katta bo'lishi mumkinligi sababli, natijani mod 10^9 + 7 ga olishimiz kerak.
        mod = 10 ** 9 + 7

        # Boshlang‘ich holatda prefix yig'indisi 0 ni hisobga olamiz, chunki summaning boshlang‘ich qiymati 0
        # bu juft (even) hisoblanadi.
        count_even = 1  # prefix yig'indilari orasida juft bo'lganlar (0 ham shu yerda inobatga olinadi)
        count_odd = 0  # prefix yig'indilari orasida toq bo'lganlar

        # Bu o'zgaruvchi hozirgi prefix yig'indining (sumaning) paritetini saqlaydi (faqat mod 2 qiymati, ya'ni 0 yoki 1)
        prefix = 0

        # Natijada topilgan odd subarraylar soni
        result = 0

        # Massivdagi har bir element uchun iteratsiya qilamiz
        for num in arr:
            # Hozirgi element qo'shilganda yangi prefix yig'indisini hosil qilamiz
            prefix += num

            # Faqat paritetni (juft yoki toq ekanligini) bilish yetarli bo‘lgani uchun,
            # prefix ni 2 ga bo‘lib qoldig'ini olamiz.
            prefix %= 2

            # Agar hozirgi prefix yig'indisi juft bo'lsa (prefix == 0)
            if prefix == 0:
                # Unda subarrayning yig'indisi odd bo'lishi uchun, oldin toq bo'lgan prefixlar (count_odd)
                # orasidan tanlashimiz kerak.
                result += count_odd
                # Shuningdek hozirgi juft prefix ni count_even ga qo'shamiz.
                count_even += 1
            else:
                # Agar prefix yig'indisi toq bo'lsa (prefix == 1)
                # Subarray odd bo'lishi uchun, oldin juft bo'lgan prefixlar (count_even) dan foydalanamiz.
                result += count_even
                # Keyin, count_odd ga toq prefixlar sonini yangilaymiz.
                count_odd += 1

            # Har bir iteratsiyadan keyin natijani mod operatsiyasi bilan kamaytiramiz,
            # chunki javob juda katta bo'lishi mumkin.
            result %= mod

        # Hisoblangan odd subarraylar sonini qaytaramiz.
        return result
