# Exercício 1
def calculadora_equacao_segundo_grau():
    a = int(input("Informe o parâmetro a da equação: "))
    b = int(input("Informe o parâmetro b da equação: "))
    c = int(input("Informe o parâmetro c da equação: "))
    print("A primeira raiz da equação é", (-b + ((b**2-4*a*c)**(1/2)))/(2*a))
    print("A segunda raiz da equação é", (-b - ((b**2-4*a*c)**(1/2)))/(2*a))

calculadora_equacao_segundo_grau()

# Exercício 2
ano = int(input("Informe o ano: "))

print((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))
