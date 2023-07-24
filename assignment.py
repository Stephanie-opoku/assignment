# green = "\033[0;33m"


list = []
aa = 0
while aa != 6:
    aa = int(input('****pella store*** \n'
                '1. buy item \n'
                '2. view cart \n'
                '3. remove from cart \n'
                '4. make purchase \n'
                '5. about us \n' 
                '6. exit app \n\n'
                'choose option: '))
    if aa == 1:
      product = input("enter product: ")
      quantity =int(input("enter quantity of product: "))
      unit_price =int(input("enter unit price: "))
      list.append(product)
      print("an item is bought")
    elif aa == 2:
       print(list)
    elif aa == 3:
        out = input("enter product to be removed: ")
        if out in list:
            list.remove(out)
            print("item has been removed")
        else:
            print("item is not purchased")
    # elif aa == 4:
    #     if len(list)!= 0:
    #         for i in set:
    #          total = (unit_price * quantity)
    #          list = [total]
    #          print(f"total amount is, {total} cedis")
    #          payment = int(input("enter payment: "))
    #     elif payment == total:
    #          print("thank you shopping at pella's store")
    #     elif payment > total:
    #          balance = payment - total
    #          print(f"you will be given a balance of,{balance} cedis")
    #     elif payment < total:
    #          print("sorry, amount is insufficient to make purchase")
    #     else:
    #         print("no item was purchased")
    
    elif aa == 4:
        # if len(list) != 0:
        total = 500
        print(f"total price is {total} cedis ")
        payment = int(input("enter payment: "))
        if payment == total:
             print("thank you shopping at pella's store")
        elif payment > total:
             balance = payment - total
             print("thank you for shopping at pella's store")
             print(f"you will be given a balance of {balance} cedis")
        elif payment < total:
             print("sorry, amount is insufficient to make purchase, please try again.")
        # else:
            # print("no item has been purchased")
    elif aa == 5 : 
        print("welcome to pella's store.")
        print("please feel free to buy and make payment to every item bought")
    elif aa == 6:
      exit 
    else:
      print("invalid user option, try again") 
       
    
