from typing import List
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 1. ingredients_mapping: ingredient => retseptlar ro'yxati
        #    retsept_ing_count: har bir retsept uchun yetishmagan ingredientlar soni
        ingredient_to_recipe = defaultdict(list)
        recipe_ing_count = {}

        # Har bir retsept uchun ingredientlar sonini saqlaymiz.
        for i, recipe in enumerate(recipes):
            recipe_ing_count[recipe] = len(ingredients[i])
            # Har bir ingredient uchun, bu retseptni ro'yxatga qo'shamiz.
            for ing in ingredients[i]:
                ingredient_to_recipe[ing].append(recipe)

        # 2. Boshlang'ich supplies ni queue ga joylashtiramiz.
        queue = deque(supplies)
        # Natija ro'yxati: tayyor bo'lishi mumkin retseptlar
        result = []

        # 3. BFS usuli yordamida, queue ichidagi ingredientlar orqali retsept prerequisites ni kamaytiramiz.
        while queue:
            cur = queue.popleft()
            # "cur" ingredienti asosida, qaysi retseptlar talab qilinishini tekshiramiz:
            for recipe in ingredient_to_recipe[cur]:
                # Ushbu ingredient retsept talablariga mos keldi: prerequisites sonini kamaytiramiz.
                recipe_ing_count[recipe] -= 1
                # Agar prerequisites soni nolga tushsa, hisoblaymizki, bu retseptni tayyorlash mumkin.
                if recipe_ing_count[recipe] == 0:
                    result.append(recipe)  # retsept yaratildi
                    queue.append(recipe)  # bu retsept endi ingredient sifatida qo'shiladi
        # 4. Natijada, tayyor mumkin retseptlar ro'yxatini qaytaramiz.
        return result
