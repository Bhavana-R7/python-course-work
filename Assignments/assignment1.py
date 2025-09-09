# Flipkart Profile Information

# App Name
app_name = "Flipkart"     

# User ID (int)
user_id = int(input("Enter your Flipkart user ID: "))                  

# Full Name (str)
full_name = input("Enter your full name: ")                            

# Wishlist (list)
wishlist_input = input("Enter items in your wishlist (comma-separated): ")         
wishlist = [item.strip() for item in wishlist_input.split(',')]

# Order History (tuple)
last_order_item = input("Enter your last ordered item: ")
last_order_amount = float(input("Enter the last order amount (in ₹): "))
order_history = (last_order_item, last_order_amount)

# Total Orders (int)
total_orders = int(input("Enter total number of completed orders: "))   

# Cart Items (int)
cart_items = int(input("Enter number of items currently in your cart: "))

# Reward Points (int)
reward_points = int(input("Enter your Flipkart SuperCoin balance: "))

# Membership Details (set)
membership_input = input("Enter your memberships (comma-separated, e.g., Plus, SuperCoin): ")       
memberships = set(m.strip() for m in membership_input.split(','))

# Delivery Address (dict)
delivery_address = {
    "House No": input("Enter your house/flat no: "),                              
    "Street": input("Enter your street/area: "),                    
    "City": input("Enter your city: "),                
    "Country": input("Enter your country: ")                
}

# Payment Methods (dict)
payment_methods = {
    "Primary": input("Enter your primary payment method: "),             
    "Backup": input("Enter your backup payment method: ")      
}

# Wallet Balance (float)
wallet_balance = float(input("Enter your Flipkart Wallet balance (₹): "))

# Notifications (bool)
notif_input = input("Do you want to receive notifications? (yes/no): ").strip().lower()
notifications_enabled = notif_input == "yes"  # Converts to boolean

# --- Display Flipkart Profile ---
print("\n--- Flipkart Profile Summary ---\n")

print(f"Welcome to {app_name}")                                      
print(f"User ID: {user_id}")                                           
print(f"Name: {full_name}")                                            
print("Wallet Balance: ₹%.2f" % wallet_balance)            

print(f"Wishlist: {wishlist}")                                          
print(f"Last Order: {order_history[0]} worth ₹{order_history[1]}")     
print(f"Total Orders Completed: {total_orders}")                       
print(f"Items in Cart: {cart_items}")                                  
print(f"Reward Points (SuperCoins): {reward_points}")                  
print(f"Memberships: {memberships}")                                   

print("\nDelivery Address:")
for key, value in delivery_address.items():
    print(f" {key}: {value}")

print("\nPayment Methods:")
for key, value in payment_methods.items():
    print(f" {key}: {value}")

print(f"\nNotifications Enabled: {notifications_enabled}")             

# --- Flipkart Profile Example Output ---

'''
Welcome to Flipkart
Enter your Flipkart user ID: 50231
Enter your full name: Bhavana
Enter items in your wishlist (comma-separated): iphone, smartwatch, shoes
Enter your last ordered item: shoes
Enter the last order amount (in ₹): 1999
Enter total number of completed orders: 12
Enter number of items currently in your cart: 3
Enter your Flipkart SuperCoin balance: 120
Enter your memberships (comma-separated, e.g., Plus, SuperCoin): 120
Enter your house/flat no: 12-34
Enter your street/area: MG road
Enter your city: hyderabad
Enter your country: india
Enter your primary payment method: UPI
Enter your backup payment method: credit card
Enter your Flipkart Wallet balance (₹): 2500
Do you want to receive notifications? (yes/no): yes

--- Flipkart Profile Summary ---

Welcome to Flipkart
User ID: 50231
Name: Bhavana
Wallet Balance: ₹2500.00
Wishlist: ['iphone', 'smartwatch', 'shoes']
Last Order: shoes worth ₹1999.0
Total Orders Completed: 12
Items in Cart: 3
Reward Points (SuperCoins): 120
Memberships: {'120'}

Delivery Address:
 House No: 12-34
 Street: MG road
 City: hyderabad
 Country: india

Payment Methods:
 Primary: UPI
 Backup: credit card

Notifications Enabled: True'''






