import re
from datetime import datetime

def saudacao():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia, boa tarde e/ou boa noite, meu POVO!\nBem-vindo a nossa aplicação de validação de CPF!\n\nBom dia!"
    elif 12 <= hora < 18:
        return "Bom dia, boa tarde e/ou boa noite, meu POVO!\nBem-vindo a nossa aplicação de validação de CPF!\n\nBoa tarde!"
    else:
        return "Bom dia, boa tarde e/ou boa noite, meu POVO!\nBem-vindo a nossa aplicação de validação de CPF!\n\nBoa noite!"

def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        return False

    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf_parcial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cpf[:9])
    digito2 = calcular_digito(cpf[:9] + digito1)

    return cpf[-2:] == digito1 + digito2
