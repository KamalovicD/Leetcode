class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # 1. LCS ni hisoblash uchun DP (dinamik programming) jadvalini tayyorlaymiz.
        # dp[i][j] str1[0...i-1] va str2[0...j-1] ning eng uzun umumiy ketma-ketligidan iborat.
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    # Agar str1[i] va str2[j] teng bo'lmasa, uzunligi ko'proq bo'lgan LCS ni tanlaymiz:
                    if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                        dp[i + 1][j + 1] = dp[i + 1][j]
                    else:
                        dp[i + 1][j + 1] = dp[i][j + 1]

        # Endi dp[m][n] ni LCS deb olamiz.
        lcs = dp[m][n]

        # 2. LCS asosida javob (supersequence) ni yig'amiz.
        ans = []
        i, j = 0, 0
        # LCS dagi har bir belgi uchun, uning oldingilaridagi belgilarni qo'shamiz:
        for c in lcs:
            # str1 dan LCS dagi harfga yetguncha bo‘lgan barcha belgilarni qo‘shamiz.
            while str1[i] != c:
                ans.append(str1[i])
                i += 1
            # str2 dan LCS dagi harfga yetguncha bo‘lgan barcha belgilarni qo‘shamiz.
            while str2[j] != c:
                ans.append(str2[j])
                j += 1
            # Endi, LCS dagi umumiy harfni natijaga qo‘shamiz.
            ans.append(c)
            i += 1
            j += 1

        # Har ikkala satrda qolgan so‘nggi belgilarni qo‘shamiz.
        ans.append(str1[i:])
        ans.append(str2[j:])

        return "".join(ans)
