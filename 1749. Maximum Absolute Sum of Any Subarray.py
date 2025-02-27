from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max_sum: Hozirgi eng katta kontig subarray yig'indisini saqlaydi.
        # Boshlang'ich qiymat 0, chunki bo'sh subarray yig'indisi ham 0.
        max_sum = 0

        # curr_max: Qadam-qadam har bir elementni qo'shgan holda,
        # shu nuqtada yakunlanadigan maksimal yig'indini hisoblaydi.
        curr_max = 0

        # min_sum: Hozirgi eng kichik (ya'ni, eng manfiy) kontig subarray yig'indisini saqlaydi.
        min_sum = 0

        # curr_min: Har bir elementni qo'shib borishda,
        # shu nuqtada yakunlanadigan minimal (eng kichik) yig'indini hisoblaydi.
        curr_min = 0

        # Massivdagi har bir element bo'ylab iteratsiya qilamiz.
        # Bu siklda biz nafaqat maksimal, balki minimal (eng salbiy) yig'indini ham hisoblaymiz.
        for num in nums:
            # Maksimal yig'indini yangilash:
            # Agar (hozirgi yig'indi + yangi element) yangi elementdan kattaroq bo'lsa,
            # demak, avvalgi qismni davom ettirish foydali.
            # Aks holda, yangi subarray boshlangan deb hisoblaymiz.
            curr_max = max(curr_max + num, num)

            # Hozirgacha uchragan maksimal yig'indini (max_sum) yangilanadi.
            max_sum = max(max_sum, curr_max)

            # Minimal yig'indini yangilash:
            # Bu yerda asosan yoqilgandek xuddi teskari logika:
            # Agar (hozirgi minimal yig'indi + num) soni kichikroq (ko'proq manfiy)
            # bo'lsa, davom ettiramiz, aks holda yangi boshlaymiz.
            curr_min = min(curr_min + num, num)

            # Eng kichik (eng salbiy) yig'indini saqlash.
            min_sum = min(min_sum, curr_min)

        # Javob: maksimal yig'indining o'zi yoki eng kichik yig'indining absolyut qiymati (ya'ni, -min_sum)
        return max(max_sum, abs(min_sum))
