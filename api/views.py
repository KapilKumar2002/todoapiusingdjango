from rest_framework import generics
from .models import ToDo
from .serializer import ToDoSerializer

class ToDoGetCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
class ToDoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer