# Binary daraxt tuguni uchun aniqlovchi kod (odatda LeetCode platformasida allaqachon berilgan)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS yordamida (postorder traversal) har bir tugun uchun
        # (umumiy ajdod, chuqurlik) juftligini qaytaruvchi yordamchi funksiya
        def dfs(node: Optional[TreeNode]) -> (Optional[TreeNode], int):
            # Agar tugun bo'lmasa, hech narsa (None) qaytaramiz va chuqurlik 0 deb belgilaymiz.
            if not node:
                return (None, 0)

            # Chap bolaga DFS ni chaqiramiz va chap subtree ichida to'plangan LCA va chuqurlikni olamiz.
            left_lca, left_depth = dfs(node.left)
            # O'ng bolaga DFS ni chaqiramiz va o'ng subtree ichida to'plangan LCA va chuqurlikni olamiz.
            right_lca, right_depth = dfs(node.right)

            # Agar chap va o'ng tomonlar teng chuqurlikka ega bo'lsa,
            # demak, eng chuqur barglar ikkala tomon ham bor va hozirgi tugun ularning umumiy ajdodi hisoblanadi.
            if left_depth == right_depth:
                return (node, left_depth + 1)
            # Agar chap tomon o'ng tomondan chuqurroq bo'lsa, chap subtree ichidagi ajdodni qaytaramiz.
            elif left_depth > right_depth:
                return (left_lca, left_depth + 1)
            # Aks holda, o'ng tomon chuqurroq bo'lsa, o'ng subtree ichidagi ajdodni qaytaramiz.
            else:
                return (right_lca, right_depth + 1)

        # DFS ni ildiz tugundan boshlaymiz va qaytgan juftlikdan faqat LCA tugunni olamiz.
        return dfs(root)[0]
