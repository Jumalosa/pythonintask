﻿#Задача 5. Вариант 3.
#Напишите программу, которая бы при запуске случайным образом отображала название одного из цветов радуги.
#Deryushkina A.B.
#15.03.2017

print("Программа случайным образом отображает название один из семи цветов радуги")
import random
color=random.randint(1,7)
if color ==1:
	print ("Вам выпал красный цвет радуги")
elif color ==2:
	print ("Вам выпал оранжевый цвет радуги")
elif color ==3:
	print ("Вам выпал желтый цвет радуги")
elif color ==4:
	print ("Вам выпал зеленый цвет радуги")
elif color ==5:
	print ("Вам выпал голубой цвет радуги")
elif color ==6:
	print ("Вам выпал синий цвет радуги")
elif color ==7:
	print ("Вам выпал фиолетовый цвет радуги")
input('\n\nНажмите enter для выхода')