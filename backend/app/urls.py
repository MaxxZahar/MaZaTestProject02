from garpixcms.urls import *  # noqa
from django.urls import path, include

urlpatterns = [path('api/v1/users/', include('user.urls')),
               path('api/v1/albums/', include('album.urls')),
               path('api/v1/register/', include('authentication.urls')),] + urlpatterns  # noqa

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

