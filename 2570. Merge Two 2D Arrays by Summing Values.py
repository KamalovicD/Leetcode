from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Dictionary yordamida id -> sum qiymatlarini saqlaymiz.
        merged = {}

        # nums1 massividagi har bir [id, value] juftligini ko‘rib chiqamiz
        for id, value in nums1:
            # Agar id dictionaryda mavjud bo‘lsa, uning qiymatini yangilaymiz,
            # aks holda 0 qiymatini olamiz va keyin shu ikkiga value qo‘shamiz.
            merged[id] = merged.get(id, 0) + value

        # nums2 massividagi har bir [id, value] juftligini ko‘rib chiqamiz va qo‘shamiz.
        for id, value in nums2:
            merged[id] = merged.get(id, 0) + value

        # Hosil bo'lgan dictionary kalitlarini (id lar) o'sish tartibida tartiblaymiz
        # va natijaviy ro'yxatga [id, sum_value] juftliklarini qo'shamiz.
        result = []
        for id in sorted(merged.keys()):
            result.append([id, merged[id]])

        return result
