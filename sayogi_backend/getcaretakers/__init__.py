import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Fetch the list of caretakers"""
    
    caretakers = [
        {"id": 1, "name": "Sarah Johnson", "location": "New York", "experience": "5 years"},
        {"id": 2, "name": "David Smith", "location": "Los Angeles", "experience": "3 years"}
    ]
    
    return func.HttpResponse(json.dumps(caretakers), mimetype="application/json")
