import math

# Ask the user for input
width = int(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the tire volume
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the result
print(f"\nThe approximate volume is {volume:.2f} liters")
