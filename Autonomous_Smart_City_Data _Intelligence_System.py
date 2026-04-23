import random
import math
import numpy as np
import pandas as pd

def create_data(n):
    data = []
    for i in range(1, n + 1):
        data.append({
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    data.append({"zone": n+1, "traffic": 0, "air_quality": 70, "energy": 120})
    data.append({"zone": n+2, "traffic": 90, "air_quality": 280, "energy": 480})
    data.append({"zone": n+3, "traffic": 100, "air_quality": 150, "energy": 430})
    return data

def classify(x):
    if x["air_quality"] > 200 or x["traffic"] > 80:
        return "High Risk"
    elif x["energy"] > 400:
        return "Energy Critical"
    elif x["traffic"] < 30 and x["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def risk_score(x):
    val = (x["traffic"] * 0.3 +
           x["air_quality"] * 0.5 +
           x["energy"] * 0.2)
    return math.sqrt(val)

def sort_by_traffic(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j]["traffic"] > data[j+1]["traffic"]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def check_stability(arr):
    if np.var(arr) < 500:
        return "Stable"
    return "Unstable"

roll_number = 5

city = create_data(15)

if roll_number % 3 == 0:
    random.shuffle(city)
else:
    city = sort_by_traffic(city)

for item in city:
    item["category"] = classify(item)
    item["risk_score"] = risk_score(item)

df = pd.DataFrame(city)

traffic = np.array(df["traffic"])
aqi = np.array(df["air_quality"])
energy = np.array(df["energy"])

means = (np.mean(traffic), np.mean(aqi), np.mean(energy))

sorted_data = city.copy()
for i in range(len(sorted_data)):
    for j in range(len(sorted_data) - i - 1):
        if sorted_data[j]["risk_score"] < sorted_data[j+1]["risk_score"]:
            sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]

top3 = sorted_data[:3]

scores = df["risk_score"]
risk_tuple = (max(scores), np.mean(scores), min(scores))

diff = np.diff(aqi)
multi = []
for i in range(len(city) - 1):
    if city[i]["risk_score"] > 15 and diff[i] > 0:
        multi.append(city[i]["zone"])

stability = check_stability(traffic)

clusters = []
temp = []
for item in city:
    if item["risk_score"] > 15:
        temp.append(item["zone"])
    else:
        if len(temp) >= 2:
            clusters.append(temp)
        temp = []
if len(temp) >= 2:
    clusters.append(temp)

avg = np.mean(scores)

if avg < 10:
    decision = "City Stable"
elif avg < 15:
    decision = "Moderate Risk"
elif avg < 20:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

zone_set = set([i["zone"] for i in city])

print(df)
print("\nMean Values:", means)
print("\nTop 3 Zones:", top3)
print("\nRisk Tuple:", risk_tuple)
print("\nMulti-factor Zones:", multi)
print("\nStability:", stability)
print("\nClusters:", clusters)
print("\nFinal Decision:", decision)

print("\nInsight:")
print("Smart city systems use data to monitor conditions and manage risks effectively.")