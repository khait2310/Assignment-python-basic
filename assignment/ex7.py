lst = list(range(0,101))
even = [x for x in lst if x%2==0]
odd = [x for x in lst if x%2!=0]
print(even)
print(odd)