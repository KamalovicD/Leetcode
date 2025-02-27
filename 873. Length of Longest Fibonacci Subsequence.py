from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Ikkinchi ma'lumotlar tuzilishini yaratamiz: 'index_map' - bu lug'at (dictionary),
        # unda kalit sifatida arr ro'yxatidagi har bir elementning qiymati,
        # va qiymat sifatida uning indeksi saqlanadi.
        index_map = {x: i for i, x in enumerate(arr)}

        # Dinamik dasturlash (DP) jadvalini yaratamiz.
        # dp[i][j] - (i, j) indekslaridagi elementlar oxirgi ikkilamchi elementlar bo'lgan
        # Fibonacci-like ketma-ketlikning uzunligini ifodalaydi.
        n = len(arr)
        dp = [[2] * n for _ in range(n)]

        # Fibonacci-like ketma-ketlikning maksimal uzunligini saqlaymiz.
        max_len = 0

        # arr ro'yxatidagi har bir i va j indekslari bo'yicha aylanamiz.
        for k in range(n):
            for j in range(k):
                # arr[i] va arr[j] dan oldin keladigan element arr[i] = arr[k] - arr[j]
                # qiymatini hisoblaymiz.
                i = index_map.get(arr[k] - arr[j])
                # Agar i mavjud bo'lsa va i < j bo'lsa,
                if i is not None and i < j:
                    # dp[j][k] ni yangilaymiz: dp[j][k] = dp[i][j] + 1
                    dp[j][k] = dp[i][j] + 1
                    # max_len ni yangilaymiz: hozirgi dp[j][k] qiymatidan eng kattasini olamiz.
                    max_len = max(max_len, dp[j][k])

        # Agar Fibonacci-like ketma-ketlik topilmasa, 0 qaytariladi.
        return max_len if max_len >= 3 else 0
