def conversor_resposta(letra):
    if letra[0] == 'a':
        return 0
    elif letra[0] == 'b':
        return 1
    elif letra[0] == 'c':
        return 2
    elif letra[0] == 'd':
        return 3
    else:
        return False

acertos = 0

perguntas = [
    {
        "Pergunta": "Quanto é 7 * 3?",
        "Opções": ['7', '10', '21', '23'],
        "Resposta": "21"
    },
    {
        "Pergunta": "Quanto é 2 * 2?",
        "Opções": ['2', '4', '8', '10'],
        "Resposta": "4"
    },
    {
        "Pergunta": "Quanto é 2³?",
        "Opções": ['4', '5', '6', '8'],
        "Resposta": "8"
    }
]


for pergunta in perguntas:
    print('\nPergunta: '+ pergunta['Pergunta'])
    print('A)  '+pergunta['Opções'][0])
    print('B)  '+pergunta['Opções'][1])
    print('C)  '+pergunta['Opções'][2])
    print('D)  '+pergunta['Opções'][3])
    resposta = input("Qual a opção correta? ").lower().strip()
    if pergunta['Opções'][conversor_resposta(resposta)] == pergunta['Resposta']:
        print('Parabéns. Você acertou!')
        acertos += 1

print(f'Você acertou {acertos} de 3 perguntas!')

