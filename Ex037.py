##Crie um programa que peça ao usuário que digite uma palavra e exiba a quantidade de vogais presentes nela.

palavra = input("Digite uma palavra: ").lower()


##print(list(palavra))
resultados = []

vogais = ["a","e","i","o","u"]

for vogal in vogais:

    contagem = palavra.count(vogal)
    resultados.append(contagem)

soma_total = sum(resultados)
print(soma_total)
    
    
  