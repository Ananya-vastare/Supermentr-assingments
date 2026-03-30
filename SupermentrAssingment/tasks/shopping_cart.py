# Shopping Cart Program
#11th feb
cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Print total items")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        item = input("Enter the name of the item to add: ")
        cart.append(item)
        print(f"'{item}' has been added to your cart.")

    elif choice == '2':
        item = input("Enter the name of the item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print(f"Error: '{item}' is not in your cart.")

    elif choice == '3':
        print("\nItems in your cart:")
        if not cart:
            print("The cart is empty.")
        else:
            for index, item in enumerate(cart, 1):
                print(f"{index}. {item}")
        print(f"Total count: {len(cart)}")

    elif choice == '4':
        print("Exiting... Happy shopping!")
        break

    else:
        print("Invalid choice, please try again.")