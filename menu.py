# CONSTANTS
ITEMNAME = "Item Name"
PRICE = "Price"
QUANTITY = "Quantity"

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
cust_order = []
#     {
#         ITEMNAME: str,
#         PRICE: float,
#         QUANTITY: int
#     }
# ]


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key        
        # Add 1 to the menu item number
        i += 1
    print(menu.keys())
    
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            #menu_items is reinitalzed for the sub menu 
            menu_items = {} 
            print("-------+--------------------------+-------")
            print("Item # | Item name                | Price")
            print("-------+--------------------------+-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{' '*(5-len(str(i)))}{i}  | {key} - {key2}{item_spaces} |{' '*(5-len(str(value2)))}${value2} ")
                        menu_items[i] = {
                            ITEMNAME: key + " - " + key2,
                            PRICE: value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{' '*(5-len(str(i)))}{i}  | {key}{item_spaces} |{' '*(5-len(str(value)))}${value}")
                    menu_items[i] = {
                        ITEMNAME: key,
                        PRICE: value
                    }
                    i += 1
            print("-------+--------------------------+-------")
            # 2. Ask customer to input menu item number
            menu_selection = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
    
                # Convert the menu selection to an integer
                int_menu_selection=int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                if int_menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    order_item_name =dict( menu_items.get(int_menu_selection))[ITEMNAME]
                    order_item_price =dict( menu_items.get(int_menu_selection))[PRICE]
                    # Ask the customer for the quantity of the menu item
                    quantity=input("Enter order quantity (if order quantity is invalid order quantity will default to 1)")
                           
                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity=1
                    
                    # Add the item name, price, and quantity to the order list
    # *** checking if the item exists? if it does then we update the quantity
                    order_item_exists = False
                    for order_item in cust_order:
                        if order_item.get(ITEMNAME) == order_item_name:
                            # Item already exists, update the quantity
                            old_order_quantity=order_item[QUANTITY]
                            order_item[QUANTITY] = int(order_item[QUANTITY]) + int(quantity)
                            order_item_exists = True
                            print(f"Updated quantity for {order_item_name} from {old_order_quantity} to {order_item[QUANTITY]}")
                            break

                    if not order_item_exists:
                        # Item does not exist, add it to the cust_order list
                        cust_order.append({ITEMNAME: order_item_name, PRICE: order_item_price, QUANTITY: quantity})
                        print(f"Added {quantity} items for {order_item_name}")
                else:
                    # Tell the customer that their input isn't valid
                    print("** Invalid Menu item Selection")
            else:
                # Tell the customer they didn't select a menu option
                print("** Invalid Menu option selected")


        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.upper() in ["Y","N"]: 
            # Keep ordering
            if keep_ordering.upper()=="Y":
                break
            elif keep_ordering.upper()=="N":
                # Exit the keep ordering question loop
                # Complete the order
                                
                place_order=False            
                
                # Exit the keep ordering question loop
                break        
        else:
            # Tell the customer to try again
            print("Invalid input option please enter Y or N")
            
                
# if a customer exits with out adding a single order item then inform them accordingly 
if len(cust_order)==0:
    print("since no menu item were picked your order has not been created. Please visit us again.")
else:
    # Since the customer decided to stop ordering, thank them for
    # their order
    print("Thank you for ordering from the variety food truck.")        
    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Uncomment the following line to check the structure of the order
    #print(order)
    print("--------------------------+--------+----------")
    print("Item name                 | Price  | Quantity ")
    print("--------------------------+--------+----------")

    # 6. Loop through the items in the customer's order
    for item in cust_order:
        # 7. Store the dictionary items as variables
        f_order_item_name=item[ITEMNAME]           
        f_price=item[PRICE]
        f_quantity=item[QUANTITY]

        # 8. Calculate the number of spaces for formatted printing
        # 9. Create space strings
        #***Calculate spaces for left aligned 
        num_item_name_spaces = 26 - len(f_order_item_name) 
        item_name_spaces = " " * num_item_name_spaces

        #***Calculate spaces for right aligned 
        num_item_price_spaces = 8 - len(str(f_price)) -2
        item_price_spaces = " " * num_item_price_spaces

        #***Calculate spaces for right aligned 
        num_item_quantity_spaces = 10 - len(str(f_quantity)) -1
        item_quantity_spaces = " " * num_item_quantity_spaces    

        # 10. Print the item name, price, and quantity
        print(f"{f_order_item_name}{item_name_spaces}|{item_price_spaces}${str(f_price)} |{item_quantity_spaces}{str(f_quantity)}")            
                    

    # 11. Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()

    order_total = sum(float(oitem[PRICE]) * int(oitem[QUANTITY]) for oitem in cust_order)

    # and print the prices.
    print("--------------------------+--------+----------")
    str_tc="Total cost of the order:"
    num_tc_spaces = 35 - len(str_tc) 
    #*** right align order  total 
    num_cost_spaces = 10 - len(str(order_total)) -2

    print(f"{str_tc}{' ' * num_tc_spaces}|{' ' * num_cost_spaces}${order_total}")
    print("-----------------------------------+----------")
