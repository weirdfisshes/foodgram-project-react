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
    pagination_class = CustomPageNumberPagination

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def subscribe(self, request, id=None):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            author = get_object_or_404(User, id=id)

        # if user == author:
        #     return Response({
        #         'errors': 'Вы не можете подписываться на самого себя'
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # if Follow.objects.filter(user=user, author=author).exists():
        #     return Response({
        #         'errors': 'Вы уже подписаны на данного пользователя'
        #     }, status=status.HTTP_400_BAD_REQUEST)

            follow = Follow.objects.create(user=user, author=author)
            serializer = FollowSerializer(
                follow, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @subscribe.mapping.delete
    def delete_subscribe(self, request, id=None):
        serializer = FollowSerializer(data=request.data)
        user = request.user
        author = get_object_or_404(User, id=id)
        if serializer.is_valid():
            user = request.user
            author = get_object_or_404(User, id=id)
        # if user == author:
        #     return Response({
        #         'errors': 'Вы не можете отписываться от самого себя'
        #     }, status=status.HTTP_400_BAD_REQUEST)
            follow = Follow.objects.filter(user=user, author=author)
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({
        #     'errors': 'Вы уже отписались'
        # }, status=status.HTTP_400_BAD_REQUEST)

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
