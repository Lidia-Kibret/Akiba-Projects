print("========================================")
print("          TRAVEL PLANNER")
print("========================================")

destination = input("Enter Destination: ")
distance = float(input("Enter Distance in kilometers: "))
speed = float(input("Enter Average Speed in km/h: "))

time = distance / speed

hours = int(time)
minutes = round((time - hours) * 60)

print("\n========================================")
print("          TRAVEL INFORMATION")
print("========================================")

print(f"Destination: {destination}")
print(f"Distance: {distance:g} km")
print(f"Average Speed: {speed:g} km/h")
print(f"Estimated Travel Time: {hours} hours {minutes} minutes")

print("========================================")