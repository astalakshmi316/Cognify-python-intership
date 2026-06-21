def convert_temperature():
    # User kitta irundhu value vanga float use panrom
    temp = float(input("Enter the temperature value: "))
    unit = input("Is this in Celsius or Fahrenheit? (Enter C or F): ").strip().upper()

    if unit == 'C':
        # Celsius to Fahrenheit mathatkana formula
        fahrenheit = (temp * 9/5) + 32
        print(f"Converted Temperature: {fahrenheit:.2f}°F")
    elif unit == 'F':
        # Fahrenheit to Celsius mathatkana formula
        celsius = (temp - 32) * 5/9
        print(f"Converted Temperature: {celsius:.2f}°C")
    else:
        print("Invalid unit! Please enter either 'C' or 'F'.")

# Function-ah call panrom
convert_temperature()
