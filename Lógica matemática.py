# Este é um programa que ajuda no aprendizado de matemática e lógica para crianças
print ('< Lógica Matemática >')
print ()
 
pontos = 0
 
print ('A seguir você deverá tentar resolver problemas de lógica e matemática.')
print ('Ao final, será exibida sua pontuação.')
print ()
print ()
print ('Você ganhou quatro barras de chocolate na Páscoa. Comeu metade de cada uma delas.')
print ('Quantas barras sobraram?')
print ()
 
resposta_1 = input ('Resposta: ')
if float (resposta_1) == 2:
    print ('Você acertou e ganhou 10 pontos!')
    pontos = pontos + 10
elif float (resposta_1) != 2:
      print ('Você errou e não ganhou pontos!')
      pontos = pontos
         
print ()
print ('De acordo com a sequência 1, 4, 7, 10...')
print ('Qual o próximo número?')
print ()
 
resposta_2 = input ('Resposta: ')
if float (resposta_2) == 13:
    print ('Você acertou e ganhou 15 pontos!')
    pontos = pontos + 15
elif float (resposta_2) != 13:
      print ('Você errou e não ganhou pontos!')
      pontos = pontos
print()
 
print (' Digite os números de 1 a 15 ao contrário. ')
print ()
 
repeticoes = 15
numeros = 15
 
while repeticoes > 0:
    numeros = input (' Digite o número da sequência: ')
    if int (numeros) == (repeticoes): 
        repeticoes = repeticoes - 1
    elif int (numeros) != (repeticoes):
        print ('Você errou a sequência e não ganhou pontos!')
        pontos = pontos
        break
    else:
        print()
 
print ()
print ('Sua pontuação final foi: ', pontos)