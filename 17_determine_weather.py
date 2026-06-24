def determine_weather():
    temp = int(input("Enter Temperature(Celsius): "))
    humidity = int(input("Enter Humidity Percentage: "))

    if temp >= 30 and humidity >= 90:
        return "Weather is Hot and Humid"
    elif temp >= 30 and humidity < 90:
        return "Weather is Hot"
    elif temp < 30 and humidity >= 90:
        return "Weather is Cool and Humid"
    elif temp < 30 and humidity < 90:
        return "Weather is Cool"
    
print(determine_weather())
    