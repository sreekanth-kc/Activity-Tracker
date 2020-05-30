from django.conf.urls import url
from user_activity.views import UserActivities, home_page
urlpatterns = [
    url(r'^getuseractivity', UserActivities.as_view(), name='getuseractivity'),
    url(r'^', home_page, name='root')
]
