from garpixcms.urls import *  # noqa
from django.urls import path, include
from authentication.viewsets import LoginViewSet
from authentication.viewsets import logout_view


urlpatterns = [urlpatterns[0]]

urlpatterns = [path('api/v1/users/', include('user.urls')),
               path('api/v1/albums/', include('album.urls')),
               path('api/v1/register/', include('authentication.urls')),
               ] + urlpatterns  # noqa

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




