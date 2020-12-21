revenue = int(input('Введите сумму выручки: '))
expenses = int(input('Введите сумму издержек: '))
profit = revenue - expenses
margin = (profit / revenue) * 0.10
if revenue > expenses:
    print('Вы работаете в прибыль: ', profit)
    print(f'Рентабельность выручки составляет:  {margin:.2f}%')
    workers = int(input('Введите количество работников '))
    print(f'{profit / workers:.1f}')
elif expenses > revenue:
    print('Вы работаете в убыток', profit)
elif revenue == expenses:
    print('Вы работаете в ноль', profit)
