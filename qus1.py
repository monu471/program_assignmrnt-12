# 1.	Write a Python program to Extract Unique values dictionary values?
a = {"a":15,"b":36,"c":15,"d":29,"e":23,"f":15}
l = []
for i in a.values():
    if i in l:
        pass
    else:
        l.append(i)
print(l)