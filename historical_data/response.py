from django.http.response import HttpResponseBadRequest, JsonResponse



class Response_data:
    @staticmethod
    def success_response(data=[],meta={}):
        object_ = {"status": "success", "data": data, "meta": meta}
        return JsonResponse(object_, safe=False, status=200)



    @staticmethod
    def failure_response(message, developer_message):
        object_ = {"status": "success", "data": [], "message": message, "developer_message": developer_message}
        return JsonResponse(object_, safe=False, status=450)