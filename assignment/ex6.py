input_str = input("input: ")

def hashcode(p=7):
    result = 0
    for i in range(len(input_str)):
        result = result*p + ord(input_str[i])*(i+1)
    return result


print(hashcode())





