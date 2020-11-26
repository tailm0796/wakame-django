from django.urls import path
from .views import LessonsList
urlpatterns = [
    path('',LessonsList.as_view(), name = 'Lessions_List'),
]