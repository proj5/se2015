from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested import routers

from users.views import UserAccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', UserAccountViewSet)


urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
]
