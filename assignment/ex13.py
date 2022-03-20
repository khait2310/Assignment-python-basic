import threading
import requests
import random
result = dict()
def thread_function():
    for _ in range(100):
        response = requests.get("https://passwordinator.herokuapp.com/generate")
        result[response.json()['data']]=random.choice([True, False])


threads = list()
for index in range(10):
    print("Main    : create and start thread ", index)
    x = threading.Thread(target=thread_function, args=())
    threads.append(x)
    x.start()

for thread in threads:
    thread.join()

print(result)
