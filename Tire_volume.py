from datetime import datetime
import math

# Prompt the user for input
width = float(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the volume
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
volume = round(volume, 2)

# Get the current date (without time)
current_date = datetime.now().date()

# Append data to the volumes.txt file
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}", file=volumes_file)

# Optional: print the result to the user
print(f"The approximate volume is {volume} liters")
