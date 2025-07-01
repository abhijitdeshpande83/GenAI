from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from src.inference import predict
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, I am flan-t5-fine-tuned")

@csrf_exempt
def intent_classify(request):
    if request.method == "POST":
        try:
            data=json.loads(request.body.decode('utf-8'))
            prompt = data.get("input", None)
            s3_bucket, s3_prefix = 'gen-ai-repository', 'finetuning/model/'

            if not isinstance(prompt, str):
                return JsonResponse({'error':"It is not a string"}, status=400)
            
            response = predict(prompt, s3_bucket, s3_prefix)
            return JsonResponse(response)
        
        except Exception as e:
            return JsonResponse ({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
        

def health(request):
    return JsonResponse({'status': 'ok'}, status=200)