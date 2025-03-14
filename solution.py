import unittest


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # 1. n sonini satr shaklida saqlaymiz va uning xonalar (raqamlar) sonini aniqlaymiz.
        s = str(n)
        m = len(s)  # masalan, n = 1000 bo'lsa, m = 4

        # 2. Takrorlanmas raqamlardan tashkil topgan sonlarni hisoblash uchun accumulator (unique_count)
        unique_count = 0

        # 3. 1–m-1 xonali sonlar uchun:
        # Masalan, agar m = 4 bo'lsa, 1-xonali, 2-xonali va 3-xonali sonlarda takrorlanmas raqamli kombinatsiyalarni qo'shamiz.
        for i in range(1, m):
            count_for_length = 9  # Birinchi raqam uchun: 1..9 (0 ruxsat etilmaydi)
            for j in range(1, i):
                count_for_length *= (10 - j)
            unique_count += count_for_length

        # 4. Endi n bilan xuddi bir xil xonalikka ega sonlar uchun kombinatsiyalarni hisoblaymiz.
        seen = set()  # Oldin tanlangan raqamlar
        for i, ch in enumerate(s):
            digit = int(ch)
            # Agar i==0 bo'lsa, bosh raqamda 0raqam ruxsat etilmaydi, shuning uchun boshlanish qiymati 1
            start = 0 if i > 0 else 1
            for d in range(start, digit):
                if d in seen:
                    # Agar raqam ilgari tanlangan bo'lsa, bu kombinatsiyani o'tkazamiz.
                    continue
                available = 10 - (i + 1)  # Qolgan xonalar uchun mavjud bo'lgan raqamlar soni
                ways = 1
                for k in range(m - i - 1):
                    ways *= (available - k)
                unique_count += ways

            # Agar hozirgi raqam allaqachon tanlangan bo'lsa, kombinatsiyalarini davom ettirish mumkin emas.
            if digit in seen:
                break
            seen.add(digit)

            # Agar butun raqamlar unikal bo'lsa, n jahldan ham kombinatsiyaga qo'shiladi.
            if i == m - 1:
                unique_count += 1

        # 5. [1, n] oralig'idagi sonlar sonidan, takrorlanmas raqamlardan tashkil topgan sonlarni ayiramiz.
        return n - unique_count


# Quyidagi qismda biz testlarimizni yozamiz.
class TestSolution(unittest.TestCase):
    def setUp(self):
        # Har bir testdan oldin Solution klassidan obyekt yaratiladi.
        self.solution = Solution()

    def test_example1(self):
        n = 20
        expected = 1  # [1,20] oralig'idagi yagona takroriy raqamli son: 11
        result = self.solution.numDupDigitsAtMostN(n)
        self.assertEqual(result, expected)

    def test_example2(self):
        n = 100
        expected = 10  # Misol: 11, 22, 33, 44, 55, 66, 77, 88, 99, va 100
        result = self.solution.numDupDigitsAtMostN(n)
        self.assertEqual(result, expected)

    def test_example3(self):
        n = 1000
        expected = 262
        result = self.solution.numDupDigitsAtMostN(n)
        self.assertEqual(result, expected)


# Bu kod blokini to'g'ri ishga tushirish uchun __main__ bo'limidan foydalanamiz.
if __name__ == '__main__':
    unittest.main()
