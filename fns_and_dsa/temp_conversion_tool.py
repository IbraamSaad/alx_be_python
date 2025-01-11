FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit




temperature = float(input("Enter the temperature to convert: "))
is_faharenheit_or_celsuis = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def main():
    match is_faharenheit_or_celsuis:
        case "F":
            celsuis = convert_to_celsius(temperature)
            print(f"{temperature}°F {celsuis}")
        case "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C {fahrenheit}")
        case "_":
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

