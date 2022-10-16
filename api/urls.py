from django.urls import path
from .views import ToDoGetCreate, ToDoUpdateDelete
urlpatterns = [
    path("",ToDoGetCreate.as_view()),
    path("<int:pk>",ToDoUpdateDelete.as_view())
]
