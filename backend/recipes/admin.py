from django.contrib import admin

from .models import (
    Favorite, Ingredient, Recipe,
    RecipeIngredients, ShoppingCart, Tag
)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'amount_favorites',
                    'amount_tags', 'amount_ingredients')
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)
    empty_value_display = '-empty-'

    @staticmethod
    def amount_favorites(obj):
        return obj.favorites.count()
    amount_favorites.short_description = 'Всего избранных: '

    @staticmethod
    def amount_tags(obj):
        return '\n'.join([i[0] for i in obj.tags.values_list('name')])
    amount_tags.short_description = 'Всего тегов: '

    @staticmethod
    def amount_ingredients(obj):
        return '\n'.join([i[0] for i in obj.ingredients.values_list('name')])
    amount_ingredients.short_description = 'Всего ингредиентов: '


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-empty-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(RecipeIngredients)
class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    empty_value_display = '-empty-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-empty-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-empty-'
