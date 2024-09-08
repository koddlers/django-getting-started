from django.urls import path

from meetings.views import detail, rooms_list

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms_list, name='rooms'),
]