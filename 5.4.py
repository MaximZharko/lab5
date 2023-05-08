from random import  randint

group_1 = ("Ахмедов", "Жарко", "Ишин", "Ившина", "Ившина", "Васильев", "Шамбурова", "Финкельберг", "Мухин", "Бигалиев")
group_2 = ("Мухин", "Боровков", "Лахин", "Киселев", "Осипов", "Сакулина", "Назарова", "Небогатиков", "Полуянов", "Новикова")

nums_1 = []
nums_2 = []

while len(nums_1) != 5:
    num = randint(0, 9)
    if num not in nums_1:
        nums_1.append(num)

while len(nums_2) != 5:
    num = randint(0, 9)
    if num not in nums_2:
        nums_2.append(num)

new_tuple = ()
for num in nums_1:
    new_tuple += (group_1[num],)
for num in nums_2:
    new_tuple += (group_2[num],)

print(*group_1)
print(*group_2)
print(*new_tuple)
print(len(new_tuple))
new_tuple = tuple(sorted(new_tuple))
print(*new_tuple)
if "Иванов" in new_tuple:
    print(new_tuple.count("Иванов"))
else:
    print("Иванова нет")