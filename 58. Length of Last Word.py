class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. Stringning boshidagi va oxiridagi ortiqcha bo'shliqlarni olib tashlaymiz.
        #    Bu qadam, agar string oxirida bo'shliq belgilar bo'lsa, ularni hisobga olmaslik uchun muhim.
        s = s.strip()

        # 2. Stringni bo'shliq belgilari bo'yicha bo'laklarga (so'zlarga) ajratamiz.
        #    Bu yerda split() metodi yordamida s stringini ajratamiz va natijada har bir so'zdan iborat ro'yxat hosil bo'ladi.
        words = s.split(" ")

        # 3. Bo'laklar ro'yxatining so'nggi elementini olamiz, chunki u oxirgi so'zni ifodalaydi.
        #    len() funksiyasi yordamida ushbu so'zning uzunligini aniqlab, qaytaramiz.
        return len(words[-1])
