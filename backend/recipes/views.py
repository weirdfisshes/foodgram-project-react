from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import IngredientSearchFilter, RecipeFilter
from .models import (
    Favorite, Ingredient, Recipe,
    RecipeIngredients, ShoppingCart, Tag
)
from .pagination import CustomPageNumberPagination
from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import (
    FavoriteSerializer, IngredientSerializer, RecipeListSerializer,
    RecipeSerializer, ShoppingCartSerializer, TagSerializer
)


class TagViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет тегов.
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    permission_classes = (ReadOnly,)


class IngredientViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет ингридиентов.
    '''
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    permission_classes = (ReadOnly,)
    filter_backends = [IngredientSearchFilter]
    search_fields = ('^name',)


class RecipeViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет рецептов.
    '''
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializer
        return RecipeSerializer

    @staticmethod
    def post_method_for_actions(request, pk, serializers):
        data = {'user': request.user.id, 'recipe': pk}
        serializer = serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete_method_for_actions(request, pk, model):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        model_obj = get_object_or_404(model, user=user, recipe=recipe)
        model_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        return self.post_method_for_actions(
            request=request, pk=pk, serializers=FavoriteSerializer)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        return self.delete_method_for_actions(
            request=request, pk=pk, model=Favorite)

    @action(detail=True, methods=['POST'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk):
        return self.post_method_for_actions(
            request=request, pk=pk, serializers=ShoppingCartSerializer)

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk):
        return self.delete_method_for_actions(
            request=request, pk=pk, model=ShoppingCart)

    @action(detail=False, methods=['get'],
            permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        shopping_list = {}
        ingredients = RecipeIngredients.objects.filter(
            recipe__carts__user=request.user).values(
                'ingredient__name',
                'ingredient__measurement_unit'
        ).annotate(total=Sum('amount'))
        for ingredient in ingredients:
            amount = ingredient['total']
            name = ingredient['ingredient__name']
            measurement_unit = ingredient['ingredient__measurement_unit']
            shopping_list[name] = {
                'measurement_unit': measurement_unit,
                'amount': amount
            }
        main_list = ([f"{item}: {value['amount']}"
                      f" {value['measurement_unit']}\n"
                      for item, value in shopping_list.items()])
        response = HttpResponse(main_list, 'Content-Type: text/plain')
        response['Content-Disposition'] = 'attachment; filename="Cart.txt"'
        return response
