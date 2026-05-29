import random
import json
import os


def zagruz():
    if os.path.exists("stat.json"):
        with open("stat.json", "r") as f:
            return json.load(f)
    return {"win": 0, "lose": 0, "draw": 0}


def sohran(s):
    with open("stat.json", "w") as f:
        json.dump(s, f)


def igra(p, c):
    if p == c:
        return "draw"
    if (p == "камень" and c == "ножницы") or (p == "ножницы" and c == "бумага") or (p == "бумага" and c == "камень"):
        return "win"
    return "lose"


print("=" * 40)
print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
print("=" * 40)

s = zagruz()
name = input("Твое имя: ")

spisok = ["камень", "ножницы", "бумага"]

while True:
    print(f"\nСчет: {name} - {s['win']} | Комп - {s['lose']} | Ничьи - {s['draw']}")
    print("\n1-камень 2-ножницы 3-бумага 0-выход")

    try:
        v = int(input("Выбор: "))
    except:
        print("Ошибка! Введи число")
        continue

    if v == 0:
        print(f"\nИтог: {s['win']} побед, {s['lose']} поражений, {s['draw']} ничьих")
        sohran(s)
        break

    if v not in [1, 2, 3]:
        print("Введи 1,2,3 или 0")
        continue

    p = spisok[v - 1]
    c = random.choice(spisok)

    print(f"\n{name}: {p}")
    print(f"Компьютер: {c}")

    rez = igra(p, c)

    if rez == "win":
        print("Ты выиграл!")
        s["win"] += 1
    elif rez == "lose":
        print("Компьютер выиграл!")
        s["lose"] += 1
    else:
        print("Ничья!")
        s["draw"] += 1

input("\nEnter...")