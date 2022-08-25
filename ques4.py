# 4.	Write a Python program to convert key-values list to flat dictionary?
l = [("monu",24),("ram",28),("rahim",36),("jhon",32)]
d = {}
for (a,b) in l:
    d.setdefault(a,b)

print(d)