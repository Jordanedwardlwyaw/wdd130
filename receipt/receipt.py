import csv
from datetime import datetime


SALES_TAX_RATE = 0.06
STORE_NAME = "Inkom Emporium"

def read_dictionary(filename, key_column_index):
    """Read products.csv into a compound dictionary."""
    dictionary = {}
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) > key_column_index:
                    key = row[key_column_index].strip()
                    dictionary[key] = row
        return dictionary
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        return {}

def main():
    try:
        
        products = read_dictionary("C:/Users/y/OneDrive/desktop/CSCP110/CSE111/Wdd130/receipt/products.csv", 0)

        if not products:  
            return

        
        order = {}
        try:
            with open("request.csv", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) < 2:
                        continue
                    product_id = row[0].strip()
                    quantity = int(row[1])  

                    
                    product_data = products[product_id]
                    name, price = product_data[1], float(product_data[2])

                    
                    if product_id in order:
                        order[product_id] = (name, order[product_id][1] + quantity, price)
                    else:
                        order[product_id] = (name, quantity, price)
        except FileNotFoundError as e:  
            print("Error: missing file")
            print(e)
            return

        
        print(STORE_NAME)
        print()

        subtotal = 0
        total_items = 0

        for name, quantity, price in order.values():
            print(f"{name}: {quantity} @ ${price:.2f}") 
            subtotal += quantity * price
            total_items += quantity

        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium.")

        
        current_date_and_time = datetime.now()
        print(f"\n{current_date_and_time:%A %I:%M %p}")

    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    except KeyError as e:
        print("Error: unknown product ID in request.csv")
        print(f"'{e}'")  

if __name__ == '__main__':
    main()