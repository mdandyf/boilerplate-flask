from flask import json, Response

def ResponseSuccess(data, message, status_code=200):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps({
            "status": status_code,
            "data": data, 
            "message": message
        }),
        status=status_code
    )

def ResponseFailed(message, status_code=400):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps({
            "status": status_code,
            "errors": message
        }),
        status=status_code
    )
