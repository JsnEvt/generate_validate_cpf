# no calculo do cpf, a multiplicacao comeca do 10 na primeira rodada e do 11 na
# segunda rodada, onde na segunda, a multiplicacao vai ate o primeiro digito
# verificador para definir o ultimo digito da sequencia.

import re


def valida_cpf(cpf):
    cpf = str(cpf)
    # expressoes regulares (substituir tudo diferente de zero a nove por nada.)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]
    reverso = 10  # contagem regressiva
    total = 0

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
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # sabendo que sequencias avaliavam como verdadeiro, faremos uma outra
    # checagem

    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
