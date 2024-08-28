col = [0,2,0,2]
col2 = [2,0,2,0]
def dropNums(col):
    for i in range(len(col)-2, -1, -1):
        if col[i] != 0:
            j = i
            while j+1<len(col) and col[j+1] == 0:
                j+=1
            col[j] = col[i]
            col[i] = 0
    return col

print(dropNums(col))
print(dropNums(col2))