# Atividade 2 - Machine Learning - AVANTI

#Questão 1:

#Uma lista de que o dev consegue colocar os números que ele quiser, e a função vai retornar apenas os números ímpares dessa lista.

def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

print(numeros_impares([1, 2, 3, 4, 5, 6, 7]))  

#Uma função que recebe em parâmetro um número inteiro e retorna uma lista com todos os números ímpares de 1 até esse número.

def numeros_impares(infinito):
    return [n for n in range (1, infinito + 1) if n % 2 != 0]

print(numeros_impares(8))


#Questão 2:

#Realizando uma função 'primo' avalio se terão números divisíveis de 2 até a raiz quadrada desse número.
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [n for n in lista if primo(n)]

print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) 