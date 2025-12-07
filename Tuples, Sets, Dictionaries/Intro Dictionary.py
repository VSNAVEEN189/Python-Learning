# Comma separated key-value pairs enclosed within {}
groceries = {'milk': 60, 'biscuits': 20, 'rice' : 90, 'bread': 30}
print(groceries)
print(type(groceries))
print(len(groceries))
print(groceries['milk'])

#To modify
groceries['milk'] = 65
print(groceries)

groceries['eggs'] = 10   #Adding new key value pair
groceries['bread'] = 35  #If key is present it updates the key
print(groceries)