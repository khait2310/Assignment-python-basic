list_file = ['/Users/viet_tran/Documents/applications.txt', '/Users/viet_tran/Documents/collections.txt',
'/Users/viet_tran/Documents/trainees.txt']
result = []
for l in list_file:
    result.append(l[l.rfind('/')+1:])
print(result)