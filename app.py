from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "getcode999"


@app.route("/isodd/<num>", methods=["GET"])
def isodd(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return "False"
        return "True"
    except:
        return {"error_msg": "inputs must be numbers"}


if __name__ == "__main__":
    app.run()
