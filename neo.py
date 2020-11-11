import re

def validade_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))
    if (not cnpj) or (len(cnpj)) < 14:
        return False

    inteiros = [x for x in map(int, cnpj)]
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x * y for (x, y) in zip(novo, prod)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    if novo == inteiros:
        return cnpj
    return False

def teste_numeros():
    assert validade_cnpj('1234567890') == False

def teste_cnpj_valido():
    assert validade_cnpj('30.652.204/0001-78') == '30652204000178'

def teste_letras():
    assert validade_cnpj('abcdefghjlkmnopqr') == False

def teste_cnpj_valido_novo():
    assert validade_cnpj('19791371000167') == '19791371000167'

def teste_cpf():
    assert validade_cnpj('09009596060') == False

def teste_cnpj_valido_novez():
    assert validade_cnpj('99.999.999/9999-62') == '99999999999962'