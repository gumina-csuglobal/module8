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
        pass
        
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
                self.cart_items[idx] = item_to_purchase

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
def prompt_item_for_sale():    
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
            item = prompt_item_for_sale()
            shopping_cart.add_item(item)

def input_choice():
    print("\n\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    return input("Choose an option: ")    

# Temporary initial items to populate shopping cart with
# Until all menu items implemented
def init_items():
    nike = ItemToPurchase()
    cookies = ItemToPurchase()
    headphones = ItemToPurchase()

    nike.item_name="Nike Romaleos"
    nike.item_description="Volt color, Weightlifting shoes"
    nike.item_quantity= 2
    nike.item_price = 189

    cookies.item_name="Chocolate Chips"
    cookies.item_description="Semi-sweet"
    cookies.item_quantity= 5
    cookies.item_price = 3

    headphones.item_name="Powerbeats 2 Headphones"
    headphones.item_description="Bluetooth headphones"
    headphones.item_quantity= 1
    headphones.item_price = 128

    return [nike,cookies,headphones]

# Prompt user information needed to create shopping car.
# returns new shopping cart
def prompt_shopping_cart():
    name = input("\nWhat is your name?: ")
    date = input("\nWhat is today's date?: ")

    return ShoppingCart(name,date)

    
def main():
    shopping_cart = prompt_shopping_cart()
    shopping_cart.cart_items = init_items()

    print_menu(shopping_cart)
   

if __name__ == "__main__":
    main()   