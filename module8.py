"""
Class holds information about an item that is available for purchase
"""
class ItemToPurchase:

    # Default constructor
    def __init__(self):
        self.item_name="None"
        self.item_description = "None"
        self.item_price=0.00
        self.item_quantity = 0

    # Prints the item name/quantity/cost information in an easy to read format
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_cost():.2f}")

    # Outputs the item name and description
    def print_description(self):
        print(f"{self.item_name}: {self.item_description}")

    # Calculates the total cost to consumer based on item cost and quantity
    def total_cost(self):
        return self.item_price*self.item_quantity
    
    # Returns boolean indicating whether this is a default ItemToPurchase with no modifications
    def is_default(self):
        return self.item == "None" and self.item_price == 0 and self.item_quantity == 0 and self.item_description=="None"
        
               
    

"""
Class holds information about many items available for purchase
"""
class ShoppingCart:

    cart_items = []

    # Default constructor
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name=customer_name
        self.current_date=current_date        

    
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        
    def remove_item(self, item_name):

        for idx, item in enumerate(self.cart_items):
            if item.name == item_name:
                del self.cart_items[idx]
                break
        else:
            print("Item not found in cart. Nothing removed.")           

    # Modifies an item's quantity    
    def modify_item(self, item_to_purchase):

        # Check if item already in cart and modify.
        
        for idx, item in enumerate(self.cart_items):
            if item.name == item_to_purchase.name:

                # If item_to_purchase is default, do not modify
                if item_to_purchase.is_default():
                    break

                # Change the quantity of the item in shopping cart
                item.item_quantity = item_to_purchase.item_quantity                

        # Item not found        
        else:
            print(" Item not found in cart. Nothing modified.") 


    # Returns quantity of all items in cart
    def get_num_items_in_cart(self):
        items = 0
        for item in self.cart_items:
            items += item.item_quantity
        
        return items

    # Determines and returns the total cost of items in cart
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.total_cost()

        return cost

    # Outputs total of objects in cart
    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = len(self.cart_items)
        if num_items:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()            
            print(f"Total: ${self.get_cost_of_cart()}")
        else:
            print("SHOPPING CART IS EMPTY")


    # Outputs each item's description
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_description()


# Prompts user for information about a new item
# creates and returns the item
def prompt_add_item():    
    print("\nADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_description = input("Enter the item description:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))

    item = ItemToPurchase()
    item.item_name = item_name
    item.item_description = item_description
    item.item_price = item_price
    item.item_quantity = item_quantity

    return item

# Prompts user for name of item to remove
# Return item name
def prompt_remove_item():    
    print("\nREMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove:\n")    
    return item_name

# Prompts user for new quantity of an item
# Return new item with new quantity
def prompt_modify_item():    
    print("\nCHANGE ITEM QUANTITY")
    item_name = input("Enter the item name:\n")    
    quantity = int(input("Enter the new quantity:\n"))

    # Create and return new ItemToPurchase with new quantity
    item = ItemToPurchase()
    item.item_name = item_name
    item.item_quantity = quantity
    return item


def print_menu(shopping_cart):
    while True:
        choice = input_choice()
        if choice == "q":
            break
        elif choice == "i":
            shopping_cart.print_descriptions()
        elif choice == "o":
            shopping_cart.print_total()
        elif choice == "a":
            item = prompt_add_item()
            shopping_cart.add_item(item)
        elif choice == "r":
            item_name = prompt_remove_item()
            shopping_cart.remove_item(item_name)
        elif choice == "c":
            new_item = prompt_modify_item()
            shopping_cart.modify_item(new_item)

def input_choice():
    print("\n\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    return input("Choose an option: ")    


# Prompt user information needed to create shopping car.
# returns new shopping cart
def prompt_shopping_cart():
    name = input("\nEnter customer's name:\n")
    date = input("\nEnter today's date:\n")
    print(f"Customer name: {name}")
    print(f"Today's date: {date}")

    return ShoppingCart(name,date)

    
def main():
    shopping_cart = prompt_shopping_cart()
    shopping_cart.cart_items = init_items()

    print_menu(shopping_cart)
   

if __name__ == "__main__":
    main()   