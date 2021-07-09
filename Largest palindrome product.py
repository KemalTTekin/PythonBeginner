n = 0
c = []
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        print(a,b)
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
                c.append(n)
                break
print(c)
