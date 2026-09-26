import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/air_quality.csv")
data = data.dropna(subset=["AQI"])
data = data.head(10)
plt.figure(figsize=(8, 5))
plt.plot(
    range(1, len(data) + 1),
    data["AQI"],
    marker="o"
)
plt.title("AQI Values")
plt.xlabel("Record")
plt.ylabel("AQI")
plt.grid(True)
plt.savefig("static/aqi_graph.png")
plt.close()
print("AQI graph created successfully!")
