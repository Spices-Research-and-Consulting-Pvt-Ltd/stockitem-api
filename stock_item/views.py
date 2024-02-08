from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
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
    
    def create(self, request):
        serializer = serializers.StockItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        stock = get_object_or_404(models.StockItem, pk=pk)
        serializer = serializers.StockItemSerializer(stock)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = get_object_or_404(models.StockItem, pk=pk)
        serializer = serializers.StockItemSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        stock = get_object_or_404(models.StockItem, pk=pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StockModelView(viewsets.ModelViewSet):
    queryset = models.StockItem.objects.all()
    serializer_class = serializers.StockItemSerializer
    
class StockItemCheckView(APIView):
    def get(self, request):
        try:
            stock_id = request.GET.get('stock_id')
            stock = models.StockItem.objects.get(id=stock_id)
            # stock = get_object_or_404(models.StockItem, id=stock_id)
            if stock:
                return Response({'exists': True}, status=status.HTTP_200_OK)
        except models.StockItem.DoesNotExist:
            # Stock item not found, return false
            return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            # Handle other exceptions (e.g., database connection error)
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)