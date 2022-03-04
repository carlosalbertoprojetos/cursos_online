from django.urls import path

from .views import forum

app_name = 'forum'


urlpatterns = [
    path('', forum, name='forum_index'),
]


