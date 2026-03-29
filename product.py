class Product:
    def __init__(self,product_id):
        self.product_id = product_id
        self._price = 0
        self._price_history = []
    
    def set_base_price(self, price):
        if price <= 0:
            print("Price must be greater than zero!")
            return
        self._price = price
        self._price_history.append(price)
        print("Base price set succesfully.")
        
    def update_price(self, new_price):
        if new_price <= 0:
            print("New price must be greater than zero!")
            return    
        self._price = new_price
        self._price_history.append(new_price)
        print("Base updated succesfully.")
        
    def get_price_history(self):
        return self._price_history
    
products = {}

first_id = input("Enter product ID:")
products[first_id] = Product(first_id)    
print(f"Prouct'{first_id}' added succesfully.")

while True:
    print("\n=====MENU=====")
    print("1. Add Product ID")
    print("2. Set Base Price")    
    print("3 .Update_Price")
    print("4. View All Price History")
    print("5. Exit")
    
    choice = input("Choose:")
    
    if choice =="1":
        product_id=input("Enter new product ID:")
        if product_id in products:
            print("Product already exist")
            
        else:
            products[product_id] = Product(product_id)
            print(f"Product'{product_id}'added succesfully.")
            
    elif choice == "2":
        product_id = input("Enter Product ID:")
        
        if product_id not in products:
            print("Product not found!")
            continue
        try:
            price =float(input("Enter based price"))
            products[product_id].set_based_price(price)
        except ValueError:
            print("Invalid input!")
            
    elif choice == "3":
        product_id = input("Enter Product ID:")
        
        if product_id not in products:
            print("Product not found!")
            continue
        try:
            price =float(input("Enter new price"))
            products[product_id].update_price(price)
        except ValueError:
            print("Invalid input!")
            
    elif choice == "4":
        if not products:
            print("No products available.")
            
        else:
            print("\n=====ALL PRODUCT PRICE HISTORY=====")
            for pid,product in products.items():
                history = product.get_price_history()
                print(f"\nProduct ID:{pid}")
                
                if not history:
                    print("No price history")
                
                else:
                    for i,p in enumerate(history,start=1):
                        print(f"{i}.{p}")
                        
    elif choice =="5":
        print("Existing program...")
        break
    
    else:
        print("Invalid choice")
        
            
            
        
        
            
     
        
        