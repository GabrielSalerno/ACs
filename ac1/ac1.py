# Exercício 1
def calculadora_equacao_segundo_grau(a, b, c):
    print("A primeira raiz da equação é", (-b + ((b**2-4*a*c)**(1/2)))/(2*a))
    print("A segunda raiz da equação é", (-b - ((b**2-4*a*c)**(1/2)))/(2*a))

a_user = int(input("Informe o parâmetro a da equação: "))
b_user = int(input("Informe o parâmetro b da equação: "))
c_user = int(input("Informe o parâmetro c da equação: "))

calculadora_equacao_segundo_grau(a_user, b_user, c_user)

# Exercício 2
ano = int(input("Informe o ano: "))

print((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))
