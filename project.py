import random

print("=" * 50)
print("     ИГРА: КАМЕНЬ - НОЖНИЦЫ - БУМАГА")
print("=" * 50)

name = input("\nВведите ваше имя: ")

hands = ["камень", "ножницы", "бумага"]

player_score = 0
computer_score = 0

while True:
    print("\n" + "-" * 40)
    print(f"Счёт: {name} - {player_score}  |  Компьютер - {computer_score}")
    print("-" * 40)

    print("\nВыберите ход:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")
    print("0 - Выйти из игры")

    try:
        choice = int(input("\nВаш выбор: "))
    except ValueError:
        print("Ошибка! Введите число 0, 1, 2 или 3")
        continue

    if choice == 0:
        print(f"\nИгра окончена! Финальный счёт: {name} - {player_score}  :  {computer_score} - Компьютер")

        if player_score > computer_score:
            print(f"Поздравляю, {name}, вы победили!")
        elif player_score < computer_score:
            print("Компьютер победил! В следующий раз повезёт!")
        else:
            print("Ничья!")
        break

    if choice not in [1, 2, 3]:
        print("Неверный выбор! Введите 1, 2, 3 или 0")
        continue

    player_hand = hands[choice - 1]

    computer_hand = random.choice(hands)

    print(f"\n{name} выбрал: {player_hand}")
    print(f"Компьютер выбрал: {computer_hand}")

    if player_hand == computer_hand:
        print("\nНичья!")
    elif (player_hand == "камень" and computer_hand == "ножницы"):
        print("\nВы выиграли этот раунд! Камень разбивает ножницы.")
        player_score += 1
    elif (player_hand == "ножницы" and computer_hand == "бумага"):
        print("\nВы выиграли этот раунд! Ножницы режут бумагу.")
        player_score += 1
    elif (player_hand == "бумага" and computer_hand == "камень"):
        print("\nВы выиграли этот раунд! Бумага накрывает камень.")
        player_score += 1
    else:
        print("\nКомпьютер выиграл этот раунд!")
        computer_score += 1

input("\nНажмите Enter для выхода...")