from src.graph import agent
import json

def lambda_handler(event, context):

    try:
        body=json.loads(event['body']) if 'body' in event else event
        usr_input = body.get('user_input', None)

        if not usr_input:
            raise ValueError("Input text is missing")

        response=agent(usr_input)

        return {
            "statusCode":200,
            "body":json.dumps(response),
            "headers":
            {
                "Content-Type":"application/json"
            }
        }

    except Exception as e:
        return {
            "statusCode":500,
            "body":json.dumps({"error":str(e)}),
            "headers":
            {
                "Content-Type":"application/json"
            }
        }
