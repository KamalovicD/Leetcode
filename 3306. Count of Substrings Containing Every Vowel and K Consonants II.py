from collections import defaultdict
import bisect

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # 1. Satr uzunligini n ga tenglaymiz.
        n = len(word)

        # 2. Unli harflarni to'plamini belgilaymiz.
        vowels = set('aeiou')

        # 3. precon massivini tuzamiz: precon[i] - satrning [0, i) oraliqda nechta undosh mavjud.
        precon = [0] * (n + 1)
        for i in range(n):
            # Agar word[i] undosh bo'lsa (ya'ni vokalga kirmasa), precon qiymatini 1 ga oshiramiz.
            precon[i + 1] = precon[i] + (0 if word[i] in vowels else 1)

        # 4. precon massividagi har bir qiymatga mos keluvchi indekslarni saqlaymiz.
        # Bu bizga keyinchalik, berilgan precon qiymati bor indekslarni binary search orqali topishga yordam beradi.
        pos_dict = defaultdict(list)
        for i, val in enumerate(precon):
            pos_dict[val].append(i)

        # 5. Unlilar uchun so'nggi uchrashuv indekslarini saqlovchi lug'atni boshlang.
        last_occurrence = {v: -1 for v in vowels}

        # 6. Natija uchun umumiy substringlar sonini saqlash uchun o'zgaruvchi.
        result = 0

        # 7. Satrni chapdan o'ngga aylantiramiz. r indeks sifatida substring tugashi sifatida qaraladi.
        for r, ch in enumerate(word):
            # Agar hozirgi harf unli bo'lsa, uning so'nggi uchrashuv indeksini yangilaymiz.
            if ch in vowels:
                last_occurrence[ch] = r

            # Agar [0, r] oralig'ida barcha unli uchramagan bo'lsa, vowel sharti qanoatlantirilmaydi.
            if any(last_occurrence[v] == -1 for v in vowels):
                continue  # Bu r uchun yechim mavjud emas, keyingi harfga o'tamiz.

            # 8. Hozirgi [0, r] dan so'nggi uchrashuvlar asosida, substring [L, r] da barcha unli borligi uchun
            # L indekslari uchun cheklov: L <= m, bu yerda m = eng kichik (min) so'nggi uchrashuv indeksi.
            m = min(last_occurrence[v] for v in vowels)

            # 9. Endi, [L, r] da aniq k ta undosh bo'lishi sharti:
            # precon[r+1] - precon[L] = k  => precon[L] = precon[r+1] - k.
            target = precon[r + 1] - k

            # 10. pos_dict dan target qiymatga ega bo'lgan indekslar ro'yhatini olamiz,
            # ularning orasida L <= m bo'lishi shartini binary search yordamida topamiz.
            # bisect_right ro'yhatda m dan kichik yoki teng indekslar sonini beradi.
            countL = bisect.bisect_right(pos_dict[target], m)

            # 11. Topilgan countL sonini umumiy natijaga qo'shamiz.
            result += countL

        # 12. Umumiy valid substringlar sonini qaytaramiz.
        return result
