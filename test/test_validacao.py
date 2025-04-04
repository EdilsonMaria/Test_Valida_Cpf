import unittest
from app.validacao import validar_cpf

class TestValidacaoCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("52998224725"))

    def test_cpf_invalido_tamanho_errado(self):
        self.assertFalse(validar_cpf("123.456.789-0"))
        self.assertFalse(validar_cpf("1234567890"))

    def test_cpf_invalido_digito_errado(self):
        self.assertFalse(validar_cpf("529.982.247-26"))

    def test_cpf_com_todos_digitos_iguais(self):
        for i in range(10):
            self.assertFalse(validar_cpf(str(i) * 11))

    def test_cpf_com_caracteres_invalidos(self):
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))
        self.assertFalse(validar_cpf("111.111.111-1a"))

if __name__ == '__main__':
    unittest.main()
