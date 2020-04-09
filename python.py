from random import choice, randint, uniform
from time import sleep
import math


class Rocha:

    def __init__(self):
        self.__peso = round(uniform(0.5, 14.2), 1)
        self.__diametro = round(uniform(0.1, 1.0), 1)
        self.__tipo = randint(1, 3)

    @property
    def peso(self):
        return self.__peso

    @property
    def diametro(self):
        return self.__diametro

    @property
    def tipo(self):
        return self.__tipo


class Lixo:
    def __init__(self):
        self.__peso = round(uniform(1.12, 8.55), 2)
        self.__diametro = round(uniform(0.1, 1.0), 2)
        self.__tipo = choice(['metalico', 'nao-metalico'])

    @property
    def peso(self):
        return self.__peso

    @property
    def diametro(self):
        return self.__diametro

    @property
    def tipo(self):
        return self.__tipo


def gera_lista_rocha():
    lista = []
    for c in range(randint(1, 7)):
        rocha = Rocha()
        lista.append(
            {'peso': rocha.peso, 'diametro': rocha.diametro, 'tipo': rocha.tipo})
    return lista


def gera_lista_lixo():
    lista = []
    for c in range(randint(1, 7)):
        lixo = Lixo()
        lista.append(
            {'peso': lixo.peso, 'diametro': lixo.diametro, 'tipo': lixo.tipo})
    return lista


for c in range(3):
    solo_marte = (gera_lista_rocha() + gera_lista_lixo())
    print('=================================================')
    print(solo_marte)
    print('=================================================')
    for item in range(len(solo_marte)):
        if(item % 2):
            item_encontrado = solo_marte[0]
            del solo_marte[0]
        else:
            item_encontrado = solo_marte.pop()
        print(item_encontrado)