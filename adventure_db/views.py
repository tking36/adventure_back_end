from django.shortcuts import render

from rest_framework import generics
from .serializers import AdventureSerializer
from .models import Adventure

class AdventureList(generics.ListCreateAPIView):
    queryset = Adventure.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = AdventureSerializer # tell django what serializer to use

class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adventure.objects.all().order_by('id')
    serializer_class = AdventureSerializer