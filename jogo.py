import random
import sys
import os


linha = '-' * 50
titulo = " Jogo da advinhação"

print(linha)
print(titulo.center(50))
print(linha)
print("\n\n")

numberRandom = random.randint(1,41)
print("Vamo começar o game,advinhe o número que está secretamente entre 1 e 40")

tentativa = 7
while  tentativa != 0:

     guess = int(input("tente advinhar o numero secreto: "))
     tentativa-=1

     if guess > 40 or guess == 0:
         print("digite um número válido entre 1 e 40")
         sys.exit()
    
     if tentativa == 0 and guess != numberRandom:
         print("voce possui " + str(tentativa) + " tentativas, ou seja voce perdeu!")
         os.system("cls")
         sys.exit()

    
     elif guess < numberRandom:
        

        print("o número que voce digitou está  abaixo do  número secreto. voce possui " + str(tentativa) + " tentativas\n")

     elif guess > numberRandom:
        
        print("o número que voce digitou está  acima do número secreto. voce possui " + str(tentativa) + " tentativas\n")

    
     elif  guess == numberRandom and tentativa != 0:
         print("parabéns voce acertou o número secreto faltando  " + str(tentativa) + " tentativas")
         sys.exit()
         
     elif  guess == numberRandom and tentativa == 0:
         print(" voce conseguiu acertar o número secreto na ultima tentativa, parabéns pela persistência")
         sys.exit()

    

  




