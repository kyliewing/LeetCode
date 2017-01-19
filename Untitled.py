def print_board(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print (a[r][c],"\t",end="")

a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print_board(a)
