class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Griddagi barcha elementlarni bitta bir o'lchovli ro'yxatga (listga) o'tkazamiz.
        nums = [num for row in grid for num in row]

        # 2. Har bir element uchun x boʻyicha modul (qoldiq) tekshiramiz.
        # Agar gridning birinchi elementining x bo'yicha qoldig'i boshqalarga qaraganda farq qilsa,
        # unda ularni bir xil qiymatga keltirish imkonsiz, shuning uchun -1 qaytaramiz.
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        # 3. Optimal operatsiyalar sonini aniqlash uchun, avvalo ro'yxatni kichikdan kattaga qarab tartiblaymiz.
        nums.sort()

        # 4. Barcha elementlar orasida yig'indini minimal qilish uchun median (o'rta qiymat)
        # tanlanadi. Median o'rtacha masofani minimallashtiradi.
        median = nums[len(nums) // 2]

        # 5. Har bir element median qiymatdan qancha masofada ekanligini aniqlaymiz.
        # Har bir operatsiyada x qo'shimcha yoki ayirish mumkin, shuning uchun
        # |num - median| ni x ga bo'lib, jami necha operatsiya kerakligini hisoblaymiz.
        operations = sum(abs(num - median) // x for num in nums)
        return operations
