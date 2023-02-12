# Tuples - A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets ().
# The only difference between List and Tuple is that you cannot modify the values of the list once created.
# That means you cannot add or remove elements to the tuple.

values = (100, 200, 300)

for num in values:
    print(num)
if (200 in values):
    print("Found!")
else:
    print("not Found!")

print(len(values))
