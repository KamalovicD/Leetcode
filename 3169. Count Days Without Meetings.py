from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 1-qadam: Uchrashuvlarni boshlanish sanasi bo‘yicha tartiblaymiz
        meetings.sort()

        # 2-qadam: Birlashgan uchrashuvlar ro‘yxatini hosil qilamiz
        merged_meetings = []
        for start, end in meetings:
            if merged_meetings and merged_meetings[-1][1] >= start:
                # Agar oldingi uchrashuv hozirgi uchrashuv bilan kesishsa, birlashtiramiz
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end)
            else:
                # Aks holda, yangi uchrashuv sifatida qo‘shamiz
                merged_meetings.append([start, end])

        # 3-qadam: Bo‘sh kunlarni hisoblash
        free_days = 0
        last_end = 0

        for start, end in merged_meetings:
            free_days += (start - last_end - 1)  # Oldingi uchrashuv tugaganidan keyingi bo‘sh kunlarni qo‘shamiz
            last_end = end  # Oxirgi band kunni yangilaymiz

        free_days += (days - last_end)  # Oxirgi uchrashuvdan keyin qolgan bo‘sh kunlarni qo‘shamiz
        return free_days
