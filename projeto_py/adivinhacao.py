import random

print("")
print(45 * "*")
print("Bem vindo ao jogo de adivinhação")
print(45 * "*")

numero_secreto = round(random.randrange(1, 11))
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String interpolation
    chute_str = input("Digite um número entre 1 e 10: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute <= 0 or chute > 11):
        print("Número informado inválido, tente novamente.")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1


print("Fim do jogo")









