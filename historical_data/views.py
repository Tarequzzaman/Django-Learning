from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, JsonResponse
from .serializer import  PriceHistorySerializer
from django.core import serializers
import json
from django.utils.timezone import now

from .response import Response_data
from .models import PriceHistory, Users






def insert_pice(requests):
    price = requests.GET.get("price", None)
    volume =requests.GET.get("price", None)

    if price or volume == None: 
        return 
    data = PriceHistory.objects.create(price= price, volume= volume)
    response = {
        'status': "success",
        'type': 'insert',
    }
    return JsonResponse(response)

def get_all_data(requests):
    try:
        event_data = PriceHistory.objects.filter()
        serializer = PriceHistorySerializer(event_data, many=True)
        return Response_data.success_response(serializer.data)


    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))



def update(requests):
    try:
        uuid = requests.GET.get('uuid')
        data =  PriceHistory.objects.filter(id = uuid).update(price = 69, updated_at = now())
        return JsonResponse({"status": "success", "data": str(data) + "rows updated"})
    except Exception as E:
        return JsonResponse({"status" : "error", "Exception": str(E)})



def create_user(requests):
    try:
        first_name = requests.GET.get("first_name")
        last_name = requests.GET.get("last_name")
        phone =  requests.GET.get('phone')
        email = requests.GET.get('email')
        data = Users.objects.create(first_name= first_name, last_name= last_name, phone = phone, email = email)
        uuid = data.id
        return Response_data.success_response([{'id': uuid}])
    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))











