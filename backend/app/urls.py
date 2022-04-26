from garpixcms.urls import *  # noqa
from django.urls import path, include

urlpatterns = [path('api/v1/users/', include('user.urls'))] + urlpatterns  # noqa
