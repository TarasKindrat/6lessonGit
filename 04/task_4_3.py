# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
number = CONFIG.find('1') # find position
slis_e = CONFIG[number:]

#print(slis_e)
list2 = []

list2 = (slis_e.strip().split(','))
print(list2)
