# Задача 9. Вариант 9.
# Создайте  игру,   в   которой компьютер   выбирает    какое-либо  слово,  а   игрок   должен его  отгадать.

# Galizin I.V.
# 22.04.2017

import random

WORDS=("стул", "ручка", "аппликация", "кружка")
# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
length=len(word)

# начало игры
print(
"""
Добро пожаловать в игру 'Отгадай слово'!
Надо угадать, какое слово загадал компьютер.
(Для выхода нажмите Enter. не вводя своей версии.)
"""
)

# отметка, сколько было подсказок
adviced=0

print("Количество букв загаданного слова: " + str(length))
print("Сейчас вы можете спросить компьютер, есть ли в слове любая из букв алфавита:")
while adviced < 5:
    char=input("Введите букву: ")
    if char == "":
        break;
    if word.find(char) > -1:
        print("Буква " + char + " есть в слове!")
    else:
        print("Буквы " + char + " в слове нет!")
    adviced = adviced + 1


if char != "":
    guess = input("Попробуйте отгадать исходное слово: ")

    while (guess != word or guess == "") and char != "":
        if guess == "":
            break
        print("K сожалению. вы неправы.")
        guess = input("Попробуйте отгадать исходное слово: ")

    if guess == word:
        print("Дa. именно так! Вы отгадали! Слово: " + word)

print("Cnacибo за игру.")
input("Haжмитe Enter. чтобы выйти.")