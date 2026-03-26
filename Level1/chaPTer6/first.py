items=[]
prices=[]
print("\n ****   Welcom to ishop calculator   ****\n")
number_of_items=int(input("How many items are there in your basket today\n"))

if number_of_items>0:
    print("\nLe's get to counting them...")
    for i in range(0,number_of_items):
        name=input(f"Please tell me the name of the item number{i+1}")
        items.append(name)
        price=float(input(f"What is the price of {name}\n$"))
        prices.append(price)
    choice=input("Would you like to see your entire basket items?").lower()
    if choice=="yes":
        print(items)
        see_price=input("Would you like to see how much it'll cost?").lower()
        if see_price=="yes":
            print(f"\n Buying these itmes will cost you :\n{sum(prices)}")
        else:
            input("Press Enter to exit")
    else:
        input("Press Enter to exit")

else:
    print("Seems you're not in the mood for shopping today :)")       