from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "getcode999"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = f"{num1} + {num2} = {num1 + num2}"
    except:
        results = {"error_msg": "inputs must be numbers"}

    return results


@app.route("/is_prime/<num>", methods=["GET"])
def is_prime(num):
    try:
        num = int(num)

        for i in range(2, num):
            if num % i == 0:  # not prime
                return "False"
        return "True"
    except:
        return {"error_msg": "inputs must be numbers"}


if __name__ == "__main__":
    app.run()
