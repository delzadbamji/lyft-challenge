from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/test", methods=["POST"])
def index():
    if request.method == "POST":
        print("-----ENTERED POST METHOD-----")
        data = request.args.get("string_to_cut")
        data = data[3:-1:3]
        response = jsonify({"return_string": data})
        response.status_code = 200

    return response


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
