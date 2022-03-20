n = int(input("input n: "))
result = list()
for i in range(2, n+1):
    test = True
    for u in result:
        if i%u == 0:
            test = False
            break
    if test == True: result.append(i)
result.insert(0,1)
print(result)