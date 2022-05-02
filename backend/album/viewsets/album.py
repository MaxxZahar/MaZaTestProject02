from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Album
from ..serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     queryset = self.queryset.filter(user=self.request.user)
    #     if not queryset:
    #         raise Exception('Not authenticated')
    #     return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
