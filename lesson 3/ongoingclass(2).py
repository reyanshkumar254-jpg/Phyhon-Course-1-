actualCost= float(input("Please Enter the Actual Products price:"))
sale_amount = float(input("Please Enter the Sales amount:")) 

if (sale_amount > actualCost):
    amount = sale_amount - actualCost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!")