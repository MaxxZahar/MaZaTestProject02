from rest_framework import routers
from .viewsets import AlbumViewSet, UpdateAlbumViewSet

album_router = routers.DefaultRouter()
album_router.register('', AlbumViewSet)
album_router.register('<int:pk>', UpdateAlbumViewSet)


urlpatterns = []
urlpatterns += album_router.urls
