
food = ["Tandoori Chicken","Vegan Burger","Truffle Cake"]
prices = [240,320,900]


myorderFood = []
myorderCost = []
counter = 0
TotalCost = 0


print("Welcome to Mc Donalds")

order = input("Can I take your order?")
if order =="No":
    exit()
else:
    print("Thank You")
       
    
    nextOrder = True
    while nextOrder == True:
        foodOrder = input("Please enter item: ")
        if foodOrder == "Tandoori Chicken":
            myorderFood.append(food[0])
            myorderCost.append(prices[0])
            counter += 1
            TotalCost += prices[0]

        elif foodOrder == "Vegan Burger":
            myorderFood.append(food[1])
            myorderCost.append(prices[1])
            counter += 1
            TotalCost += prices[1]

        elif foodOrder == "Truffle Cake":
            myorderFood.append(food[2])
            myorderCost.append(prices[2])
            counter += 1
            TotalCost += prices[2]

        else:
            print("Not in Menu")

        finished = input("Have you finished ordering: Y/N: ")
        if finished == "N":
            nextOrder = True
        else:
            nextOrder = False
        
print(myorderFood)
print(myorderCost)
print(counter)

y = 0
print("Here is your order: ")
print(" ")
print("**********")
while(y<counter):
    print("Item: ",(myorderFood[y]))
    print("Cost: INR",str(myorderCost[y]))
    y+=1
print()    
print("TotalCost: INR",TotalCost)


Welcome to Mc Donalds
Can I take your order?Yes 
Thank You
Please enter item: Tandoori Chicken
Have you finished ordering: Y/N: N
Please enter item: Vegan Burger
Have you finished ordering: Y/N: Y
['Tandoori Chicken', 'Vegan Burger']
[240, 320]
2
Here is your order: 
 
**********
Item:  Tandoori Chicken
Cost: INR 240
Item:  Vegan Burger
Cost: INR 320

TotalCost: INR 560