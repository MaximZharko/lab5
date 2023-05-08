list_of_nums = [5, 6, 2, 5, 3, 6, 7, 9, 1]
list_pairs = []

for num in list_of_nums:
    if num not in list_pairs:
        list_pairs.append(num)
    else:
        print(num)
