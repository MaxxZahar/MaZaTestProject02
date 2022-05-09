from rest_framework import viewsets, mixins, permissions, filters
from ..serializers import PhotoSerializer
from ..models import Photo


class PhotoViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                   mixins.ListModelMixin):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['added_at', 'album__id']
    ordering = ['-added_at']

    def get_queryset(self):
        queryset = self.queryset.filter(album__user=self.request.user)
        return queryset
