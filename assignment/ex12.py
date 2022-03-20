n = input("input n: ")
count = 0
temp1, temp2 = 0, 1

if not type(n) is int:
    raise TypeError("n is not numeric")
n = int(n)
while count < n:
    print(temp1)
    temp = temp1 + temp2 
    temp1 = temp2
    temp2 = temp
    count += 1
