# Atividade 2 - Machine Learning - AVANTI

Questão 1:

#Uma lista de que o dev consegue colocar os números que ele quiser, e a função vai retornar apenas os números ímpares dessa lista.

def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

print(numeros_impares([1, 2, 3, 4, 5, 6, 7]))  

#Uma função que recebe em parâmetro um número inteiro e retorna uma lista com todos os números ímpares de 1 até esse número.

def numeros_impares(infinito):
    return [n for n in range (1, infinito + 1) if n % 2 != 0]

print(numeros_impares(8))

Resultado de ambos: [1, 3, 5, 7]
