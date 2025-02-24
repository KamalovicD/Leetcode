class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. Agar 'needle' bo'sh satr bo'lsa, 0 qaytaramiz.
        if not needle:
            return 0

        # 2. 'haystack' va 'needle' uzunliklarini saqlaymiz.
        hay_len = len(haystack)
        needle_len = len(needle)

        # 3. 'haystack' ichida 'needle' qidiramiz.
        for i in range(hay_len - needle_len + 1):
            # 4. 'haystack' dan 'needle' uzunligicha bo'lak olamiz.
            substring = haystack[i:i+needle_len]
            # 5. Agar bo'lak 'needle' ga teng bo'lsa, indeksni qaytaramiz.
            if substring == needle:
                return i

        # 6. Agar 'needle' topilmasa, -1 qaytaramiz.
        return -1
