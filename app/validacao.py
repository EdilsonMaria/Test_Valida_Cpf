import re
from datetime import datetime

def saudacao():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "Bom dia, Boa tarde, Boa noite meu povo\nBom dia!"
    elif 12 <= hora < 18:
        return "Bom dia, Boa tarde, Boa noite meu povo\nBoa tarde!"
    else:
        return "Bom dia, Boa tarde, Boa noite meu povo\nBoa noite!"

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)  # Remove pontos e traços

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"
