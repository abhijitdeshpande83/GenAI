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
            prompt = data.get("input")
            model_uri = 's3://sagemaker-us-east-1-720332985926/huggingface-pytorch-training-2025-06-28-15-47-21-142/output/model.tar.gz'

            response = predict(prompt, model_uri)
            return JsonResponse(response)
        
        except Exception as e:
            return JsonResponse ({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
        