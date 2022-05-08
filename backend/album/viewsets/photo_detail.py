from rest_framework import viewsets, mixins, permissions
from ..serializers import PhotoSerializer, UpdatePhotoSerializer
from ..models import Photo


class PhotoDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(album__user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdatePhotoSerializer
        else:
            return PhotoSerializer
