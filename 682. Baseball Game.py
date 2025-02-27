from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 'record' ro'yxati o'yin davomida amal natijalarini (ballarni) saqlaydi.
        record = []

        # operations ro'yxatidagi har bir amal bo'yicha aylanamiz.
        for op in operations:
            if op == "C":
                # "C" - Oldingi qo'shilgan ballni bekor qiladi va record dan olib tashlaydi.
                record.pop()
            elif op == "D":
                # "D" - Oldingi ballning ikki baravarini hisoblab, yangi ball sifatida qo'shadi.
                record.append(record[-1] * 2)
            elif op == "+":
                # "+" - Oldingi ikki ballni yig'indisini hisoblab, yangi ball sifatida qo'shadi.
                record.append(record[-1] + record[-2])
            else:
                # Agar op raqam bo'lsa (masalan, "5", "-2" va hokazo),
                # uni butun songa o'zgartirib, record ga qo'shamiz.
                record.append(int(op))

        # Yakuniy natija – record dagi barcha ballarning yig'indisi qaytariladi.
        return sum(record)
