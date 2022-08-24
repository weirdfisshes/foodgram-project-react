from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from djoser.views import UserViewSet

from .models import Follow, User
from .serializers import FollowSerializer
from recipes.pagination import CustomPageNumberPagination


class FollowViewSet(UserViewSet):
    """
    Вьюсет подписок.
    """
    pagination_class = CustomPageNumberPagination

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        serializer = FollowSerializer(
            data=request.data,
            context={'request': request, 'author': author}
        )
        serializer.is_valid(raise_exception=True)
        follow = Follow.objects.create(user=user, author=author)
        serializer = FollowSerializer(
            follow, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def unsubscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        serializer = FollowSerializer(
            data=request.data,
            context={'request': request, 'author': author}
        )
        serializer.is_valid(raise_exception=True)
        follow = Follow.objects.filter(user=user, author=author)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
