file_names = ['/Users/viet_tran/Documents/applications.txt', '/Users/viet_tran/Documents/collections.txt',
'/Users/viet_tran/Documents/trainees.txt']

def extract(file_name):
    return file_name[file_name.rfind('/')+1:file_name.find('.')]

result = list(map(extract, file_names))
print(result)