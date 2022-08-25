# 2.Write a Python program to find the sum of all items in a dictionary?
dic = {"a":15,"b":"kamal","c":15,"d":29,"e":23,"f":"raj"}
sum = 0
for i in dic.values():
    if type(i) == int:
        sum = sum+i
    else:
        pass
print(sum)


