"""
Programação Estruturada
2024.1
09/03/2024

AC2
"""
# Exercício 1
def eq_seg_grau(a, b, c):
    x1 = (-b + ((b**2-4*a*c)**(1/2)))/(2*a)
    x2 = (-b - ((b**2-4*a*c)**(1/2)))/(2*a)
    return x1, x2

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Exercício 2
def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return (valor_hora * num_horas) * (1 - irpf)

def main():
    print(eq_seg_grau(5,10,-2))
    print(bissexto(2004))
    print(calcula_salario(100, 10))

main()