#!/usr/bin/env python3
# -*- config: utf-8 -*-

import pandas as pd
import numpy as np

# Использовать объект Series, содержащий следующие индексы: фамилия, имя; знак Зодиака;
# дата рождения (отдельный индекс для каждого из трех чисел). Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в DataFrame, с заданными
# колонками; вывод на экран информации о людях, родившихся под знаком, название
# которого введено с клавиатуры; если таких нет, выдать на дисплей соответствующее
# сообщение.


def add(iter_dat):
    temp_1 = input('Введите фамилию> ')
    temp_2 = input('Введите имя> ')
    temp_3 = input('Введите знак зодиака> ')
    temp_4 = input('Введите день рождения> ')
    temp_5 = input('Введите месяц рождения> ')
    temp_6 = input('Введите год рождения> ')
    dat_frame.loc[iter_dat] = [temp_1, temp_2, temp_3, temp_4, temp_5, temp_6]


def find():
    temp_f = input('Какой знак зодиака> ')
    print(f'\nЛюди по вашему запросу:\n{dat_frame[dat_frame["Знак зодиака"] == temp_f]}')


if __name__ == '__main__':
    first_ser = pd.Series(['Беляев', 'Виталий', 'Рак', '11', '07', '2002'],
                          ['Фамилия', 'Имя', 'Знак зодиака', 'День рождения', 'Месяц рождения', 'Год рождения'])
    iter_dat = 1
    dat_frame = pd.DataFrame(
        {
            'Фамилия': {iter_dat: first_ser['Фамилия']},
            'Имя': {iter_dat: first_ser['Имя']},
            'Знак зодиака': {iter_dat: first_ser['Знак зодиака']},
            'День рождения': {iter_dat: first_ser['День рождения']},
            'Месяц рождения': {iter_dat: first_ser['Месяц рождения']},
            'Год рождения': {iter_dat: first_ser['Год рождения']},
        }
    )
    while True:
        comm = input('Введите команду> ')
        if comm == 'add':
            iter_dat += 1
            add(iter_dat)
        elif comm == 'find':
            find()
        elif comm == 'help':
            print('Помощь\nДобавить человека - add\n'
                  'Найти людей по знаку зодиака - find\n'
                  'Показать таблицу - show\nПомощь - help'
                  'Выход - exit')
        elif comm == 'show':
            print(dat_frame)
        elif comm == 'exit':
            break
        else:
            print('Ошибка')
