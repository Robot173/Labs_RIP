#!/usr/bin/env python3
from librip.gen import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price2': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
for i in gen_random(2,5, 8):
    print(i, end = " ")
print (" ")
# Реализация задания 1
for i in field(goods, 'title', 'price2'):
    print(i, end = " ")