week_tuple = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

print("Сколько Вы хотите выходных?")
num = int(input())

weekends = []
work = []

for i in range(len(week_tuple) - num):
    work.append(week_tuple[i])

for i in range(len(week_tuple) - num, len(week_tuple)):
    weekends.append(week_tuple[i])

print("Ваши выходные дни:")
print(*weekends)
print("Ваши рабочие дни:")
print(*work)
