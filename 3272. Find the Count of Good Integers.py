class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Faktoriallarni oldindan hisoblash
        fact = [1] * (11)
        for i in range(1, 11):
            fact[i] = fact[i - 1] * i

        # Barcha n xonali palindromlarni yaratish
        palindromes = []
        if n == 1:
            palindromes = list(range(1, 10))
        else:
            if n % 2 == 0:
                half_len = n // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                for first_half in range(start, end):
                    s = str(first_half)
                    palindrome_str = s + s[::-1]
                    palindromes.append(int(palindrome_str))
            else:
                half_len = (n - 1) // 2
                start = 10 ** half_len
                end = 10 ** (half_len + 1)
                for first_part in range(start, end):
                    s = str(first_part)
                    first_half_part = s[:half_len]
                    middle = s[half_len]
                    palindrome_str = first_half_part + middle + first_half_part[::-1]
                    palindromes.append(int(palindrome_str))

        # K ga bo'linadigan palindromlarni va ularning raqam to'plamlarini olish
        multisets = set()
        for p in palindromes:
            if p % k != 0:
                continue
            counts = [0] * 10
            for c in str(p):
                counts[int(c)] += 1
            multisets.add(tuple(counts))

        # Har bir raqam to'plami uchun yaroqli sonlarni hisoblash
        total = 0
        for m in multisets:
            denominator = 1
            for count in m:
                denominator *= fact[count]
            count_0 = m[0]
            numerator = fact[n - 1] * (n - count_0)
            total += numerator // denominator

        return total