print("================================")
print("          BMI REPORT")
print("================================")

name = input("Enter your Name: ")
weight = float(input("Enter Weight in kilograms: "))
height = float(input("Enter Height in meters: "))

bmi = weight / (height * height)

print("\n================================")
print("          BMI REPORT")
print("================================")

print(f"Name: {name}")
print(f"Weight: {weight:g} kg")
print(f"Height: {height:.2f} m")
print(f"\nBMI: {bmi:.2f}")

print("================================")
