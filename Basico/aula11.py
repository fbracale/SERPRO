def configuration_acess (**kwargs):
    if len(kwargs) <= 3:
        if kwargs['arg3'] == 0:
            print('Olá, Felipe. Bem vindo!')
        else:
            print('Usuário não identificado!')
    elif kwargs['arg4'] == -1:
        print('GOD MODE!')
    else:
        print('Modo Admin!')

    
    # for chave, valor in kwargs.items():
    #     print(chave, valor)



configs = {
    'arg1': 0,
    'arg2': 1,
    'arg3': 2,
    'arg4': 1
}

configuration_acess(**configs)