from rest_framework.routers import DefaultRouter
from apps.users.api.user_viewsets import UserViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='users')
urlpatterns = router.urls