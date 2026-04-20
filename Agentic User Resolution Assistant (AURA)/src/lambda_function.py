from src.graph import agent
import json

def lambda_handler(event, context):

    try:
        usr_input=json.loads(event['body']) if 'body' in event else event

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
