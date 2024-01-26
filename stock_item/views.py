from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
# Create your views here.


class StockList(generics.ListCreateAPIView):
    queryset = models.StockItem.objects.all()
    serializer_class = serializers.StockItemSerializer
    
class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StockItem.objects.all()
    serializer_class = serializers.StockItemSerializer
    
    
class StockListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = models.StockItem.objects.all()
        serializer = serializers.StockItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        stock = get_object_or_404(models.StockItem, pk=pk)
        serializer = serializers.StockItemSerializer(stock)
        return Response(serializer.data)