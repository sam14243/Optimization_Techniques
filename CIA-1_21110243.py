import random

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

def anagram(s1,s2,arr1,i,j,l1,l2,ms,mms):
    temp = 0
    #arr1 = arr
    #print('i: ',i, end = ' ')
    #print('j: ',j, end = ' ')
    #print()
    if ((i == l1 - 1) and (j == l2 - 1)):
        print(arr1)
        #for y in range(i):
            #for z in range(j):
                #print(arr1[y][z], end = ' ')
            #print()
        return arr1
    elif ((i != l2-1) and (j == l2-1)):
        if (s1[j - 1] == s2[i - 1]):
            arr1[i][j] = arr1[i-1][j-1] + ms
            #print(arr)
            anagram(s1,s2,arr1,i+1,1,l1,l2,ms,mms)
        else:
            temp = maximum(arr1[i-1][j-1] + mms, arr1[i-1][j] + mms, arr1[i][j-1] + mms);
            arr1[i][j] = temp;
            #print(arr)
            anagram(s1,s2,arr1,i+1,1,l1,l2,ms,mms)
    elif((j != l2-1)):
        if (s1[j - 1] == s2[i - 1]):
            arr1[i][j] = arr1[i-1][j-1] + ms
            #print(arr1[i][j])
            anagram(s1,s2,arr1,i,j+1,l1,l2,ms,mms)
        else:
            temp = maximum(arr1[i-1][j-1] + mms, arr1[i-1][j] + mms, arr1[i][j-1] + mms);
            arr1[i][j] = temp;
            #print(arr1[i][j])
            anagram(s1,s2,arr1,i,j+1,l1,l2,ms,mms)
    else:
        return arr
            
    '''elif ((j == l2-1) and (i == l2-1)):
        if (s1[j -1] == s2[i - 1]):
            arr[i][j] = arr[i-1][j-1] + ms
            anagram(s1,s2,arr,i+1,j+1,l1,l2,ms,mms)
        else:
            temp = maximum(arr[i-1][j-1] + mms, arr[i-1][j] + mms, arr[i][j-1] + mms);
            arr[i][j] = temp;
            anagram(s1,s2,arr,i+1,j+1,l1,l2,ms,mms)'''


def backtrack():
    maxu = maximum(arr1[i_max][j_max-1], arr1[i_max-1][j_max], arr1[i_max-1][j_max-1])
    
def generate():
    s = ""
    D = {'A':4,'C':4,'G':4, 'T':4}
    L = ['A', 'C', 'G', 'T']
    while(L != []):
        c = random.choice(L)
        if (D[c] > 0):
            #print(c)
            D[c] -= 1
            s+=c
        for i in L:
            if (D[i] == 0):
                L.remove(i)
    return s
s1 = generate()
s2 = generate()
l1 = len(s1) + 1
l2 = len(s2) + 1
arr1 = [[0]*l1]*l2
ms = 5
mms = -4
i = 1
j = 1
i_max = l1 - 1
j_max = l2 - 1
print(s1)
print(s2)
#a = maximum(1,2,3)
#print(a)
#print(arr[1][2])
arr = anagram(s1,s2,arr1,i,j,l1,l2,ms,mms)
#print(arr)



