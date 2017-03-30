def weather_activity():
    
    message = "The recommended Activity is: "
    print("What is the current temperature?: ")
    temp = int(input())
    if temp >= 90:
        message = message + "Swimming"
    elif temp >= 80:
        message = message + "Cycling"
    elif temp >= 32:
        message = message + "Golf"
    elif temp >= 0:
        message = message + "Dancing"
    else:
        message = message + "Sitting by the fire"
    print(message)

if __name__ == "__main__":
        weather_activity()
