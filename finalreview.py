def mastermind(x,y):
    i = 0
    j = 0
    same_pos = 0
    same_val = 0
    nope = []
    while j < len(x):
        if x[i] == y[j]:
            same_pos += 1
        i+=1
        j+=1
    for z in x:
        for h in y:
            if z == h and z not in nope:
                same_val += 1
                nope.append(z)
 

    print("There is %s exact match(es)" % same_pos)
    print("A common value appears %s time(s)" % same_val)

def prime(num):
    prime = True
    if num == 2 or num == 3:
        return prime
    if num < 2:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            prime = False
    return prime
    
    
def money(x):
    str(x)
    dollars =""
    for i in x:
        if not i == ".":
            dollars +=i
        if i == ".":
            
            dollars *=100

def mode(x):
    temp = [0 for i in range(-100,101)]
    for a in x:
        temp[a]+=1
    mode = max(temp)
    for i in range(len(temp)):
        if temp[i] == mode:
            return i

def make_Y(n):   # n is odde
    a = []
    for i in range(n):
        a.append([False]*n)

    for i in range(n):
        if (i <= n//2):
            a[i][i] = True
            a[i][n-1-i] = True
        else:
            a[i][n//2] = True

    return a

def print_matrix(a):
    for row in a:
        for element in row:
            if element:
                print ("*", end=" ")
            else:
                print (".", end=" ")
        print()

def count(lst):
    n = len(lst)
    temp = [0]*n
    for val in lst:
        if val >= n:
            return False
        temp[val] +=1
    for val in temp:
        if val == 0:
            return False
    return True
        
