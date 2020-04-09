deposito_lixo = [{'diametro': 0.46, 'tipo': 'nao-metalico', 'peso': 7.23}, {'diametro': 0.34, 'tipo': 'nao-metalico', 'peso': 7.69}, {'diametro': 0.67, 'tipo': 'metalico', 'peso': 2.32}, {'diametro': 0.95,
                                                                                                                                                                                            'tipo': 'nao-metalico', 'peso': 5.35}, {'diametro': 0.24, 'tipo': 'metalico', 'peso': 6.99}, {'diametro': 0.15, 'tipo': 'metalico', 'peso': 2.28}, {'diametro': 0.21, 'tipo': 'metalico', 'peso': 2.76}]

metalico = 0
nao_metalico = 0
for i in deposito_lixo:
    if(i['tipo'] == 'metalico'):
        metalico += 1
    else:
        nao_metalico += 1


a = {metalico, nao_metalico}
print(a)
