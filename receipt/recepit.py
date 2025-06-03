import csv
from datetime import datetime

# Constants
SALES_TAX_RATE = 0.06
STORE_NAME = "Inkom Emporium"

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return:
        A compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row  # Store entire row as value
        return dictionary
    except FileNotFoundError:
        print(f"Error: missing file '{filename}'")
        return {}

try:
    # Read product catalog using read_dictionary function
    products = read_dictionary("products.csv", 0)

    if not products:
        raise FileNotFoundError("Products file is missing.")

    # Read customer order
    order = {}
    with open("request.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            product_id, quantity = row[0], int(row[1])
            if product_id in products:
                name, price = products[product_id][1], float(products[product_id][2])
                order[product_id] = (name, quantity, price)
            else:
                raise KeyError(f"Error: unknown product ID '{product_id}' in request.csv")

    # Print receipt header
    print(STORE_NAME)
    print("=" * 40)

    # Compute and print ordered items
    subtotal = 0
    total_items = 0
    for product_id, (name, quantity, price) in order.items():
        print(f"{name:<20} {quantity:>3} @ ${price:>5.2f}")
        subtotal += price * quantity
        total_items += quantity

    # Compute totals
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    print("=" * 40)
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("\nThank you for shopping at the Inkom Emporium.")

    # Print date and time
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%A %I:%M %p}")

except FileNotFoundError as e:
    print(f"Error: missing file\n{e}")
except PermissionError as e:
    print(f"Error: permission denied\n{e}")
except KeyError as e:
    print(e)