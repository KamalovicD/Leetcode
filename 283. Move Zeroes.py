class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 1. Nol bo'lmagan elementlarning joylashtiriladigan indeksini saqlaydigan ko'rsatkich
        last_non_zero = 0

        # 2. Massivni boshidan oxirigacha aylantiramiz
        for current in range(len(nums)):
            # 3. Agar hozirgi element nolga teng bo'lmasa
            if nums[current] != 0:
                # 4. Hozirgi elementni last_non_zero indeksiga yozamiz
                nums[last_non_zero] = nums[current]
                # 5. Agar last_non_zero va current farqli bo'lsa, current indeksiga 0 yozamiz
                if last_non_zero != current:
                    nums[current] = 0
                # 6. last_non_zero ni 1 ga oshiramiz
                last_non_zero += 1
