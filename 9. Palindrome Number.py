class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Agar x manfiy bo‘lsa, uni palindrom deb hisoblamaymiz.
        # Masalan, -121: chapdan " -121 " o‘qiladi, o‘ngdan esa "121-" – ular bir xil emas.
        if x < 0:
            return False

        # 2. x ni string tarkibiga aylantiramiz.
        # Misol: 121 -> "121"
        s = str(x)

        # 3. s ning teskari variantini hosil qilamiz.
        # Python'da slicing [::-1] yordamida stringni teskari tartibda olish mumkin.
        # Misol: "121"[::-1] -> "121", "123"[::-1] -> "321"
        # 4. Agar s teskari holatdan ham o‘sha bo‘lsa, x palindromdir; aks holda, palindrom emas.
        return s == s[::-1]
