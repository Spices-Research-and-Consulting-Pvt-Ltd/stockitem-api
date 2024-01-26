from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
# Create your views here.


class StockList(generics.ListCreateAPIView):
    queryset = models.StockItem.objects.all()
    serializer_class = serializers.StockItemSerializer
    