s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
c1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element = dict()

for i,w in enumerate(s.split(" ")):
    if i in c1:
        element[w[0]] = i+1
    else:
        element[w[0:2]] = i+1

print(element)
