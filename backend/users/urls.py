from django.urls import include, path

from .views import FollowListView, FollowViewSet

app_name = 'users'


urlpatterns = [
    path(
        'users/subscriptions/',
        FollowListView.as_view(),
        name='subscriptions'
    ),
    path(
        'users/<int:user_id>/subscribe/',
        FollowViewSet.as_view(),
        name='subscribe'
    ),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
