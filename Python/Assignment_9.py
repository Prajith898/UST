#9. Create a shopping cart for the below bakery_items using dictionary or list


#code
bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
cart={}
def view_items():
    print ("\n*** Items details  ***\n")
    print ("   Item    Price  \n")
    for i in  bakery_items:
        print("     ",i,"      ",bakery_items[i],"\n")
def add_item():
    item=input("Enter the item to be added in to the list\n")
    cart[item]=1
def remove_item():
    item=input("Enter the item to be removed from the list\n")
    del cart[item]
def view_cart():
    print("\n your cart :", cart)
def update():
    item=input("Enter the Item to be updated\n")
    q=int(input("\nEnter the quantity\n"))
    cart[item]=q
def bill():
    cost=0
    for i in cart.keys():
        cost=cost+cart[i]*bakery_items[i]
    print("\n Total amount to be paid :", cost)
    print
print(""" Enter choice
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill
            """)
i=True

while(i==True):
    print(""" Enter choice
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill
            """)
    opt=input(" \n")
    if opt=='1':
        view_items()
    elif opt=='2':
        add_item()
    elif opt=='3':
        view_cart()
    elif opt=='4':
        update()
    elif opt=='5':
        remove_item()
    elif opt=='6':
        bill()
        i=False
    else:
        print("Wrong choice, Enter the correct choice")


    
