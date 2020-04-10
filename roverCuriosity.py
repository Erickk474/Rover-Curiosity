from random import choice, randint, uniform, shuffle
from time import sleep
import math

# Armazena o lixo deixado por expedições passadas.
lixo_expedicao_passada = []

# Cria uma Rocha.
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

# Cria um Lixo espacial.
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

# Cria um Curiosity.
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

    @capacidade.setter 
    def atualiza_capacidade(self, valor): 
        self.__capacidade = valor

# Gera uma quantidade aleatória de rochas com propriedades de valores também aleatórios.
# Caso haja algum lixo espacial da expedição passada, o mesmo é adicionado e embaralhado na lista.
def gera_lista_rocha(lixo_expedicao_passada):
    lista = []
    for c in range(randint(1000, 10001)):
        rocha = Rocha()
        lista.append(
            {'peso': rocha.peso, 'diametro': rocha.diametro, 'tipo': rocha.tipo})
    if(len(lixo_expedicao_passada)):
        shuffle(lista)
    return lista

# Gera uma quantidade aleatória de lixo espacial com propriedades de valores também aleatórios.
def gera_lista_lixo():
    lista = []
    for c in range(randint(1000, 1001)):
        lixo = Lixo()
        lista.append(
            {'peso': lixo.peso, 'diametro': lixo.diametro, 'tipo': lixo.tipo})
    return lista

# Discerne o tipo do objeto encontrado, se uma rocha ou um lixo espacial.
def discenir_item(tipo_objeto):
    if tipo_objeto['tipo'] == 'metalico' or tipo_objeto['tipo'] == 'nao-metalico':
        return 'lixo'
    return 'rocha'

# Valida se o objeto encontrado possui valores aceitáveis para ser coletado.
def valida_objeto(tipo_objeto, objeto):
    if(tipo_objeto == 'rocha'):
        if(objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.74):
            return True
    elif objeto['peso'] <= 2.5 and objeto['diametro'] <= 0.3:
        return True

# Valida se o objeto pode ser coletado com a atual capacidade atual do Curiosity.
# Distingue o tipo do objeto encontrado, se lixo espacial ou rocha.
# Caso seja uma rocha, distingue o tipo de rocha e armazena.
# Caso seja um lixo espacial, a função 'equilibra_lixos' é acionada.
def coleta_objeto(tipo_objeto, objeto, Curiosity):
    if (Curiosity.capacidade + objeto['peso']) > 70.0:
        return False
    if tipo_objeto == 'rocha':
        if(objeto['tipo'] == 1):
            Curiosity.atualiza_capacidade = Curiosity.capacidade + objeto['peso']
            Curiosity.deposito_rocha['tipo_1'].append(objeto)
        if(objeto['tipo'] == 2):
            Curiosity.atualiza_capacidade = Curiosity.capacidade + objeto['peso']
            Curiosity.deposito_rocha['tipo_2'].append(objeto)
        else:
            Curiosity.atualiza_capacidade = Curiosity.capacidade + objeto['peso']
            Curiosity.deposito_rocha['tipo_3'].append(objeto)
    else:
        equilibra_lixos(objeto, Curiosity)
    return True

# Analisa a quantidade de cada tipo de rocha, encontra o tipo com menor quantidade e,
# elimina um por um até que a quantidade de todos os tipos de rocha estejam equivalentes.
# Atualiza a capacidade atual do Curiosity.
def equilibra_rochas(Curiosity):

    tipo_1 = len(Curiosity.deposito_rocha['tipo_1'])
    tipo_2 = len(Curiosity.deposito_rocha['tipo_2'])
    tipo_3 = len(Curiosity.deposito_rocha['tipo_3'])

    base = min(tipo_1, tipo_2, tipo_3)

    while(tipo_1 > base):
        Curiosity.atualiza_capacidade = Curiosity.capacidade - Curiosity.deposito_rocha['tipo_1'][0]['peso']
        del Curiosity.deposito_rocha['tipo_1'][0]
        tipo_1 -= 1

    while(tipo_2 > base):
        Curiosity.atualiza_capacidade = Curiosity.capacidade - Curiosity.deposito_rocha['tipo_2'][0]['peso']
        del Curiosity.deposito_rocha['tipo_2'][0]
        tipo_2 -= 1

    while(tipo_3 > base):
        Curiosity.atualiza_capacidade = Curiosity.capacidade - Curiosity.deposito_rocha['tipo_3'][0]['peso']
        del Curiosity.deposito_rocha['tipo_3'][0]
        tipo_3 -= 1

# Analisa o tipo do último lixo espacial adicionado, o tipo de lixo espacial encontrado e se é possível empilhar.
# Atualiza a capacidade atual do Curiosity.
def equilibra_lixos(objeto, Curiosity):
    while len(Curiosity.deposito_lixo) > 0:
        ultimo_lixo = Curiosity.deposito_lixo[len(Curiosity.deposito_lixo) - 1]
        if ultimo_lixo['tipo'] == objeto['tipo']:
            lixo_removido = Curiosity.deposito_lixo.pop()
            lixo_expedicao_passada.append(lixo_removido)
            Curiosity.atualiza_capacidade -= lixo_removido['peso']
        else:
            Curiosity.deposito_lixo.append(objeto)
            break
    Curiosity.deposito_lixo.append(objeto)
    Curiosity.atualiza_capacidade = Curiosity.capacidade + objeto['peso']

