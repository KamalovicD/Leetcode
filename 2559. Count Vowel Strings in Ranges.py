from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        # "vowels" to'plami – bu bizga unli harflarni (a, e, i, o, u) sifatida tezkor tekshirish imkonini beradi.

        prefix = [0] * (len(words) + 1)
        # "prefix" degan massiv yaratildi. Uning uzunligi words uzunligidan 1 ta ortiq, chunki
        # prefix[0] = 0 bo‘ladi va shundan keyin har bir indeksda hozirgacha bo‘lgan to‘plam (yig‘indi) qiymat saqlanadi.

        for i, word in enumerate(words):
            # Har bir so'zni indekslar bo‘yicha ko‘rib chiqamiz.
            if word[0] in vowels and word[-1] in vowels:
                # Agar so'zning birinchi (word[0]) va oxirgi harfi (word[-1]) unli bo‘lsa,
                # shart bajariladi.
                prefix[i + 1] = prefix[i] + 1
                # Bu indeksga kelib, oldingi (prefix[i]) qiymatga 1 qo‘shamiz.
            else:
                prefix[i + 1] = prefix[i]
                # Agar so‘z shartni bajarmasa, to‘plam qiymati o‘zgarmaydi.

        ans = []
        # Natijalarni saqlash uchun bo'sh ro‘yxat

        for l, r in queries:
            # Har bir so‘rov uchun: [l, r] oralig‘idagi so‘zlar shartga javob beradimi degan savol.
            # Biz prefix yig'indidan foydalanamiz.
            # prefix[r+1] – prefix[l] bizga [l, r] oralig'idagi mos so‘zlar sonini beradi.
            ans.append(prefix[r + 1] - prefix[l])

        return ans
