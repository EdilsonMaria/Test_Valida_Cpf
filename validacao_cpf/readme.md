# Validação de CPF em Python

Este projeto é uma aplicação simples desenvolvida em Python que valida números de CPF (Cadastro de Pessoa Física) conforme as regras da Receita Federal do Brasil.

---

## 📁 Estrutura do Projeto

```
validacao_cpf.py/
│
├── app/
│   └── validacao.py         # Funções de saudação e validação de CPF
│
├── test/
│   └── test_validacao.py    # Testes unitários com unittest
│
└── main.py                  # Interface de execução do programa
```

---

## 🚀 Como usar a aplicação

1. **Clone o repositório:**

```bash
git clone https://github.com/EdilsonMaria/Test_Valida_Cpf.git
cd validacao_cpf.py
```

2. **Execute a aplicação:**

```bash
python main.py
```

A aplicação irá:
- Exibir uma saudação personalizada com base no horário atual.
- Solicitar ao usuário um número de CPF.
- Informar se o CPF digitado é válido ou inválido.

---

## 🔬 Validação de CPF

A função `validar_cpf()` remove pontuações e verifica se:
- O CPF possui 11 dígitos.
- Não é uma sequência de dígitos iguais.
- Os dígitos verificadores finais estão corretos, com base nos cálculos oficiais da Receita Federal.

---

## ✅ Testes Unitários

Os testes estão localizados na pasta `test/` e foram escritos usando o módulo `unittest`.

### 📋 Casos de Teste Cobertos

- `test_cpf_valido`: verifica CPFs válidos com e sem pontuação.
- `test_cpf_invalido_tamanho_errado`: rejeita CPFs com menos de 11 dígitos.
- `test_cpf_invalido_digito_errado`: rejeita CPFs com dígitos finais inválidos.
- `test_cpf_com_todos_digitos_iguais`: rejeita CPFs com todos os dígitos repetidos (ex: `111.111.111-11`).
- `test_cpf_com_caracteres_invalidos`: rejeita CPFs com letras ou caracteres especiais fora do padrão.

### ▶️ Como executar os testes

```bash
python -m unittest discover -s test
```

---

## 💡 Importância dos Testes

Testes unitários são fundamentais para garantir a qualidade do código, prevenir regressões e assegurar que todas as regras de negócio (neste caso, validação de CPF) estão sendo corretamente aplicadas. Isso permite refatorações futuras com segurança.

---

