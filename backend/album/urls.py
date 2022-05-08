from rest_framework import routers
from .viewsets import AlbumViewSet, UpdateAlbumViewSet, PhotoViewSet, PhotoDetailViewSet

album_router = routers.DefaultRouter()
album_router.register('albums', AlbumViewSet)
album_router.register('albums', UpdateAlbumViewSet)
album_router.register('photos', PhotoViewSet)
album_router.register('photos', PhotoDetailViewSet)


urlpatterns = []
urlpatterns += album_router.urls
