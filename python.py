from random import choice, randint, uniform
from time import sleep
import math


class Curiosity:

    def __init__(self):
        self.__deposito_rocha = {
            "tipo_1": [],
            "tipo_2": [],
            "tipo_3": []
        }
        self.__deposito_lixo = []
        self.__capacidade = 0

    @property
    def deposito_rocha(self):
        return self.__deposito_rocha

    @property
    def deposito_lixo(self):
        return self.__deposito_lixo

    @property
    def capacidade(self):
        return self.__capacidade


class Rocha:

    def __init__(self):
        self.__peso = round(uniform(0.5, 14.2), 1)
        self.__diametro = round(uniform(0.1, 5), 1)
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


def equilibra_rochas(Curiosity):

    tipo_1 = len(Curiosity.deposito_rocha['tipo_1'])
    tipo_2 = len(Curiosity.deposito_rocha['tipo_2'])
    tipo_3 = len(Curiosity.deposito_rocha['tipo_3'])

    base = min(tipo_1, tipo_2, tipo_3)

    while(tipo_1 > base):
        del Curiosity.deposito_rocha['tipo_1'][0]
        tipo_1 -= 1

    while(tipo_2 > base):
        del Curiosity.deposito_rocha['tipo_2'][0]
        tipo_2 -= 1

    while(tipo_3 > base):
        del Curiosity.deposito_rocha['tipo_3'][0]
        tipo_3 -= 1


def coleta_rocha(objeto, Curiosity):
    if(objeto['tipo'] == 1):
        Curiosity.deposito_rocha['tipo_1'].append(objeto)
    if(objeto['tipo'] == 2):
        Curiosity.deposito_rocha['tipo_2'].append(objeto)
    else:
        Curiosity.deposito_rocha['tipo_3'].append(objeto)


robo = Curiosity()
for i in range(10):
    rocha = Rocha()
    rocha = {"tipo": rocha.tipo, "diametro": rocha.diametro, "peso": rocha.peso}
    coleta_rocha(rocha, robo)
print(len(robo.deposito_rocha['tipo_1']))
print(len(robo.deposito_rocha['tipo_2']))
print(len(robo.deposito_rocha['tipo_3']))
print('------------------------------------')
equilibra_rochas(robo)
print('------------------------------------')
print(len(robo.deposito_rocha['tipo_1']))
print(len(robo.deposito_rocha['tipo_2']))
print(len(robo.deposito_rocha['tipo_3']))
print(robo.deposito_rocha)