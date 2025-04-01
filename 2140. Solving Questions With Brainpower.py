from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Savollar ro'yxatidagi savollar sonini hisoblaymiz.
        n = len(questions)

        # dp massivini yaratamiz. dp[i] — i-savoldan boshlab erishishimiz mumkin bo'lgan eng yuqori ball.
        # Bizga oxirgi savoldan keyin hech qanday ball yo‘q ekanligini ko‘rsatish uchun qo‘shimcha element qo‘shamiz.
        dp = [0] * (n + 1)

        # Savollarni orqadan, ya'ni oxirgi savoldan 0-indeksgacha ko'rib chiqamiz.
        for i in range(n - 1, -1, -1):
            # Hozirgi savolning ball va brainpower (yo'q qila oladigan navbatdagi savollar soni) qiymatlarini ajratamiz.
            points, brainpower = questions[i]

            # Agar hozirgi savolni yechsak, keyingi yecha oladigan savol indeksi:
            # i + brainpower + 1. Shu orqali hozirgi savolni yechish qachon keyingi savolga o'tishimizni ko'rsatadi.
            next_index = i + brainpower + 1

            # Agar hozirgi savolni yechsak, olamiz:
            # - hozirgi savol uchun points
            # - va agar next_index mavjud bo'lsa (indeks chetidan chiqmasa) dp[next_index] qiymatini.
            solve = points + (dp[next_index] if next_index < len(dp) else 0)

            # Agar savolni o'tkazsak, toʻgʻridan-toʻgʻri keyingi savolga o'tamiz va u yerdan maksimal ballni olamiz.
            skip = dp[i + 1]

            # Ushbu qadamda, savolni yechish yoki o'tkazish variantlaridan eng yuqori ball beradiganini tanlaymiz.
            dp[i] = max(solve, skip)

        # Natijada, birinchi savoldan boshlab ololadigan maksimal ballni qaytaramiz.
        return dp[0]
