from rest_framework import serializers
from . import models

class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockItem
        fields = '__all__'
        
        
class StockItemFrontEndSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.StockItem
        fields = ['id', 'item_name', 'item_code']