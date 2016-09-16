s1 ="paraparaparadise"
s2 = "paragraph"

f = lambda s: [s[i:i+2] for i in range(0, len(s), 2)]
x = f(s1)
y = f(s2)
print(x)
print(y)

union = set(x).union(y)
print("union:", union)

inter = set(x).intersection(y)
print("Intersection:", inter)

diff = set(x).difference(y)
print("diff:", diff)

f = lambda l: "se" in l
print("se in x:", f(x))
print("se in y:", f(y))
