# List comprehensions provide a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it.
# Syntax: [ expression for item in list if conditional ]

randomList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[print(i) for i in randomList if i % 2 != 0]
