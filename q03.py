s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = list()

for w in s.split(" "):
    l.append(len(w))

print(l)
