from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 1. Uchrashuvlarni boshlanish kuniga qarab saralash
        meetings.sort()

        # 2. Ishlash mumkin bo'lgan kunlar hisoblagichi
        available_days = 0

        # 3. Oxirgi band bo'lgan kunni saqlash
        last_meeting_end = 0

        # 4. Barcha uchrashuvlarni ko'rib chiqamiz
        for start, end in meetings:
            # Agar mavjud uchrashuv avvalgi uchrashuvdan keyin boshlansa, bo'sh kunlarni hisoblaymiz
            if start > last_meeting_end + 1:
                available_days += start - (last_meeting_end + 1)

            # Oxirgi uchrashuv tugagan kunni yangilaymiz
            last_meeting_end = max(last_meeting_end, end)

        # 5. Agar oxirgi uchrashuvdan keyin hali bo'sh kunlar bo'lsa, ularni hisoblaymiz
        if last_meeting_end < days:
            available_days += days - last_meeting_end

        return available_days
