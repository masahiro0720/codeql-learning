
from flask import Flask, request

app = Flask(__name__)

@app.get("/calculate")
def calculate():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    if a is None or b is None:
        return "Please provide integer parameters a and b", 400

    return str(a + b)
