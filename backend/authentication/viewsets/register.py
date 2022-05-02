from rest_framework import viewsets, mixins
from user.models import User
from ..serializers import RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

