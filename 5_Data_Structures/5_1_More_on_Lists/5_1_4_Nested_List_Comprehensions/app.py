# -*- coding: UTF-8 -*-

# > The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.
# > Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# > The following list comprehension will transpose rows and columns:
print([[row[i] for row in matrix] for i in range(4)]) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# > As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# > which, in turn, is the same as:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# > In the real world, you should prefer built-in functions to complex flow statements.
# > The zip() function would do a great job for this use case:
print(list(zip(*matrix))) # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
# > See Unpacking Argument Lists for details on the asterisk in this line.