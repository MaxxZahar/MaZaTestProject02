from rest_framework import routers
from .viewsets import RegisterViewSet

auth_router = routers.DefaultRouter()
auth_router.register('', RegisterViewSet)

urlpatterns = []
urlpatterns += auth_router.urls

