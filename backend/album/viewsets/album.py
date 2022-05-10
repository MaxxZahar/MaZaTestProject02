from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Album
from ..serializers import AlbumSerializer
from rest_framework import filters
from django.db.models import Count


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'number_of_photos']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        queryset = queryset.annotate(number_of_photos=Count('album_photo'))
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
