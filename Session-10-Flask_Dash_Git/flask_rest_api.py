from flask import Flask, jsonify, request, abort
import numpy as np
app =Flask(__name__)
@app.route("/test", methods=["POST"])
def create_task():
#Check if we the incoming fields match the expected
#else throw an error
    if not request.json or not "numbers" in request.json:
        abort(400)
    numbersToSum=request.json["numbers"]
    result=sum(numbersToSum)
    if np.isnan(result):
        abort(400, "Input numbers not valid")
    return jsonify({"sum":result}), 201
if __name__ =="__main__":
    app.run()
