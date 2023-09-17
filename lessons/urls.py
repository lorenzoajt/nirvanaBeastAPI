from django.urls import path
from .views import LessonsList, LessonDetail

urlpatterns = [
    path('lessons/', LessonsList.as_view()),
    path('lessons/<int:pk>/', LessonDetail.as_view()),
]