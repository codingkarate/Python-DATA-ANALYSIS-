while True:
    name = input("Enter your name: ")
    total = 0
    while True:
        q = int (input("Enter quantity: "))
        amt = int(input("Enter amt per product: "))
        total += amt*q
        repeat = input("Do you want to add product? (y/n) ")
        if repeat == "y":
            continue
        else: 
            break
    print("your invoice\n")
    print(total,"\n")
    print("Thank you for visiting us \n", name)
    repeat1 = print("Do you want to go to the next customer? y/n")
    if repeat1 == "y":
        continue
    else:
        break
    
