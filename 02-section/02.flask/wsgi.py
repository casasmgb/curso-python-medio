from app import create_app
from flask import jsonify
import traceback
from app.custom_exception import CustomException

app = create_app()

@app.errorhandler(CustomException)
def handle_custom_exception(error):
    print(f"CustomException caught: {error}\nStack Trace:\n{error.stack_trace}")
    response = {
        "error": 1,
        "message": str(error.message),
        "code": error.code,
        "data": []
    }
    return jsonify(response), error.code

@app.errorhandler(Exception)
def handle_general_exception(error):
    stack_trace = traceback.format_exc()
    print(f"Exception caught: {error}\nStack Trace:\n{stack_trace}")
    response = {
        "error": 1,
        "message": str(error),
        "code": 500,
        "data": []
    }
    return jsonify(response), 500

if __name__ == "__main__":
    app.run()