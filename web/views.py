from django.shortcuts import render
from rest_framework import viewsets
from .models import persona
from .serialzers import personaSerializer
from django.shortcuts import render


# Create your views here.
class personaViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = personaSerializer