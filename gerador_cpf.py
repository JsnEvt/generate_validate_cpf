'''este programa visa gerar uma sequencia de numeros aleatorios de 9 digitos
e validar os dois digitos finais atraves do codigo iniciado no loop.'''

from random import randint


def gerador_cpf():
    numero = str(randint(100000000, 999999999))  # para ser a faixa de numeros
    # a serem gerados para o CPF(intervalo e faixa)

    novo_cpf = numero
    reverso = 10  # contagem regressiva
    total = 0

    # loop cpf
    for index in range(19):
        if index > 8:  # aqui, ele conta ate o nono digito, do zero ate o oitavo.
            index -= 9  # para iniciar uma nova contagem

        total += int(novo_cpf[index]) * reverso

        reverso -= 1  # para decrementar em 1
        if reverso < 2:  # como a contagem da multiplicacao para em 2...
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0  # para comecar a segunda rodada e ir ate o primeiro digito
            # verificador.
            # novo_cpf recebe o primiero digito calculado na
            novo_cpf += str(d)
            # primeira e na segunda rodada.

    # evita sequencias ... ex. 11111111111
    #sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # sabendo que sequencias avaliavam como verdadeiro, faremos uma outra
    # checagem

    # if cpf == novo_cpf and not sequencia:
    #    print('Valido')
    # else:
    #    print('Invalido')

    return novo_cpf
