import numpy as np

def P(r,c,v,t): #Row,Column,Value,Turn
    if r == 0:
        if c == 0:
            if v == 0:
                return 'a' #Null en a11
            elif v == 1:
                return 'b' #O en a11
            elif v == 2:
                return 'c' #X en a11
        elif c == 1:
            if v == 0:
                return 'd' #Null en a12
            elif v == 1:
                return 'e' #O en a12
            elif v == 2:
                return 'f' #X en a12
        elif c == 2:
            if v == 0:
                return 'g' #Null en a13
            elif v == 1:
                return 'h' #O en a13
            elif v == 2:
                return 'i' #X en a13

    elif r == 1:
        if c == 0:
            if v == 0:
                return 'j' #Null en a21
            elif v == 1:
                return 'k' #O en a21
            elif v == 2:
                return 'l' #X en a21
        elif c == 1:
            if v == 0:
                return 'm' #Null en a22
            elif v == 1:
                return 'n' #O en a22
            elif v == 2:
                return 'o' #X en a22
        elif c == 2:
            if v == 0:
                return 'p' #Null en a23
            elif v == 1:
                return 'q' #O en a23
            elif v == 2:
                return 'r' #X en a23

    elif r == 2:
        if c == 0:
            if v == 0:
                return 's' #Null en a31
            elif v == 1:
                return 't' #O en a31
            elif v == 2:
                return 'u' #X en a31
        elif c == 1:
            if v == 0:
                return 'v' #Null en a32
            elif v == 1:
                return 'w' #O en a32
            elif v == 2:
                return 'x' #X en a32
        elif c == 2:
            if v == 0:
                return 'y' #Null en a33
            elif v == 1:
                return 'z' #O en a33
            elif v == 2:
                return 'aa' #X en a33
    print('Matriz mal planteada')
    return False

def Matrix2Formula(A):
    rows = len(A[:,0])
    columns = len(A[0,:])
    FirstRules = []
    print('Matriz de ' +  str(rows) + 'X' + str(columns))
    for r in range(rows):
        for c in range(columns):
            FirstRules.append(P(r,c,A[r,c],1))
    return FirstRules

def Dict2Matrix(dict):
    row1 = [0,0,0]
    row2 = [0,0,0]
    row3 = [0,0,0]
    for x in dict:
        #++++R_O_W_1+++++
        if x == 'a':
            if dict['a'] == 0:
                continue
            elif dict['a'] == 1:
                row1[0] = 0
        elif x == 'b':
            if dict['b'] == 0:
                continue
            elif dict['b'] == 1:
                row1[0] = 1
        elif x == 'c':
            if dict['c'] == 0:
                continue
            elif dict['c'] == 1:
                row1[0] = 2

        if x == 'd':
            if dict['d'] == 0:
                continue
            elif dict['d'] == 1:
                row1[1] = 0
        elif x == 'e':
            if dict['e'] == 0:
                continue
            elif dict['e'] == 1:
                row1[1] = 1
        elif x == 'f':
            if dict['f'] == 0:
                continue
            elif dict['f'] == 1:
                row1[1] = 2

        if x == 'g':
            if dict['g'] == 0:
                continue
            elif dict['g'] == 1:
                row1[2] = 0
        elif x == 'h':
            if dict['h'] == 0:
                continue
            elif dict['h'] == 1:
                row1[2] = 1
        elif x == 'i':
            if dict['i'] == 0:
                continue
            elif dict['i'] == 1:
                row1[2] = 2

        #++++R_O_W_2+++++
        if x == 'j':
            if dict['j'] == 0:
                continue
            elif dict['j'] == 1:
                row2[0] = 0
        elif x == 'k':
            if dict['k'] == 0:
                continue
            elif dict['k'] == 1:
                row2[0] = 1
        elif x == 'l':
            if dict['l'] == 0:
                continue
            elif dict['l'] == 1:
                row2[0] = 2

        if x == 'm':
            if dict['m'] == 0:
                continue
            elif dict['m'] == 1:
                row2[1] = 0
        elif x == 'n':
            if dict['n'] == 0:
                continue
            elif dict['n'] == 1:
                row2[1] = 1
        elif x == 'o':
            if dict['o'] == 0:
                continue
            elif dict['o'] == 1:
                row2[1] = 2

        if x == 'p':
            if dict['p'] == 0:
                continue
            elif dict['p'] == 1:
                row2[2] = 0
        elif x == 'q':
            if dict['q'] == 0:
                continue
            elif dict['q'] == 1:
                row2[2] = 1
        elif x == 'r':
            if dict['r'] == 0:
                continue
            elif dict['r'] == 1:
                row2[2] = 2

        #++++R_O_W_3++++
        if x == 's':
            if dict['s'] == 0:
                continue
            elif dict['s'] == 1:
                row3[0] = 0
        elif x == 't':
            if dict['t'] == 0:
                continue
            elif dict['t'] == 1:
                row3[0] = 1
        elif x == 'u':
            if dict['u'] == 0:
                continue
            elif dict['u'] == 1:
                row3[0] = 2

        if x == 'v':
            if dict['v'] == 0:
                continue
            elif dict['v'] == 1:
                row3[1] = 0
        elif x == 'w':
            if dict['w'] == 0:
                continue
            elif dict['w'] == 1:
                row3[1] = 1
        elif x == 'x':
            if dict['x'] == 0:
                continue
            elif dict['x'] == 1:
                row3[1] = 2

        if x == 'y':
            if dict['y'] == 0:
                continue
            elif dict['y'] == 1:
                row3[2] = 0
        elif x == 'z':
            if dict['z'] == 0:
                continue
            elif dict['z'] == 1:
                row3[2] = 1
        elif x == 'aa':
            if dict['aa'] == 0:
                continue
            elif dict['aa'] == 1:
                row3[2] = 2

    return np.array([row1,row2,row3])















letras = [chr(x) for x in range(97, 123)]
letras.append('aa')


#PRUEBA MATRIX TO FORMULA
a = np.array([[1,0,0], [2,1,0], [1,2,0]])
print(a[0,0])
print(len(a[0,:]))
print(len(a[:,0]))
FRules = Matrix2Formula(a)
print(FRules)



#PRUEBA DICT 2 MATRIX
dict1 = {'a': 0 , 'b' : 1 , 'c' : 0       ,      'd' : 1 , 'e' : 0 , 'f' : 0      ,     'g' : 1 , 'h' : 0 , 'i' : 0 ,
         'j': 0 , 'k' : 0 , 'l' : 1       ,      'm' : 0 , 'n' : 1 , 'o' : 0      ,     'p' : 1 , 'q' : 0 , 'r' : 0 ,
         's': 0 , 't' : 1 , 'u' : 0       ,      'v' : 0 , 'w' : 0 , 'x' : 1      ,     'y' : 1 , 'z' : 0 , 'aa' : 0 }

A = Dict2Matrix(dict1)
print(A)