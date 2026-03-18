x = input("Enter username: ")
y = int(input("Enter password: "))
if x == "Akhil" and y == 456 :
    print("\nLogin Successful.\n")
    b = int(input("Enter number of buildings "))
    readings = []
    for i in range(b):
        value = int(input(f"Enter reading for building {i+1}: "))
        readings.append(value)
    valid = [e for e in readings if e >= 0]
    total = sum(valid)
    Food = input("\nHave you taken food ? (yes/no): ").lower()
    if Food == "yes":
        print("Good. System detects energy levels in you.")
    else:
        print("Warning: Low energy detected.Take some food .")
    e_dict = {
        "efficient": [e for e in readings if 0 <= e <= 50],
        "moderate": [e for e in readings if 51 <= e <= 150],
        "high": [e for e in readings if e > 150],
        "invalid": [e for e in readings if e < 0]
    }
    Num_buildings = len(readings)
    analysis = (total, Num_buildings)
    high_count = len(e_dict["high"])
    eff_count = len(e_dict["efficient"])
    mod_count = len(e_dict["moderate"])
    if total > 600:
        result = "Energy Waste Detected. The electricity board is not happy."
    elif high_count > 3:
        result = "Overconsumption detected. Too much power usage."
    elif (eff_count - mod_count <= 1) and (mod_count - eff_count <= 1):
        result = "Balanced usage. Everything looks under control."
    elif eff_count > max(mod_count, high_count):
        result = "Efficient campus. Good job managing energy."
    else:
        result = "Moderate usage. Nothing unusual."
    print("\n--- Campus Energy Intelligence Report ---")
    print("Energy usage classification:")
    for key, value in e_dict.items():
        print(f"{key} buildings: {value}")
    print("\nTotal energy consumed:", analysis[0])
    print("Number of buildings analyzed:", analysis[1])
    print("System Conclusion:", result)
else:
    print("\nInvalid login. Access denied.")