"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
sales = float(input("Enter Sales: $"))

while sales < 1:
    sales = float(input("Invalid Number. Please enter an ammount above 1.Enter Sale: $"))
if sales < 1000:
    bonus = sales*0.1
else:
    bonus = sales*0.15

print("Your bonus for this sale is $"+str(bonus))
