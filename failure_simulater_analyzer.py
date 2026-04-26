import random
import math
import numpy as np
import pandas as pd
import copy

def make_data(n):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "metrics": {
                "traffic": random.randint(10,100),
                "pollution": random.randint(20,300),
                "energy": random.randint(50,500)
            },
            "history": [random.randint(5,40) for _ in range(3)]
        })
    return data

def rotate_data(d):
    return d[3:] + d[:3]

def create_copies(d):
    a = d
    b = copy.copy(d)
    c = copy.deepcopy(d)
    return a, b, c

def modify_data(d):
    for i in d:
        i["metrics"]["traffic"] += 5
        i["history"].append(random.randint(1,50))

def risk_calc(x):
    total = x["metrics"]["traffic"] + x["metrics"]["pollution"] + x["metrics"]["energy"]
    return math.log(total)

def manual_correlation(x, y):
    x = np.array(x)
    y = np.array(y)
    mx = np.mean(x)
    my = np.mean(y)
    num = sum((x-mx)*(y-my))
    den = math.sqrt(sum((x-mx)**2) * sum((y-my)**2))
    return num/den

def find_anomalies(risk):
    mean = np.mean(risk)
    std = np.std(risk)
    a = []
    for i,v in enumerate(risk):
        if v > mean + std:
            a.append(i)
    return a

def find_clusters(risk):
    c = []
    temp = []
    avg = np.mean(risk)
    for i,v in enumerate(risk):
        if v > avg:
            temp.append(i)
        else:
            if len(temp) >= 2:
                c.append(temp)
            temp = []
    if len(temp) >= 2:
        c.append(temp)
    return c

data = make_data(15)

data = rotate_data(data)

a, b, c = create_copies(data)

print("BEFORE")
print("Original:", data)
print("Assigned:", a)
print("Shallow:", b)
print("Deep:", c)

modify_data(a)
modify_data(b)
modify_data(c)

print("\nAFTER")
print("Original:", data)
print("Assigned:", a)
print("Shallow:", b)
print("Deep:", c)

rows = []
for i in data:
    rows.append({
        "zone": i["zone"],
        "traffic": i["metrics"]["traffic"],
        "pollution": i["metrics"]["pollution"],
        "energy": i["metrics"]["energy"]
    })

df = pd.DataFrame(rows)

traffic = df["traffic"]
pollution = df["pollution"]

corr = manual_correlation(traffic, pollution)

risk_vals = [risk_calc(i) for i in data]

anomalies = find_anomalies(risk_vals)

clusters = find_clusters(risk_vals)

stability = 1 / np.var(risk_vals)

result = (max(risk_vals), min(risk_vals), stability)

if stability > 0.02:
    decision = "System Stable"
elif stability > 0.01:
    decision = "Moderate Risk"
elif stability > 0.005:
    decision = "High Corruption Risk"
else:
    decision = "Critical Failure"

print("\nDataFrame:\n", df)
print("\nCorrelation:", corr)
print("\nAnomalies:", anomalies)
print("\nClusters:", clusters)
print("\nTuple:", result)
print("\nDecision:", decision)

print("\nExplanation:")
print("Shallow copy affects nested data because inner structures share same memory reference.")