# Gera saídas de texto descrevendo a ação do Curiosity
def curiosity_aviso_capacidade():
    sleep(0.5)
    print('-'*50)
    print('Capacidade máxima atingida!')
    print('-'*50)
    sleep(1)
    print('Curiosity está equilibrando os tipos de rochas!')
    sleep(1)
    print('Equilibrio concluído!')
    sleep(1)
    print('-'*50)
    sleep(1)

# Gera saída de texto com informação sobre o objeto coletado.
def curiosity_aviso_coleta(tipo_objeto, objeto, Curiosity):
    sleep(0.05)
    print('Curiosity coletou {}: {} | capacidade atual: {}'.format(tipo_objeto, objeto, Curiosity.capacidade))

# Valida se as rochas estão mais ou menos equilibradas.
def valida_equilibrio(n1, n2, n3):
    if (n1 - 1) == n2 and n2 == n3 or (n1 + 1) == n2 and n2 == n3:
        return True
    if (n2 - 1) == n1 and n1 == n3 or (n2 + 1) == n1 and n1 == n3:
        return True
    if (n3 - 1) == n2 and n2 == n1 or (n3 + 1) == n2 and n2 == n1:
        return True

# Valida a expedição pode ser encerrada analisando os seguintes critério:
# - Se a capacidade do Curiosity está sendo comprometida.
# - Se as rochas estão equilibradas.
def valida_expedicao(Curiosity):
    deposito_1 = len(Curiosity.deposito_rocha['tipo_1'])
    deposito_2 = len(Curiosity.deposito_rocha['tipo_2'])
    deposito_3 = len(Curiosity.deposito_rocha['tipo_3'])

    if(Curiosity.capacidade > 69.5):
        if(valida_equilibrio(deposito_1, deposito_2, deposito_3)):
            return True
        else:
            return False

# Gera saídas de texto descrevendo a ação do Curiosity e os dados da expedição concluída.
def encerra_expedicao(Curiosity):
    lixos = Curiosity.deposito_lixo
    rochas = Curiosity.deposito_rocha
    contagem_lixo = soma_tipo_lixo(Curiosity.deposito_lixo)
    total_rochas = rochas['tipo_1'] + rochas['tipo_2'] + rochas['tipo_3']
    sleep(1)
    print('='*50)
    print('Expedicao encerrada!')
    print('-'*50)
    sleep(1)
    print('Emitindo relatorio...')
    sleep(1)
    print('='*50)
    print('Total de rochas: {}'.format(len(total_rochas)))
    print('Rochas tipo 1: {}'.format(len(rochas['tipo_1'])))
    print('Rochas tipo 2: {}'.format(len(rochas['tipo_2'])))
    print('Rochas tipo 3: {}'.format(len(rochas['tipo_3'])))
    print('='*50)
    print('Total de lixo: {}'.format(len(lixos)))
    print('Lixo metalico: {}'.format(contagem_lixo['metalico']))
    print('Lixo nao-metalico: {}'.format(contagem_lixo['nao_metalico']))
    print('='*50)
    sleep(1)
    print('Dirigindo-se a estacao espacial mais proxima')
    print('-'*50)
    sleep(2)
    print('Curiosity terminou exploracao. Liberando espaco de armazenamento')
    print('-'*50)
    sleep(2)
    print('Carga liberada!')
    print('-'*50)
    sleep(1)
    print('Curiosity esta pronto para uma nova expedicao!')
    print('='*50)
    print('\n')

# Soma a quantidade de cada tipo de lixo espacial.
def soma_tipo_lixo(deposito_lixo):
    metalico = 0
    nao_metalico = 0
    for i in deposito_lixo:
        if(i['tipo'] == 'metalico'):
            metalico += 1
        else:
            nao_metalico += 1
    return {'metalico': metalico, 'nao_metalico': nao_metalico}

# Gera saídas de texto descrevendo a ação do Curiosity.
def mensagem_inicia_expedicao():
    print('===================================================')
    print('Curiosity esta iniciando uma nova expedicao')
    print('===================================================')
    sleep(2)
    print('\n')

# Inicia uma nova expedição do Curiosity.
def expedicao(quantidade): # Recebe a quantidade de expedições que o Curiosity deve realizar.
    for expedicao in range(quantidade): # Realiza instruções enquanto a quantidade de expedições não tiver sido alcançada.
        mensagem_inicia_expedicao()
        robo_curiosity = Curiosity()
        solo_marte = (gera_lista_rocha(lixo_expedicao_passada) + gera_lista_lixo()) # Junção dos objetos gerados, formando um solo.
        for index in range(len(solo_marte)): # Realiza instruções para cada objeto no solo.
            if(index % 2): # Caso seja par, ele encontra um objeto do tipo Rocha
                item_encontrado = solo_marte[0]
                del solo_marte[0]
            else:          # Caso seja ímpar, ele encontra um objeto do tipo Lixo espacial.
                item_encontrado = solo_marte.pop()
            tipo_objeto = discenir_item(item_encontrado)
            if robo_curiosity.capacidade >= 69.5: # Caso a capacidade do Curiosity esteja comprometida, realiza o equilíbrio de rochas.
                equilibra_rochas(robo_curiosity)
                curiosity_aviso_capacidade()
            if valida_objeto(tipo_objeto, item_encontrado): # Valida o tipo de objeto encontrado
                if(coleta_objeto(tipo_objeto, item_encontrado, robo_curiosity)): # Caso o objeto seja coletado emite um aviso da coleta.
                    curiosity_aviso_coleta(tipo_objeto, item_encontrado, robo_curiosity)

            if valida_expedicao(robo_curiosity): # Valida se a expedição pode ser encerrada.
                break
        encerra_expedicao(robo_curiosity)


expedicao(3) # Inicializa expedições conforme o valor inserido