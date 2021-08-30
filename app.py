from flask import Flask, request, render_template, jsonify
import joblib

# Machine Learning Algorithms
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Model Selection and Evaluation
from sklearn.model_selection import train_test_split
# Feature Scaling
from sklearn.preprocessing import StandardScaler

# Performance
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

app = Flask(__name__)


@app.route("/")  # defaults to only GET requests
def homepage():
    return render_template("index.html")


# allow the use of POST request with methods=["POST"]
@app.route("/api/predict", methods=["POST"])
def predict():
    if request.method == "POST":  # if the request method is POST
        x_values = request.get_json()  # get the json data
        print(x_values)
        model = joblib.load("Resources/Potential_model.pkl")  # load the model
        results = [[
                int(x_values['age']),
                float(x_values['overall_rating']),
                float(x_values['Value_rating']),
                float(x_values['hits_total'])
            ]]
        print(results)
        prediction = model.predict(  # perform the prediction by passing in your x-values
            [[
                int(x_values['age']),
                float(x_values['overall_rating']),
                float(x_values['Value_rating']),
                float(x_values['hits_total'])
            ]]
        )
        print(prediction)
        # return the predicted result
        return jsonify({"prediction": str(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)
