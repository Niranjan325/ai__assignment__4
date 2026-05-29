from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')

digits = range(10)

for perm in permutations(digits, len(letters)):

    s,e,n,d,m,o,r,y = perm

    if s == 0 or m == 0:
        continue

    send = 1000*s + 100*e + 10*n + d
    more = 1000*m + 100*o + 10*r + e
    money = 10000*m + 1000*o + 100*n + 10*e + y

    if send + more == money:

        print("Solution Found")
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)

        print("\nMapping")
        print("S =", s)
        print("E =", e)
        print("N =", n)
        print("D =", d)
        print("M =", m)
        print("O =", o)
        print("R =", r)
        print("Y =", y)

        break
