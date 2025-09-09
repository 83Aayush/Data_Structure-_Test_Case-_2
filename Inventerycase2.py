def process_sale(inventory, sku, qty_sold):
    updated_inventory = []
    found = False

    for item_sku, item_qty in inventory:
        if item_sku == sku:
            found = True
            if item_qty >= qty_sold:
                updated_inventory.append((item_sku, item_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                updated_inventory.append((item_sku, item_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {item_qty}")
        else:
            updated_inventory.append((item_sku, item_qty))

    if not found:
        print(f"SKU {sku} not found in inventory.")

    return updated_inventory


def identify_zero_stock(inventory):
   zero_List = [sku for sku,qty in inventory if qty == 0]
   if zero_List:
       print(f"Zero stock SKUs: {zero_List}")
   else:
       print("No zero stock items found .")
       return zero_List
   
# ---------------- MAIN PROGRAM ----------------
 
if __name__ == "__main__":
    inventory = []

  
    n = int(input("Enter number of items in inventory: "))
    for i in range(n):
        sku = int(input(f"Enter SKU for item {i+1}: "))
        qty = int(input(f"Enter quantity for SKU {sku}: "))
        inventory.append((sku, qty))

    print("\nInitial Inventory:", inventory)

    while True:
        print("\nChoose an option:")
        print("1. Normal Sale")
        print("2. Insufficient Stock Sale")
        print("3. SKU Not Found")
        print("4. Identify Zero Stock")
        print("5. No Zero Stock Check")
        print("6. Sale Reducing to Zero")
        print("7. Show Inventory")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":   
            sku = int(input("Enter SKU to sell: "))
            qty = int(input("Enter quantity sold: "))
            inventory = process_sale(inventory, sku, qty)

        elif choice == "2": 
            sku = int(input("Enter SKU to sell: "))
            qty = int(input("Enter quantity sold (greater than available): "))
            inventory = process_sale(inventory, sku, qty)

        elif choice == "3":  
            sku = int(input("Enter SKU to sell (non-existing SKU): "))
            qty = int(input("Enter quantity sold: "))
            inventory = process_sale(inventory, sku, qty)

        elif choice == "4": 
            identify_zero_stock(inventory)

        elif choice == "5": 
            identify_zero_stock(inventory)

        elif choice == "6":  
            sku = int(input("Enter SKU to sell completely: "))
            qty = int(input("Enter quantity equal to current stock: "))
            inventory = process_sale(inventory, sku, qty)

        elif choice == "7":
            print("Current Inventory:", inventory)

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")

        