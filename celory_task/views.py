from django.shortcuts import render
from .task import sample_task_1
from django.views.decorators.csrf import csrf_exempt
from config.response import Response_data



@csrf_exempt
def run_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        task = sample_task_1.apply_async(retry=True, retry_policy={'max_retries': 3,'interval_start': 0,'interval_step': 0.2, 'interval_max': 0.2} , kwargs={"counter":int(task_type)})
        return Response_data.success_response({"task_id": task.id})

   