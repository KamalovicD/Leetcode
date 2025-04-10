class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # 1. s uzunligini olamiz, B = 10^(len(s)), va t = int(s).
        L = len(s)
        B = 10 ** L
        t = int(s)

        # 2. Agar finish < t bo'lsa, x = p*B + t hech qachon finish gacha yetmaydi.
        if finish < t:
            return 0

        # 3. x ∈ [start, finish] sharti: start ≤ p*B + t ≤ finish.
        #    Agar start ≤ t, p_min = 0, aks holda p_min = ceil((start - t)/B)
        if start <= t:
            p_min = 0
        else:
            p_min = (start - t + B - 1) // B  # Yuqoriga qarab butun qismini olish (ceiling)
        p_max = (finish - t) // B

        # Agar p_min > p_max bo'lsa, oraliqda mos son mavjud emas.
        if p_min > p_max:
            return 0

        # 4. [0, n] oralig‘ida, faqat allowed raqamlar (0..limit) ishlatilgan sonlarni hisoblaydigan
        #    "digit DP" usuli yordamida funksiya yaratamiz.
        def count_valid(n: int) -> int:
            # n ga qadar bo'lgan, faqat ruxsat etilgan (0..limit) raqamlar ishlatilgan sonlarning soni.
            sN = str(n)
            L_N = len(sN)
            from functools import lru_cache

            @lru_cache(maxsize=None)
            def dp(pos: int, tight: bool, lead: bool) -> int:
                # Agar barcha raqam joylashtirildi, bitta to'g'ri son topildi.
                if pos == L_N:
                    return 1
                res = 0
                # tight bo'lsa, joriy pozitsiyada yuqori chegara int(sN[pos]); aks holda, maksimal allowed raqam – limit.
                upper = int(sN[pos]) if tight else limit
                # Endi, ruxsat etilgan raqamlar 0 dan upper (ammo upper qisman ham limit bilan cheklanadi).
                for dig in range(0, min(limit, upper) + 1):
                    new_tight = tight and (dig == upper)
                    new_lead = lead and (dig == 0)
                    res += dp(pos + 1, new_tight, new_lead)
                return res

            return dp(0, True, True)

        # 5. [0, p_max] oralig'idagi valid sonlarni hisoblaymiz.
        valid_up_to_p_max = count_valid(p_max)
        # Agar p_min > 0, [0, p_min-1] oralig'idagi valid sonlarni ham hisoblaymiz.
        valid_up_to_p_min_minus = count_valid(p_min - 1) if p_min > 0 else 0

        valid_count = valid_up_to_p_max - valid_up_to_p_min_minus
        return valid_count
