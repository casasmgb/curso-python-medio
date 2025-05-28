# utils.py

def format_response(data, message, code=0):
    if data and (isinstance(data, list) or isinstance(data, object)):
        return {
            "error": 0,
            "message": message,
            "code": code,
            "data": data
        }
    else:
        return {
            "error": 1,
            "message": message,
            "code": code,
            "data": []
        }
