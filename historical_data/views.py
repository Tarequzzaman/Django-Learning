from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, JsonResponse
from .serializer import  DistrictSerializer
from django.core import serializers
import json

from .models import PriceHistory

# Create your views here.



def insert_pice(requests):

    data = PriceHistory.objects.create(price= 66.66, volume=3.5)
    response = {
        'status': "success",
        'type': 'insert',
    }
    return JsonResponse(response)

def get_all_data(requests):
    event_list = PriceHistory.objects.filter()
    list1 = []
    for x in event_list:
        dict_1 ={}
        dict_1['id'] = x.id
        dict_1['price']= x.price
        dict_1['volume']=x.volume
        dict_1['created_at'] = x.created_at

        list1.append(dict_1)
        



    # serializers_data = serializers.serialize('json', event_list)
    # print(type(serializers_data))

    return JsonResponse(list1, safe=False)



def update(requests):
    try:
        uuid = requests.GET.get('uuid')
        print(uuid)
        data =  PriceHistory.objects.filter(id = uuid).update(price = 69)
        print(type(data))
        return JsonResponse({"status": "success", "data": str(data) + " rows updated"})
    except Exception as E:
        return JsonResponse({"status" : "error", "Exception": str(E)})










