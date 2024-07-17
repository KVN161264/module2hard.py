def password(n):
    key = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                key.append(f'{i}{j}')
    result = ''.join(key)
    return result
num = 0
while num < 3 or num > 20:
    num = int(input("Введите число для пароля от 3 до 20: "))
pass_1 = password(num)
print(f"Пароль для числа {num}: {pass_1}")