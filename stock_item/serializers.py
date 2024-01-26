from rest_framework import serializers
from . import models

class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockItem
        fields = '__all__'