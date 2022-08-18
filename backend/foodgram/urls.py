
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

api_patterns = [
    path('', include('recipes.urls', namespace='api_recipes')),
    path('', include('users.urls', namespace='api_users')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)