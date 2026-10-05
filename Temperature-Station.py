celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

celsius = (fahrenheit - 32) * 5 / 9
kelvin = celsius + 273.15

print(f"\nCelsius: {celsius}°C")
print(f"Fahrenheit: {fahrenheit}°F")
print(f"Kelvin: {kelvin} K")

print(f"\nFahrenheit: {fahrenheit}°F")
print(f"Celsius: {celsius}°C")
print(f"Kelvin: {kelvin} K")