# Dictionaries
# A dictionary is a collection which is unordered, changeable and indexed
# In Python dictionaries are written with curly brackets{}, and they have keys and values.
# Syntax: {key:value, key2:value2}
# Unlike Tuples, you can modify the values here, like this, dictionary_name['key']= new_value 
# To print only the keys, 
# for i in dictionary_name: 
#   print(i) 
# To print only the values, 
# for i in dict_name: 
#   print(dict_name[i]) 
# To print both key and value, 
#   for i,j in dict_name.items(): 
#   print(i,j) 

dict_random = {1:'one', 2: 'two', 3: 'three'}
for i in dict_random:
    print(i)
for i in dict_random:
    print(dict_random[i])
for i,j in dict_random.items():
    print(i,j)
print(len(dict_random))
dict_random[4] = 'four'
for i,j in dict_random.items():
    print(i,j)




# num.update({5: 'five'})