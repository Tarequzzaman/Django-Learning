from django.shortcuts import render
from .documents import CarDocument
from config.response import  Response_data




def get_data(request):
    query = request.GET.get('q', '')
    sqs_app = CarDocument.search().query("multi_match", query = query, fields = ["name", "title", "abstract", "description"])
    print(sqs_app)
    return Response_data.success_response([])
    




