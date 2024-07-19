from calculadora import Calculadora

def test_soma():
    calculadora = Calculadora()
    resultado = calculadora.soma(3, 5)
    assert resultado == 8

def test_subtrair():
    calculadora = Calculadora()
    resultado = calculadora.subtrair(10, 5)
    assert resultado == 5