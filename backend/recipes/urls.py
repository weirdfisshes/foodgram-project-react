
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = 'recipes'

api_router = DefaultRouter()
api_router.register(r'recipes', RecipeViewSet, basename='recipes')
api_router.register(r'tags', TagViewSet, basename='tags')
api_router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path(r'', include(api_router.urls)),
]
