from random import randint
import numpy as np

'''
i = number of row
j = number of column
S = sudoku list
'''

def busyColumn(i,j,S):
    for m in range(0,9):
        if m==i:        #if m==i, not interested in the value cause doing column
            continue
        if S[m][j]==S[i][j]:
            return True #means the culumn is busy(occupied)
    return False #means column not busy

def busyRow(i,j,S): #same explanation as row
    for n in range(0,9):
        if n==j:
            continue
        if S[i][n]==S[i][j]:
            return True
    return False

def busyBos(i,j,S):
    if i>=0 and i<=2 and j>=0 and j<=2: #first 3x3 matrix
        for m in range(0,3):
            for n in range(0,3):
                if m==i and n==j:
                    continue    #skip iteration
                if S[m][n]==S[i][j]: #have found repeated value in the box
                    return True
        return False

    if i>=0 and i<=2 and j>=3 and j<=5:
        for m in range(0,3):
            for n in range(3,6):
                if m==i and n==j:
                    continue    #skip iteration
                if S[m][n]==S[i][j]: #have found repeated value in the box
                    return True
        return False

    if i>=0 and i<=2 and j>=6 and j<=8:
        for m in range(0,3):
            for n in range(6,9):
                if m==i and n==j:
                    continue    #skip iteration
                if S[m][n]==S[i][j]: #have found repeated value in the box
                    return True
        return False

    if i >= 3 and i <= 5 and j >= 0 and j <= 2:  # first 3x3 matrix
        for m in range(3, 6):
            for n in range(0, 3):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

    if i >= 3 and i <= 5 and j >= 3 and j <= 5:
        for m in range(3, 6):
            for n in range(3, 6):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

    if i >= 3 and i <= 5 and j >= 6 and j <= 8:
        for m in range(3, 6):
            for n in range(6, 9):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

    if i >= 6 and i <= 8 and j >= 0 and j <= 2:  # first 3x3 matrix
        for m in range(6, 9):
            for n in range(0, 3):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

    if i >= 6 and i <= 8 and j >= 3 and j <= 5:
        for m in range(6, 9):
            for n in range(3, 6):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

    if i >= 6 and i <= 8 and j >= 6 and j <= 8:
        for m in range(6, 9):
            for n in range(6, 9):
                if m == i and n == j:
                    continue  # skip iteration
                if S[m][n] == S[i][j]:  # have found repeated value in the box
                    return True
        return False

def sudoku(n): #n - number of elements to remove
    S = np.zeros([9,9],dtype=int)
    maxiter=100
    while True:
        flag1 =False
        flag2 =False
        for i in range(0,9):
            for j in range(0,9):
                count=1
                while count<maxiter:
                    k = randint(1,9)
                    S[i][j]= k
                    cond1 = busyColumn(i,j,S)
                    cond2 = busyRow(i,j,S)
                    cond3 = busyBos(i,j,S)
                    if cond1==False and cond2==False and cond3==False:
                        break
                    count+=1
                if count == maxiter:
                    flag1=True
                    break
            if flag1==True:
                flag2=True
                break
        if flag2==True:
            S=np.zeros([9,9],dtype=int)
        else:
            break
    #print(S)
    count = 1
    #print('\n')
    while count <=n:
        i = randint(0,8)
        j = randint(0,8)
        if S[i][j] == 0:
            continue
        else:
            S[i][j]=0
            count+=1
    print(S)

sudoku(25)