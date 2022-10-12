A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, ],
    [6, 7, 3, ],
    [4, 5, 9, ]]
 
# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]
 
for r in result:
    print(r)