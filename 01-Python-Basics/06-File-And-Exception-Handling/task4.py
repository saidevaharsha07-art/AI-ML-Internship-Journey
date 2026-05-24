try:
    f = open("sample1.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("File does not exist")