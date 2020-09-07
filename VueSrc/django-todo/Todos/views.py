from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo


class TodoDetailApi(mixins.RetrieveModelMixin, generics.GenericAPIView):

    lookup_field = "id"
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
