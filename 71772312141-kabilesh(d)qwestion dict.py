#calculate total bill amount
prices={'botties':30,'tiffin':100,'bag':400,'bicycle':2000}
stock={'botties':10,'tiffin':8,'bag':1,'bicycle':5}
total=0
for key in prices:
    value=prices[key]*stock[key]
    total+=value
print(total)
print('total bill amount=',total)
output:
bottles 300
tiffin 800
bag 400
bicycle 10000
total bill amount=11500
