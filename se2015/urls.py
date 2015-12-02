from django.conf.urls import include, url
from django.contrib import admin

from users.views import UserListView, LoginView, LogoutView, UserDetailView
from users.views import AvatarView
from se2015.views import IndexView

from records.views import ExerciseRecordView, ExamRecordView
from exercises.views import ExerciseView, SkillView, GradeView, ExamDetailView
from exercises.views import ExamListView


urlpatterns = [
    url(r'^api/avatar/(?P<username>.+)/$', AvatarView.as_view()),
    url(r'^api/exam_list/(?P<grade_id>.+)/$', ExamListView.as_view()),
    url(r'^api/exam/(?P<exam_id>.+)/$', ExamDetailView.as_view()),
    url(r'^api/exam_record/(?P<exam_id>.+)/$', ExamRecordView.as_view()),
    url(r'^api/v1/exercise/(?P<grade_id>.+)/(?P<skill_id>.+)/$',
        ExerciseView.as_view()),
    url(r'^api/v1/exercise/(?P<grade_id>.+)/$', SkillView.as_view()),
    url(r'^api/v1/grades/$', GradeView.as_view()),
    url(r'^api/v1/accounts/records/(?P<username>.+)/$',
        ExerciseRecordView.as_view(),
        name='recordDetail'),
    url(r'^api/v1/accounts/(?P<username>.+)/$', UserDetailView.as_view(),
        name='detail'),
    url(r'^api/v1/accounts/', UserListView.as_view(), name='list'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
]
