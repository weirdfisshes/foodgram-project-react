from django.contrib import admin

from .models import Ingredient, Recipe, Tag


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'quantity', 'unit') 
    search_fields = ('name',) 
    empty_value_display = '-пусто-'

class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug') 
    search_fields = ('name',) 
    empty_value_display = '-пусто-' 

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'text') 
    search_fields = ('name',) 
    empty_value_display = '-пусто-' 

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin) 