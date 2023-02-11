# Collection Data Types
# A list is a collection which is ordered and which can be changed. 
# List elements are enclosed with Square Brackets []. Eg: randomlist = ['one','two'] 
# List stores the values in an order. It start with an index 0. 
# To access the first element in the list, you have to use list[0]. 
# The first element is always stored in the index 0. 
# For traversing through a list, you can use a for loop. Eg: for i in list_name: print(i) 

randomList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in randomList:
    if(num % 2 == 0):
        print(num)
        