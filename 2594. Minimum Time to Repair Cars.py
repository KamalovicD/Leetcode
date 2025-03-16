from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # 1. Tekshiruvchi funksiya: "canRepair"
        # Berilgan t vaqt ichida barcha mexaniklar qancha mashinani ta’mirlay olishini hisoblaydi.
        # Agar jami mashina soni cars ga teng yoki katta bo‘lsa, bu vaqt yetarli ekanligini bildiradi.
        def canRepair(t: int) -> bool:
            total = 0  # barcha mexaniklar tomonidan ta’mirlanadigan mashinalar soni
            for r in ranks:
                # Har bir mexanik uchun:
                # r * n² <= t   (n – ta’mirlanadigan mashina soni)
                # Bu tenglamani yechish orqali, n <= sqrt(t / r) bo‘ladi.
                # Biz butun son qismidan foydalanamiz: maksimal n = floor(sqrt(t / r))
                total += int((t / r) ** 0.5)
                # Agar jami mashinalar soni allaqachon kerakli son cars ga yetgan bo‘lsa,
                # biz darhol True qaytaramiz.
                if total >= cars:
                    return True
            # Agar for sikli tugagan bo‘lsa va jami son cars ga yetmasa, False qaytaramiz.
            return total >= cars

        # 2. Binary search uchun qidiruv oralig‘i (time interval)
        # Pastki chegara: lo = 0 (nol vaqt)
        # Yuqori chegara: hi = max(ranks) * cars²
        # Sababi, eng sekin mexanik (eng katta rank) barcha mashinalarni ta’mirlash uchun eng ko‘p vaqt talab qiladi.
        lo = 0
        hi = max(ranks) * cars * cars  # Bu maksimal mumkin bo‘lgan vaqt
        answer = hi  # Javobni avval yuqori chegara sifatida belgilaymiz

        # 3. Binary search sikli: vaqt oralig‘ida t ni qidiramiz
        while lo <= hi:
            mid = (lo + hi) // 2  # Orta davrani tanlaymiz
            # Agar mid vaqt ichida barcha mashinalarni ta’mirlash mumkin bo‘lsa,
            # bu vaqt variant bo‘lib, endi yanada kichik vaqt topishga harakat qilamiz.
            if canRepair(mid):
                answer = mid
                hi = mid - 1  # yuqori chegara kamaytiramiz, chunki vaqtni kamaytirishga harakat qilamiz
            else:
                # Agar mid vaqt yetarli bo‘lmasa, pastki chegara oshiriladi.
                lo = mid + 1

        # 4. Minimal vaqt (answer) ni qaytaramiz
        return answer
