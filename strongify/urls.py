from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework import routers

from strongify.apps.authentication import views as auth_views
import strongify.views as views


# router = routers.DefaultRouter()
# router.register(r'users', auth_views.UserViewSet)
# router.register(r'groups', auth_views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name="home"),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace="rest_framework")),
    # url(r'^$', home, name="home"),
]
