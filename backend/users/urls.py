from django.urls import include, path

from .views import FollowViewSet

from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register('users', FollowViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
