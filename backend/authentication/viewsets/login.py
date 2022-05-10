from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from user.models import User
from ..serializers import LoginSerializer
from django.contrib.auth import login, authenticate


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        password = serializer.validated_data['password']
        authenticate(username=user, password=password)
        login(self.request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
