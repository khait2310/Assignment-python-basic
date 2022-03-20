import random
import string

upper = [random.choice(string.ascii_uppercase) for _ in range(3)]
lower = [random.choice(string.ascii_lowercase) for _ in range(3)]
spec = [random.choice('!@#$%^&*') for _ in range(2)]
digit = [random.choice(string.digits) for _ in range(3)]
dictionary = upper+lower+spec+digit

random.shuffle(dictionary)
print("".join(dictionary))