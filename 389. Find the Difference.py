class Solution(object):
    def findTheDifference(self, s, t):
        """
        :param s: str
        :param t: str
        :return: str
        """
        s_sum = 0  # 's' satridagi harflarning ASCII qiymatlari yig'indisi
        t_sum = 0  # 't' satridagi harflarning ASCII qiymatlari yig'indisi

        for char in s:
            s_sum += ord(char)  # 's' satridagi harflarning ASCII qiymatlarini qo'shamiz

        for char in t:
            t_sum += ord(char)  # 't' satridagi harflarning ASCII qiymatlarini qo'shamiz

        diff = t_sum - s_sum  # 't' va 's' ASCII yig'indilarining farqi

        return chr(diff)  # Farqni harfga aylantirib qaytaramiz
