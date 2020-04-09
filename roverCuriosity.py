from random import choice, randint, uniform
from time import sleep
import math

proxima_expedicao = []


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


def discenir_item(item):
    if item['tipo'] == 'metalico' or item['tipo'] == 'nao-metalico':
        return 'lixo'
    return 'rocha'


def valida_item(item, objeto):
    if(item == 'rocha'):
        if(objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.74):
            return True
    elif objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.3:
        return True


def coleta_item(item, objeto, Curiosity):
    if (Curiosity.capacidade + objeto['peso']) < 70.0:
        if item == 'rocha':
            if(objeto['tipo'] == 1):
                Curiosity.deposito_rocha['tipo_1'].append(objeto)
                Curiosity.capacidade += objeto['peso']
            if(objeto['tipo'] == 2):
                Curiosity.capacidade += objeto['peso']
                Curiosity.deposito_rocha['tipo_2'].append(objeto)
            else:
                Curiosity.capacidade += objeto['peso']
                Curiosity.deposito_rocha['tipo_3'].append(objeto)
        else:
            equilibra_lixos(objeto, Curiosity)
        return True


def equilibra_rochas(Curiosity):

    tipo_1 = len(Curiosity.deposito_rocha['tipo_1'])
    tipo_2 = len(Curiosity.deposito_rocha['tipo_2'])
    tipo_3 = len(Curiosity.deposito_rocha['tipo_3'])

    base = min(tipo_1, tipo_2, tipo_3)

    while(tipo_1 > base):
        Curiosity.capacidade -= Curiosity.deposito_rocha['tipo_1'][0]['peso']
        del Curiosity.deposito_rocha['tipo_1'][0]
        tipo_1 -= 1

    while(tipo_2 > base):
        Curiosity.capacidade -= Curiosity.deposito_rocha['tipo_2'][0]['peso']
        del Curiosity.deposito_rocha['tipo_2'][0]
        tipo_2 -= 1

    while(tipo_3 > base):
        Curiosity.capacidade -= Curiosity.deposito_rocha['tipo_3'][0]['peso']
        del Curiosity.deposito_rocha['tipo_3'][0]
        tipo_3 -= 1


def equilibra_lixos(objeto, Curiosity):
    while len(Curiosity.deposito_lixo) > 0:
        ultimo_lixo = Curiosity.deposito_lixo[len(Curiosity.deposito_lixo) - 1]
        if ultimo_lixo['tipo'] == objeto['tipo']:
            lixo_removido = Curiosity.deposito_lixo.pop()
            Curiosity.capacidade -= lixo_removido['peso']
        else:
            Curiosity.deposito_lixo.append(objeto)
            break
    Curiosity.deposito_lixo.append(objeto)
    Curiosity.capacidade += objeto['peso']


def Curiosity_aviso_capacidade():
    sleep(0.5)
    print('---------------------------------------------------------------------')
    print('Capacidade maxima atingida!')
    print('---------------------------------------------------------------------')
    sleep(1)
    print('Curiosity esta equilibrando os tipos de rochas!')
    sleep(1)
    print('Equilibrio concluido!')
    sleep(1)
    print('---------------------------------------------------------------------')
    sleep(1)


def Curiosity_aviso_coleta(item, objeto, Curiosity):
    sleep(0.05)
    print('Curiosity coletou {}: {} | capacidade: {}'.format(
        item, objeto, Curiosity.capacidade))


def valida_equilibrio(n1, n2, n3):
    if (n1 - 1) == n2 and n2 == n3 or (n1 + 1) == n2 and n2 == n3:
        return True
    if (n2 - 1) == n1 and n1 == n3 or (n2 + 1) == n1 and n1 == n3:
        return True
    if (n3 - 1) == n2 and n2 == n1 or (n3 + 1) == n2 and n2 == n1:
        return True


def valida_expedicao(Curiosity):
    deposito_1 = len(Curiosity.deposito_rocha['tipo_1'])
    deposito_2 = len(Curiosity.deposito_rocha['tipo_2'])
    deposito_3 = len(Curiosity.deposito_rocha['tipo_3'])

    if(Curiosity.capacidade > 69.5):
        if(valida_equilibrio(deposito_1, deposito_2, deposito_3)):
            return True
        else:
            return False


def encerra_expedicao(Curiosity):
    lixos = Curiosity.deposito_lixo
    rochas = Curiosity.deposito_rocha
    total_rochas = rochas['tipo_1'] + rochas['tipo_2'] + rochas['tipo_3']
    sleep(1)
    print('===================================================')
    print('Expedicao encerrada!')
    print('---------------------------------------------------')
    sleep(1)
    print('Emitindo relatorio...')
    sleep(1)
    print('===================================================')
    print('Total de rochas: {}'.format(len(total_rochas)))
    print('Rochas tipo 1: {}'.format(len(rochas['tipo_1'])))
    print('Rochas tipo 2: {}'.format(len(rochas['tipo_2'])))
    print('Rochas tipo 3: {}'.format(len(rochas['tipo_3'])))
    print('===================================================')
    print('Total de lixo: {}'.format(len(lixos)))
    print('Lixo metalico: {}'.format(len(lixos)))
    print('Lixo nao-metalico: {}'.format(len(lixos)))
    print('===================================================')
    sleep(1)
    print('Dirigindo-se a estacao espacial mais proxima')
    print('---------------------------------------------------')
    sleep(2)
    print('Curiosity terminou exploracao. Liberando espaco de armazenamento')
    print('---------------------------------------------------')
    sleep(2)
    print('Carga liberada!')
    print('---------------------------------------------------')
    sleep(1)
    print('Curiosity esta pronto para uma nova expedicao!')
    print('===================================================')


def gera_lista_rocha():
    lista = []
    for c in range(randint(1000, 10001)):
        rocha = Rocha()
        lista.append(
            {'peso': rocha.peso, 'diametro': rocha.diametro, 'tipo': rocha.tipo})
    return lista


def gera_lista_lixo():
    lista = []
    for c in range(randint(1000, 1001)):
        lixo = Lixo()
        lista.append(
            {'peso': lixo.peso, 'diametro': lixo.diametro, 'tipo': lixo.tipo})
    return lista


def inicia_expedicao(quantidade):
    for expedicao in range(quantidade):
        robo = Curiosity()
        solo_marte = (gera_lista_rocha() + gera_lista_lixo())
        for item in range(len(solo_marte)):
            if(item % 2):
                item_encontrado = solo_marte[0]
                del solo_marte[0]
            else:
                item_encontrado = solo_marte.pop()
            item = discenir_item(item_encontrado)
            if robo.capacidade >= 69.5:
                equilibra_rochas(robo)
                Curiosity_aviso_capacidade()

            if valida_item(item, item_encontrado):
                if(coleta_item(item, item_encontrado, robo)):
                    Curiosity_aviso_coleta(item, item_encontrado, robo)

            if valida_expedicao(robo) == True:
                break
        encerra_expedicao(robo)


inicia_expedicao(3)
