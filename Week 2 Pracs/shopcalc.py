item_num = int(input("How many items would you like to enter?:"))
shopping_list = []

for i in range(0,item_num):
    item_cost = float(input("Please enter the item cost in $:"))
    while item_cost <= 0:
        item_cost = float(input("Please enter an amount above $0"))
    shopping_list.append(item_cost)

total = sum(shopping_list)
if total >= 100:
    total = total * 0.90

print("The total cost of all items will be $"+ str(total))