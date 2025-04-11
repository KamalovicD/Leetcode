class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0  # Simmetrik sonlar sonini hisoblash uchun
        for num in range(low, high + 1):  # low dan high gacha sonlarni aylanamiz
            s = str(num)  # Sonni stringga aylantiramiz
            n = len(s)  # Raqamlar sonini topamiz
            if n % 2 == 0:  # Agar raqamlar soni juft bo‘lsa
                half = n // 2  # Yarmiga bo‘lamiz
                first_half_sum = sum(int(digit) for digit in s[:half])  # Birinchi yarmi yig‘indisi
                second_half_sum = sum(int(digit) for digit in s[half:])  # Ikkinchi yarmi yig‘indisi
                if first_half_sum == second_half_sum:  # Agar yig‘indilar teng bo‘lsa
                    count += 1  # Simmetrik sonlar sonini oshiramiz
        return count  # Natijani qaytaramiz