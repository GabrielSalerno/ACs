"""
Programação Estruturada
2024.1
12/03/2024

AC5
"""
import random

def main():
    vida_aventureiro = 100
    ataque_avetureiro = random.randint(10, 20)
    defesa_avetureiro = random.randint(1, 5)


    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    print("Aventureiro:", vida_aventureiro,ataque_avetureiro, defesa_avetureiro)
    print("Monstro:", vida_monstro,ataque_monstro)

    num_rodada = 0
    while vida_aventureiro >= 0 or vida_monstro >= 0:
        num_rodada += 1
        print("Rodada", num_rodada)
        vida_monstro -= random.randint(1, ataque_avetureiro)
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        ataque_rodada_monstro = random.randint(1, ataque_monstro)
        print(ataque_rodada_monstro)
        if ataque_rodada_monstro > defesa_avetureiro:
            vida_aventureiro -= (ataque_rodada_monstro - defesa_avetureiro)
        else:
            vida_aventureiro -= (defesa_avetureiro - ataque_rodada_monstro)
        if vida_aventureiro <= 0:
            print("Vôce morreu!")
            break
        print("Aventureiro:", vida_aventureiro,ataque_avetureiro, defesa_avetureiro)
        print("Monstro:", vida_monstro,ataque_monstro)

main()
