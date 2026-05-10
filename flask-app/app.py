from flask import Flask, render_template, request

from transformations_anrozk import reverse_string

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_str = ""
    if request.method == "POST":
        input_str = request.form.get("input_str", "")
        result = reverse_string(input_str)
    return render_template("index.html", result=result, input_str=input_str)


if __name__ == "__main__":
    app.run(debug=True)
