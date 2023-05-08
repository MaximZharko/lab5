list_of_nums = [1, 2, 3, 4, 5]

print("Введите произвольное число")
num = int(input())
if num in list_of_nums:
    print(*list_of_nums)
    print(num)
    print("Поздравляю, Вы угадали число!")
else:
    print(*list_of_nums)
    print(num)
    print("Нет такого числа!")

