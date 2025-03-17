class Solution:
    def intToRoman(self, num: int) -> str:
        # 1. Qiymatlar va ularning Rim raqamlari:
        #    Biz qiymatlarni katta→kichik tartibda joylashtiramiz,
        #    shunda eng katta qiymatdan boshlab, sonni bosqichma-bosqich kamaytiramiz.
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        # 2. Natija uchun bo'sh string yaratamiz
        result = ""

        # 3. Har bir qiymat bo‘yicha iteratsiyadan foydalanamiz:
        #    Agar num berilgan qiymatdan katta yoki teng bo‘lsa,
        #    shu Rim raqamini natijaga qo‘shamiz va num dan bu qiymatni ayiramiz.
        for i, value in enumerate(values):
            # Agar num ≥ value bo‘lsa, shu qiymatga mos Rim raqamini natijaga qo‘shamiz.
            while num >= value:
                result += romans[i]
                num -= value
                # Misol: num = 3749 bo'lsa, avvalo 1000 (M) ga qarab:
                # 3749 ≥ 1000 → result "M", num = 3749 - 1000 = 2749, yana "M", keyin 1749, yana "M", keyin 749
        # 4. Natijani qaytaramiz.
        return result
