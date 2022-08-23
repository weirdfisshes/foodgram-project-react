from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = 'recipes'

api_router = DefaultRouter()
api_router.register('recipes', RecipeViewSet, basename='recipes')
api_router.register('tags', TagViewSet, basename='tags')
api_router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(api_router.urls)),
]
