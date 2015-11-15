from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested import routers

from users.views import UserListView, LoginView, LogoutView, UserDetailView
from se2015.views import IndexView

from exercises.views import ExerciseViewSet, ExerciseView, SkillView


router = routers.SimpleRouter()
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    url(r'^api/v1/exercise/(?P<grade_id>.+)/(?P<skill_id>.+)/$',
        ExerciseView.as_view()),
    url(r'^api/v1/exercise/(?P<grade_id>.+)/$', SkillView.as_view()),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/accounts/(?P<username>.+)/$', UserDetailView.as_view(),
        name='detail'),
    url(r'^api/v1/accounts/', UserListView.as_view(), name='list'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
]
