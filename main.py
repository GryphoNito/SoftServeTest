import random

def guess(start, end, N):
    print(f"Вітаю я загадав число від {start} до {end}. Спробуйте вгадати його за {N} спроб.")
    random_number = random.randint(start, end)
    for i in range(0, N):
        print("Введіть ваше припущення: ", end='')
        number = int(input())
        if number > random_number:
            print("Занадто велике")
        elif number < random_number:
            print("Занадто маленьке")
        elif number == random_number:
            print(f"Ви вгадали! Це число {random_number}")
            return
    return f"На жаль Ви програли, загадане число - {random_number}"

guess(1, 100, 7)

