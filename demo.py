
from flask import Flask, request

app = Flask(__name__)

@app.get("/calculate")
def calculate():
    expression = request.args.get("expression", "")
    return str(eval(expression))
