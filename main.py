from app.validacao import saudacao, validar_cpf

def main():
    print(saudacao())
    cpf = input("Digite o número do CPF (com ou sem pontuação): ")
    if validar_cpf(cpf):
        print("CPF válido na Receita Federal ✅")
    else:
        print("CPF inválido na Receita Federal ❌")

if __name__ == "__main__":
    main()
