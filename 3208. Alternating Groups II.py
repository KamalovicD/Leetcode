from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        diff = [1 if colors[i] != colors[(i + 1) % n] else 0 for i in range(n)]

        extended_diff = diff + diff

        count = 0

        current_sum = sum(extended_diff[:k - 1])

        if current_sum == k - 1:
            count += 1

        for i in range(1, n):

            current_sum = current_sum - extended_diff[i - 1] + extended_diff[i + k - 2]

            if current_sum == k - 1:
                count += 1

        return count
