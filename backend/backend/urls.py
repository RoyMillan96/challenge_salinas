from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v0.1',
        description="Documentación pública de API",
        contact=openapi.Contact(email="roymillan96@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('login/',Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    re_path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('users/', include('apps.users.api.routers')),
    path('weather/', include('apps.weather.api.urls')),
]
