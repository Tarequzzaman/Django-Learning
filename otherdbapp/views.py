from django.shortcuts import render
from django.shortcuts import render
from config.response import  Response_data
from .models import Users

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



def get_user(requests):
    return Response_data.failure_response("Something Went Wrong", "")
