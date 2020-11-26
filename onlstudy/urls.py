from django.urls import path
from .views import LessonsList, LessonCreate, LessonDetail, LessonEdit, LessonDelete
urlpatterns = [
    path('', LessonsList.as_view(), name='lessions_list'),
    path('create', LessonCreate.as_view(), name='lesson_create'),
    path('detail/<uuid:pk>/', LessonDetail.as_view(), name='lesson_detail'),
    path('edit/<uuid:pk>/', LessonEdit.as_view(), name='lesson_edit'),
    path('delete/<uuid:pk>/', LessonDelete.as_view(), name='lesson_delete'),
]
