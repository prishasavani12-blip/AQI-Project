from flask import Flask, render_template, request
from aqi_calculation import calculate_aqi, get_category, get_health_advice
import pandas as pd
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    aqi = None
    category = None
    advice = None
    if request.method == "POST":
        try:
            pm25 = float(request.form["pm25"])
            pm10 = float(request.form["pm10"])
            co = float(request.form["co"])
            no2 = float(request.form["no2"])
            so2 = float(request.form["so2"])
            o3 = float(request.form["o3"])
            aqi = calculate_aqi(pm25, pm10, co, no2, so2, o3)
            category = get_category(aqi)
            advice = get_health_advice(aqi)
        except (ValueError, KeyError):
            advice = "Please enter valid pollutant values."
    return render_template(
        "index.html",
        aqi=aqi,
        category=category,
        advice=advice
    )
@app.route("/dashboard")
def dashboard():
    data = pd.read_csv("data/air_quality.csv")
    data = data.dropna(subset=["AQI"])
    data = data.tail(10)
    return render_template(
        "dashboard.html",
        data=data.to_dict("records")
    )
@app.route("/analysis")
def analysis():
    data = pd.read_csv("data/air_quality.csv")
    data = data.dropna(subset=["AQI", "Date"])
    data = data.tail(20)
    dates = data["Date"].astype(str).tolist()
    aqi_values = data["AQI"].tolist()
    return render_template(
        "analysis.html",
        dates=dates,
        aqi_values=aqi_values
    )
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)