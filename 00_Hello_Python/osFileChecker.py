import os

directoryPath = 'e:/Python-Practice/'

content = os.listdir(directoryPath)

file = "hello"

path = os.path.join(directoryPath, file)

os.remove(path)

for item in content:
        print(item)