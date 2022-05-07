from rest_framework import viewsets, mixins
from user.models import User
from ..serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # def get_serializer(self, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     kwargs['context'] = self.get_serializer_context()
    #
    #     data = self.request.data.copy()
    #     data['password'] = make_password(self.request.data.get('password'))
    #     kwargs['data'] = data
    #
    #     return serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        print(self.get_serializer_context()['request'])
        serializer.save()

