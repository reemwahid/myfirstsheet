fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

#for fruit, price in fruitPrices.items():

def buyLotsOfFruit(orderList):
    totalCost = 0.0           
    for order in orderList:
        fruit, multiplier = order;
        totalCost += fruitPrices[fruit] * multiplier;          
    return totalCost
    
# Main Method    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    buyLotsOfFruit(orderLis print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList)