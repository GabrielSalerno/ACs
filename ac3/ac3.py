# Exercício 1
def determina_tipo_triangulo(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        return "Não é um triângulo"
    elif a == b and a == c and b == c:
        return "Equilátero"
    elif (a == b and a != c) or (b == c and b != a):
        return "Isósceles"
    elif a != b and a != c and b != c:
        return "Escaleno"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))

# Exercício 2
def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return ""

def testa_dia_semana():
    print(dia_semana(2))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(9))

def main():
    testa_triangulo()
    testa_dia_semana()

main()