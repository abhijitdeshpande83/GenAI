from src.graph import agent
import json

def lambda_handler(event, context):

    try:
        usr_input=json.loads(event['body']) if 'body' in event else event

        if not usr_input:
            raise ValueError("Input text is missing")

        response=agent(usr_input)

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
