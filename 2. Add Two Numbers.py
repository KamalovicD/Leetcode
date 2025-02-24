class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val      # Tugundagi qiymat
         self.next = next    # Keyingi tugunga havola

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Natijani saqlash uchun bosh (dummy) tugun yaratamiz
        dummy = ListNode(0)
        current = dummy     # Yangi ro'yxatda harakatlanuvchi ko'rsatkich
        carry = 0           # Yodda qolgan qiymatni saqlaymiz

        # l1 yoki l2 tugunlari mavjud bo'lsa yoki yodda qolgan qiymat bo'lsa davom etamiz
        while l1 or l2 or carry:
            # l1 dan qiymat olamiz yoki 0 ga o'rnatamiz
            val1 = l1.val if l1 else 0
            # l2 dan qiymat olamiz yoki 0 ga o'rnatamiz
            val2 = l2.val if l2 else 0

            # Raqamlarni va yodda qolgan qiymatni qo'shamiz
            total = val1 + val2 + carry
            # Yodda qolgan qiymatni yangilaymiz
            carry = total // 10
            # Yangi tugun qiymatini aniqlaymiz
            new_val = total % 10

            # Yangi tugun yaratamiz va uni natija ro'yxatiga qo'shamiz
            current.next = ListNode(new_val)
            current = current.next  # Ko'rsatkichni yangilaymiz

            # l1 va l2 ko'rsatkichlarini yangilaymiz
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Natija ro'yxatini qaytaramiz (dummy tugundan keyin)
        return dummy.next
