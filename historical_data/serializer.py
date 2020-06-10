from rest_framework import serializers

from .models import *

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ['id','price', 'volume', 'created_at']





