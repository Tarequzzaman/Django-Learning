from rest_framework import serializers

from .models import *

class DistrictSerializer(serializers.ModelSerializer):
    #json = serializers.SerializerMethodField('clean_json')
    #fields = ['Id', 'DistrictName']
    class Meta:
        model = PriceHistory
        fields = ('price', 'volume')


