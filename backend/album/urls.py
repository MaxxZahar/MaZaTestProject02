from rest_framework import routers
from .viewsets import AlbumViewSet

album_router = routers.DefaultRouter()
album_router.register('', AlbumViewSet)

urlpatterns = []
urlpatterns += album_router.urls
