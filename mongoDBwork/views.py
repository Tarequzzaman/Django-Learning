from django.shortcuts import render
from config.response import  Response_data

from .serializers import PostSerializers
from .models import Post



def create_post(requests):
    try:
        post = Post.objects.create(
          title='Hello MongoDB!',
          description='Just wanted to drop a note from Django. Cya!',   
          )
        return Response_data.success_response([], {"message": "Data insert Successfull"})
    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))


def get_post(requests):
    try:
        post_id = requests.GET.get('post_id', None)
        if post_id== None:
            return Response_data.failure_response("Something Went Wrong", "Please enter post_id")
        post_data = Post.objects.filter(id=post_id).first()
        serializer = PostSerializers(post_data, many=False)
        return Response_data.success_response([serializer.data])
    except Exception as E:
        return Response_data.failure_response("Something Went Wrong", str(E))