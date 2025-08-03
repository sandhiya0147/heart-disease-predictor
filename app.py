from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")
features = joblib.load("feature_columns.pkl")
target_names = joblib.load("target_names.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        inputs = [float(request.form[feat]) for feat in features]
        prediction = model.predict([inputs])[0]
        result = target_names[prediction]
    return render_template("index.html", features=features, result=result)

if __name__ == "__main__":
    app.run(debug=True)
