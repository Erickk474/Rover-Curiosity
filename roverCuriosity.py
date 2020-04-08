from random import choice, randint, uniform
from time import sleep
import math

proxima_expedicao = []


class Rocha:

    def __init__(self):
        self.__peso = round(uniform(0.5, 14.2), 1)
        self.__diametro = round(uniform(0, 5), 1)
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
        self.__diametro = round(uniform(0, 5), 2)
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


def valida_capacidade(Curiosity, objeto):
    if Curiosity.capacidade <= 70:
        return True


def gera_item():
    n = choice([1, 2])
    if n == 1:
        gerou = Rocha()
        item = {
            "peso": gerou.peso,
            "diametro": gerou.diametro,
            "tipo": gerou.tipo
        }
    else:
        gerou = Lixo()
        item = {
            "peso": gerou.peso,
            "diametro": gerou.diametro,
            "tipo": gerou.tipo
        }

    return item


def discenir_item(item):
    if item['tipo'] == 'metalico' or item['tipo'] == 'nao-metalico':
        return 'lixo'
    return 'rocha'


def valida_item(item, objeto, Curiosity):
    if(item == 'rocha'):
        if(objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.74):
            return True
    elif objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.3:
        return True


def coleta_item(item, objeto, Curiosity):
    if (item == 'rocha'):
        if(objeto['tipo'] == 1):
            Curiosity.deposito_rocha['tipo_1'].append(objeto)
        if(objeto['tipo'] == 2):
            Curiosity.deposito_rocha['tipo_2'].append(objeto)
        else:
            Curiosity.deposito_rocha['tipo_3'].append(objeto)
    else:
        Curiosity.deposito_lixo.append(objeto)


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

robo = Curiosity()

while True:

    objeto = gera_item()
    item = discenir_item(objeto)
    if robo.capacidade <= 70:
        if valida_item(item, objeto, robo):
            coleta_item(item, objeto, robo)
            robo.capacidade += objeto['peso']
    else:
        break

equilibrio = equilibra_rochas(robo)


# print('rocha: ', robo.deposito_rocha)
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('lixo: ', robo.deposito_lixo)
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('capacidade', robo.capacidade)
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------------------------------------------------')
#print('tipo_1', len(robo.deposito_rocha['tipo_1']))
#print('tipo_2', len(robo.deposito_rocha['tipo_2']))
#print('tipo_3', len(robo.deposito_rocha['tipo_3']))


# print('equilibra rochas: ', equilibra_rochas(robo))
# while True:
# print(gera_item())
