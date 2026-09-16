class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\n===== {self.name} Menu =====")
        for food in self.menu:
            print(f"- {food.item_id}: {food.name} - ₹{food.price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, food, quantity):
        self.items.append((food, quantity))
        print(f"{food.name} added to cart.")

    def calculate_total(self):
        total = 0
        for food, quantity in self.items:
            total += food.price * quantity
        return total


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.status = "Placed"

    def place_order(self):
        total = self.cart.calculate_total()
        print("\n=====ORDER DETAILS=====")
        print(f"Order Status: {self.status}")
        
        self.status = "CONFIRMED"
        print("Order Confirmed!")
        
        self.status = "PREPARING"
        print("Food is being prepared...")
        
        self.status = "OUT FOR DELIVERY"
        print("Order is out for delivery...")
        
        self.status = "DELIVERED"
        print("Order Delivered!")


# Execution block (moved outside the class to prevent infinite recursion)
if __name__ == "__main__":
    restaurant = Restaurant("Foodie Haven")
    
    pizza = FoodItem(1, "Pizza", 250)
    burger = FoodItem(2, "Burger", 150)
    juice = FoodItem(3, "Juice", 100)
    
    restaurant.add_food(pizza)
    restaurant.add_food(burger)
    restaurant.add_food(juice)
    
    restaurant.show_menu()
    
    cart = Cart()
    cart.add_item(pizza, 1)
    cart.add_item(burger, 2)
    cart.add_item(juice, 1)
    
    order = Order(cart)
    order.place_order()