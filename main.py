class WildfireRiskSystem:
    def __init__(self, temp, wind_speed, humidity, near_forest, rainfall):
        self.temp = temp
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.near_forest = near_forest
        self.rainfall = rainfall
        self.risk_level = ""

    def calculate_risk(self):
        riskCount = 0

        # Temperature
        if self.temp > 90:
            riskCount += 2
        elif self.temp > 75:
            riskCount += 1

        # Wind speed
        if self.wind_speed > 20:
            riskCount += 2
        elif self.wind_speed > 10:
            riskCount += 1

        # Humidity
        if self.humidity < 20:
            riskCount += 2
        elif self.humidity < 40:
            riskCount += 1

        # Proximity to forest/grassland
        if self.near_forest == "yes":
            riskCount += 2

        # Rainfall
        if self.rainfall < 0.2:
            riskCount += 2
        elif self.rainfall < 1.0:
            riskCount += 1

        # Risk level decision
        if riskCount >= 7:
            self.risk_level = "Extreme Risk"
        elif riskCount >= 5:
            self.risk_level = "High Risk"
        elif riskCount >= 3:
            self.risk_level = "Moderate Risk"
        else:
            self.risk_level = "Low Risk"

    def display_summary(self):
        print("\n444 Wildfire Risk Summary:")
        print(f"Temperature: {self.temp}°F")
        print(f"Wind Speed: {self.wind_speed} mph")
        print(f"Humidity: {self.humidity}%")
        print(f"Near Forest or Dry Grassland: {self.near_forest}")
        print(f"Rainfall: {self.rainfall} inches")
        print(f"\n Wildfire Risk Level: {self.risk_level}")

def is_number(s):
    dot_count = 0
    for char in s:
        if char == '.':
            dot_count += 1
        elif not char.isdigit():
            return False
    return dot_count <= 1 and len(s) > 0

def get_valid_input(prompt):
    value = input(prompt)
    while not is_number(value):
        print(" Please enter a valid number.")
        value = input(prompt)
    return float(value)

def get_yes_no(prompt):
    answer = input(prompt).lower()
    while answer not in ["yes", "no"]:
        print(" Please type 'yes' or 'no'.")
        answer = input(prompt).lower()
    return answer

def main():
    print(" Wildfire Risk Alert System \n")

    temp = get_valid_input("What is the Temperature (°F): ")
    wind = get_valid_input("What is the Wind Speed (mph): ")
    humidity = get_valid_input("What is the Humidity (%): ")
    near_forest = get_yes_no("Are you near a forest or dry grassland? (yes/no): ")
    rainfall = get_valid_input("Amount of Rainfall in the past 7 days (inches): ")

    risk_system = WildfireRiskSystem(temp, wind, humidity, near_forest, rainfall)
    risk_system.calculate_risk()
    risk_system.display_summary()

if __name__ == "__main__":
    main()

