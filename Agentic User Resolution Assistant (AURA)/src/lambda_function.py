from src.graph import agent
import json

def lambda_handler(event, context):

    try:
        body = json.loads(event['body']) if 'body' in event else event

        user_text = body.get("user_input")
        session = body.get("session_id")

        if not user_text:
            raise ValueError("Input text is missing")

        response=agent(user_text,session)

        data = {   
                    "message": response.get("messages")[-1].content,
                    "extracted_info": response.get("extracted_info"),
                    "complaint_data": response.get("complaint_data"),
                    "missing_info": response.get("missing_info"),
                    "active_flow": response.get("active_flow"),
                    "customer_profile": response.get("customer_profile"),
                }

        return {
            "statusCode":200,
            "body":json.dumps(data),
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
