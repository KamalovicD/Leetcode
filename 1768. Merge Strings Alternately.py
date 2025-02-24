class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :param word1: Birinchi satr (str)
        :param word2: Ikkinchi satr (str)
        :return: Birlashtirilgan satr (str)
        """
        result = ""  # Natijaviy satrni saqlash uchun bo'sh satr yaratamiz
        i, j = 0, 0  # word1 va word2 satrlari uchun indekslarni belgilaymiz

        # Har ikkala satrning oxiriga yetmaguncha davom etuvchi sikl
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]  # word1 ning i-indeksdagi harfini natijaga qo'shamiz
                i += 1  # Indeksni 1 ga oshirib, keyingi harfga o'tamiz
            if j < len(word2):
                result += word2[j]  # word2 ning j-indeksdagi harfini natijaga qo'shamiz
                j += 1  # Indeksni 1 ga oshirib, keyingi harfga o'tamiz

        return result  # Birlashtirilgan satrni qaytaramiz
