catalog = [ # dictionary list of store products
    {
        "id": 4,
        "title": "Keyboard",
        "price": 63.87
    },
    {
        "id": 2,
        "title": "Coffee mug",
        "price": 34.99
    },
    {
        "id": 9,
        "title": "Trackpad",
        "price": 97.93
    },
    { 
        "id": 7,
        "title": "Mouse", 
        "price": 14.99
    },
]
 
# FULL CODE
from catalog import catalog  # import your catalog list

# Global shopping cart
cart = []

# ----------------------------
# Helper functions
# ----------------------------
 
def print_header(text):
    print("---------------------")
    print(text)
    print("---------------------")

def print_menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Product")
    print(" 3.- View Cart")
    print(" 4.- Add Product to Catalog")
    print(" 5.- Clear Cart")
    print(" 6.- Pay")
    print("")
    print(" Q.- Quit")

# ----------------------------
# Catalog and Cart Functions
# ----------------------------

def print_catalog():
    print_header("- Our catalog -")
    for prod in catalog:        # Ljust which means left justify. so 15 spaces to the right
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
    print("---------------------\n")

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)  # add product to the cart (bag)
            print(f'{prod["title"]} added to your cart.')
            break  # stop after finding the product

    if not found:
        print("**Error: Invalid ID")
    print("---------------------\n")

def search_product():
    text = input("Search text: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')
            choice = input("Do you want to add this item to your cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break  # stop after first match

    if not found:
        print("Sorry, this item doesn’t exist.")
    print("---------------------\n")

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]} |')
        cart_total()  # show total
    print("---------------------\n")

def cart_total():
    total = 0  # start from 0 and add up prices
    for prod in cart:
        total += prod["price"]  # add product price to total
    print(f"Total: ${total}")

def clear_cart():
    cart.clear()
    print("Your cart has been cleared.")
    print("---------------------\n")

def pay():
    if not cart:
        print("Your cart is empty. Add something first!")
        print("---------------------\n")
        return

    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    cart_total()
    print(f"\nThank you {full_name}!")
    print("Your order has been processed.")
    print("A confirmation has been sent to your email.")
    cart.clear()  # empty cart after payment
    print("---------------------\n")

# ----------------------------
# Add new product to catalog
# ----------------------------

def add_product_to_catalog():
    # ID
    while True:
        prod_id_input = input("Enter product ID: ")
        if prod_id_input.isdigit():
            prod_id = int(prod_id_input)
            break
        else:
            print("**Error: ID must be a number, try again.")

    # Title
    title = input("Enter product title: ")

    # Price
    while True:
        price_input = input("Enter product price: ")
        if price_input.replace(".", "", 1).isdigit():
            price = float(price_input)
            break
        else:
            print("**Error: Price must be a number, try again.")

    # Build dictionary
    new_prod = {"id": prod_id, "title": title, "price": price}
    catalog.append(new_prod)
    print(f'Product "{title}" added to catalog!')
    print("---------------------\n")

# ----------------------------
# Main Program Loop
# ----------------------------
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Store xy")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        add_product_to_catalog()
    elif option == "5":
        clear_cart()
    elif option == "6":
        pay()
    elif option == "q" or option == "Q":
        print("Good bye!")
        break
    else:
        print("** Error: invalid option")
        print("---------------------\n")

