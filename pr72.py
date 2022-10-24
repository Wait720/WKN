a = input()[::-1]
b = " "
s = []
for i in a:
    if i != " ":
        b += i
    else:
        s.append(b)
        b = " "
s.append(b)
print(max(s, key=len))
