n = int(input("Введіть число n = "))
count = 0

while n >= 0:
    n -= 3
    count += 1

print("Цикл виконався разів:", count)
input()