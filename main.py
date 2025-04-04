from app.validacao import saudacao, validar_cpf

def main():
    print(saudacao())
    cpf = input("Digite o número do CPF (com ou sem pontuação): ")
    if validar_cpf(cpf):
        print("CPF válido ✅")
    else:
        print("CPF inválido ❌")

if __name__ == "__main__":
    main()
