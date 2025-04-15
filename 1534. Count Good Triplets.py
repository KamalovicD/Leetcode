class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0  # Yaxshi tripletlar sonini hisoblaydi
        n = len(arr)  # Massivning uzunligi

        # Uchta sikl bilan barcha tripletlarni tekshiramiz
        for i in range(n - 2):  # Birinchi raqam uchun
            for j in range(i + 1, n - 1):  # Ikkinchi raqam uchun
                for k in range(j + 1, n):  # Uchinchi raqam uchun
                    # Shartlarni tekshiramiz
                    if (abs(arr[i] - arr[j]) <= a and
                            abs(arr[j] - arr[k]) <= b and
                            abs(arr[i] - arr[k]) <= c):
                        count += 1  # Yaxshi triplet topsak, hisobni oshiramiz

        return count  # Natijani qaytaramiz