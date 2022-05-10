from rest_framework import viewsets, mixins
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
