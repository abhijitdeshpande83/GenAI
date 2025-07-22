from src.inference_generation import predict
import json

# s3_bucket, s3_prefix = 'gen-ai-repository', 'finetuning/model/'

def lambda_function(event, context):

    try:
        body = json.loads(event['body']) if 'body' in event else event
        input_text = body.get('input', None)

        if input_text is None:
            raise ValueError("Input text is missing")
        
        result = predict(input_text)

        return {
            "statusCode":200,
            "body": json.dumps(result),
            "headers":
            {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers":
            {
                "Content-Type": "application/json"
            }
        }