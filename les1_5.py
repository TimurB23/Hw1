a = int(input("Введите результаты пробежки первого дня в км? "))
b = int(input("Введите общий желаемый результат в км ?"))
days = 1
while b - a > 0:
    a = a + (a / 100 * 10)
    days = days + 1
    print(f'{days}-й день: {a:.2f} km')

