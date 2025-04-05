from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0  # Natijada yig'iladigan XOR qiymatlarini qo'shish uchun ombor (accumulator)
        n = len(nums)  # Massivda nechta element borligini aniqlaymiz

        # DFS (chuqurga qarab qidirish) orqali barcha kichik to'plamlarni (subset) ko'rib chiqamiz.
        def dfs(index: int, current_xor: int):
            nonlocal total_sum  # Ichki funksiya tashqaridagi total_sum ga kirish uchun
            # Agar biz massivning so'ngiga yetgan bo'lsak, ya'ni har bir element ustida qaror qabul qilgan bo'lsak,
            # current_xor - hozirgi kichik to'plamning XOR yig'indisidir. Uni jami natijaga qo'shamiz.
            if index == n:
                total_sum += current_xor
                return

            # Option 1: Hozirgi elementni tanlamaymiz
            dfs(index + 1, current_xor)

            # Option 2: Hozirgi elementni tanlaymiz va current_xor ga uning XOR ni qo'shamiz.
            dfs(index + 1, current_xor ^ nums[index])

        # DFS ni 0-indeks va boshlang'ich XOR qiymati 0 bilan boshlaymiz.
        dfs(0, 0)
        return total_sum
