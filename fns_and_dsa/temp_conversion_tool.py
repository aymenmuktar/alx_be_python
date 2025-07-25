# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FREEZING_POINT_F = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temp_value = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

