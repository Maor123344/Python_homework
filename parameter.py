amount = 0
while amount <= 100:
    num = int(input("please enter how many chocolate do you want "))
    if num > 100 :
        print("we dont have enough chocolate")
        break

    else:
          amount = amount + num
          stock = 100 - amount
          if stock < 0:
            print("we dont have enough chocolate")
            break
          if stock > 0:
           print(stock)
