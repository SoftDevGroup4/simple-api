from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "getcode"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = {"plus": num1 + num2}
    except:
        results = {"error_msg": "inputs must be numbers"}

    return jsonify(results)


if __name__ == "__main__":
    app.run()
