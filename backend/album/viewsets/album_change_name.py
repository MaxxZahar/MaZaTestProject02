from rest_framework import viewsets, mixins
from ..serializers import AlbumSerializer
from ..models import Album


class UpdateAlbumViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
