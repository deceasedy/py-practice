"""
Напишите программу, которая выводит на экран сообщение в «телеграфном» стиле: буквы сообщения должны появляться по одной с некоторой задержкой.
"""

from time import sleep

def type(text):
    prev = text
    tosend = ""
    while tosend != prev:
        print(tosend + '_', end = '\r'); sleep(0.2)
        tosend += text[0]; text = text[1:]
        print(tosend, end='\r'); sleep(0.2)

type("hello")