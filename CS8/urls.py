
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^macroinvertebrados/login', include('Login.urls')),
    re_path(r'^macroinvertebrados/admin', include('example.urls')),

    #re_path(r'^api/v1/estudiantes/', include('example.urls')),
    #re_path(r'^api/v1/grupos/', include('example.urls')),
    #re_path(r'^api/v1/materias/', include('example.urls')),
    #re_path(r'^api/v1/profesores/', include('example.urls')),
    #path(r'^api-auth/', include('rest_framework.urls'))
]
