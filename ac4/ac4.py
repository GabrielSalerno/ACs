"""
Programação Estruturada
2024.1
05/03/2024

AC4
"""

def ler_nome_user():
    """
    Pede para o usuário informar o nome e retorna uma string.
    """
    return input("Informe seu nome: ")

def ler_notas():
    """
    Lê e retorna quatro notas do tipo float
    """
    ap1 = float(input("Informe a AP1: "))
    ap2 = float(input("Informe a AP2: "))
    asub = float(input("Informe a AS: "))
    ac = float(input("Informe a AC: "))
    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    """
    Retorna False se pelo menos uma das notas for menor que 0 e maior que 10
    """
    if ap1 > 10 or ap1 < 0:
        return False
    if ap2 > 10 or ap2 < 0:
        return False
    if asub > 10 or asub < 0:
        return False
    if ac > 10 or ac < 0:
        return False
    else:
        return True

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas detre as informadas
    """
    if ap1 > ap2:
        if ap2 < asub:
            maior_nota = asub
            return maior_nota, ap1
    if ap2 > ap1:
        if ap1 < asub:
            maior_nota = asub
            return maior_nota, ap2
    else:
        return ap1, ap2

def calcular_media(n1, n2, ac):
    """
    Calcula a média do aluno.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media):
    """
    Informa se o aluno passou ou não na disciplina
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabens! Você foi aprovado.")
    else:
        print("Você foi reprovado.")

def main():
    nome = ler_nome_user()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1,n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()
