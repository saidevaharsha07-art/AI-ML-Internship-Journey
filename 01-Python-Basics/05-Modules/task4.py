lst = [1, 2, 3, 4, 5, 6]
filtered_lst = list(filter(lambda x: x % 2 == 0, lst))
squared_lst = list(map(lambda x: x ** 2, filtered_lst))
print("Filtered List (Even Numbers):", filtered_lst)
print("Squared List (Even Numbers):", squared_lst)