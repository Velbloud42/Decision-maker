import random
import time
import os
ascii = """
┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┓━━━━━━━━━
┗┓┏┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━━━━━
━┃┃┃┃┏━━┓┏━━┓┏┓┏━━┓┏┓┏━━┓┏━┓━━━━━┏┓┏┓┏━━┓━┃┃┏┓┏━━┓┏━┓
━┃┃┃┃┃┏┓┃┃┏━┛┣┫┃━━┫┣┫┃┏┓┃┃┏┓┓━━━━┃┗┛┃┗━┓┃━┃┗┛┛┃┏┓┃┃┏┛
┏┛┗┛┃┃┃━┫┃┗━┓┃┃┣━━┃┃┃┃┗┛┃┃┃┃┃━━━━┃┃┃┃┃┗┛┗┓┃┏┓┓┃┃━┫┃┃━
┗━━━┛┗━━┛┗━━┛┗┛┗━━┛┗┛┗━━┛┗┛┗┛━━━━┗┻┻┛┗━━━┛┗┛┗┛┗━━┛┗┛━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""" 

#funkce
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def wait():
    time.sleep(3)
def vsldkj():
    print("Výsledek je: ")

#fáze 1
clear()
print(ascii)
print("""
2- dvě věci na rozhodování
3- tři věci na rozhodování
4- čtyři věci na rozhodování
5- pět věcí na rozhodování
6- šest věcí na rozhodování
7- sedm věcí na rozhodování
8- osm věcí na rozhodování
9- devět věcí na rozhodování
10- deset věcí na rozhodování
""")
a = input("sem piš číslo: ")
clear()

#varianta 2
if a == "2":
    b = input("1. ")
    c = input("2. ")
    vrjnt1 = [b, c]
    rndm2 = random.choice(vrjnt1)
    clear()
    vsldkj()
    print()
    print(rndm2)
    print()
    wait()

#varianta 2
if a == "3":
    d = input("1. ")
    e = input("2. ")
    f = input("3. ")
    vrjnt2 = [d, e, f]
    rndm3 = random.choice(vrjnt2)
    clear()
    vsldkj()
    print()
    print(rndm3)
    print()
    wait()

#varianta 3
if a == "4":
    g = input("1. ")
    h = input("2. ")
    i = input("3. ")
    j = input("4. ")
    vrjnt3 = [g ,h, i, j]
    rndm4 = random.choice(vrjnt3)
    clear()
    vsldkj()
    print(rndm4)
    print()
    wait()    

#varianta 4
if a == "5":
    k = input("1. ")
    l = input("2. ")
    m = input("3. ")
    n = input("4. ")
    o = input("5. ")
    vrjnt4 = [k, l, m, n, o]
    rndm5 = random.choice(vrjnt4)
    clear()
    vsldkj()
    print(rndm5)
    print()
    wait()

#varianta 5
if a == "6":
    p = input("1. ")
    q = input("2. ")
    r = input("3. ")
    s = input("4. ")
    t = input("5. ")
    u = input("6. ")
    vrjnt5 = [p, q, r, s, t, u]
    rndm6 = random.choice(vrjnt5)
    clear()
    vsldkj()
    print(rndm6)
    print()
    wait()

#varianta 7
if a == "7":
    v = input("1. ")
    w = input("2. ")
    x = input("3. ")
    y = input("4. ")
    z = input("5. ")
    A = input("6. ")
    B = input("7. ")
    vrjnt6 = [v, w, x, y, z, A, B]
    rndm7 = random.choice(vrjnt6)
    clear()
    vsldkj()
    print(rndm7)
    print()
    wait()

#varianta 8
if a == "8":
    C = input("1. ")
    D = input("2. ")
    E = input("3. ")
    F = input("4. ")
    G = input("5. ")
    H = input("6. ")
    I = input("7. ")
    J = input("8. ")
    vrjnt7 = [C, D, E, F, G, H, I, J]
    rndm8 = random.choice(vrjnt7)
    clear()
    vsldkj()
    print(rndm8)
    print()
    wait()

#varianta 9
if a == "9":
    K = input("1. ")
    L = input("2. ")
    M = input("3. ")
    N = input("4. ")
    O = input("5. ")
    P = input("6. ")
    Q = input("7. ")
    R = input("8. ")
    S = input("9. ")
    vrjnt8 = [K, L, M, N, O, P, Q, R, S]
    rndm9 = random.choice(vrjnt8)
    clear()
    vsldkj()
    print(rndm9)
    print()
    wait()

#varianta 10
if a == "10":
    T = input("1. ")
    U = input("2. ")
    V = input("3. ")
    W = input("4. ")
    X = input("5. ")
    Y = input("6. ")
    Z = input("7. ")
    AB = input("8. ")
    CD = input("9. ")
    EF = input("10. ")
    vrjnt9 = [T, U, V, W, X, Y, Z, AB, CD, EF]
    rndm10 = random.choice(vrjnt9)
    clear()
    vsldkj()
    print(rndm10)
    print()
    wait()