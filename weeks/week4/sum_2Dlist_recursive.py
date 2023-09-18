def main():
    list1= [[2, 1, 3], [4, 9, 8],[6, 2, 7]]
    list2= [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
    #print(recursive_sum(list1, list2))

    rec_list=(recursive_sum(list1,list2))
    for i in rec_list:
        print(i)

def recursive_row_sum(m, i, j):
    if j == len(m[i]):
        return 0
    else:
        return m[i][j] + recursive_row_sum(m, i, j+1)

def recursive_col_sum(m, i, j):
    if i == len(m):
        return 0
    else:
        return m[i][j] + recursive_col_sum(m, i+1, j)

def recursive_sum(m, n):
    for i in range(len(m)):
        for j in range(len(m[i])):
            cell=recursive_row_sum(m, i, j) + recursive_col_sum(m, i, j)
            n[i][j]= cell

    return n
    
main()





