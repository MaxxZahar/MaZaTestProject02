from rest_framework import routers
from .viewsets import AlbumViewSet, UpdateAlbumViewSet, PhotoViewSet

album_router = routers.DefaultRouter()
album_router.register('albums', AlbumViewSet)
album_router.register('albums/<int:pk>', UpdateAlbumViewSet)
album_router.register('photos', PhotoViewSet)


urlpatterns = []
urlpatterns += album_router.urls
