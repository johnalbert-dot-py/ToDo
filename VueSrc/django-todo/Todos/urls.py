from django.urls import path
from .views import TodoDetailApi


urlpatterns = [
    path("todo/<int:id>/", TodoDetailApi.as_view(), name="todo-detail"),
]
