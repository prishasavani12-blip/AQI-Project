def calculate_aqi(pm25, pm10, co, no2, so2, o3):
    """
    Calculate a simple AQI value based on pollutant values.
    """
    aqi_pm25 = pm25 * 2
    aqi_pm10 = pm10 * 0.5
    aqi_co = co * 10
    aqi_no2 = no2 * 1
    aqi_so2 = so2 * 1
    aqi_o3 = o3 * 1
    aqi = max(
        aqi_pm25,
        aqi_pm10,
        aqi_co,
        aqi_no2,
        aqi_so2,
        aqi_o3
    )
    aqi = min(aqi, 500)
    return round(aqi)
def get_category(aqi):
    """
    Return AQI category.
    """
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"
def get_health_advice(aqi):
    """
    Return simple health advice according to AQI.
    """
    if aqi <= 50:
        return "Air quality is good. Enjoy your outdoor activities."
    elif aqi <= 100:
        return "Air quality is acceptable. Sensitive people should take some care."
    elif aqi <= 200:
        return "Sensitive people should reduce prolonged outdoor activities."
    elif aqi <= 300:
        return "Avoid prolonged outdoor activities and take necessary precautions."
    elif aqi <= 400:
        return "Avoid outdoor activities as much as possible."
    else:
        return "Avoid outdoor activities. Everyone may experience health effects."