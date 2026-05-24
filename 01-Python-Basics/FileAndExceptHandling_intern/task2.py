f = open("sample.txt", "r")
data = f.read()
word = input("Enter word to search: ")
if word in data:
    print(word, "found in file")
else:
    print(word, "not found in file")
f.close()