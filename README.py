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


#Questão 3: 
def diferenca_simetrica(lista_1, lista_2):
    return list(set(lista_1) ^ set(lista_2))
                
print(diferenca_simetrica([1, 2, 3, 4], [3, 4, 5, 6])) 


#Questão 4:
def segundo_maior(numeros):
    unicos = list(set(numeros))
    if len(unicos) < 2:
        return None  # não existe segundo maior
    unicos.sort(reverse=True)
    return unicos[1]

lista = [4, 1, 7, 7, 3, 9, 2]
print(segundo_maior(lista))


#Questão 5:
def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])

pessoas = [("Carlos", 34), ("Ana", 28), ("Bruno", 41)]
print(ordenar_por_nome(pessoas))

#Questão 6:
import pandas as pd

def outliers_zscore(df, coluna, limite=3):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    z = (df[coluna] - media) / desvio
    return df[abs(z) > limite] 


import pandas as pd

def outliers_zscore(df, coluna, limite=3):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    z = (df[coluna] - media) / desvio
    return df[abs(z) > limite]

def identificar_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    return outliers

outliers = identificar_outliers_iqr(df, 'valor')
print(f"Foram encontrados {len(outliers)} outliers")

df_limpo = df.drop(outliers.index) # Remover os outliers

df['valor'] = df['valor'].clip(lower=limite_inferior, upper=limite_superior)

df.loc[outliers.index, 'valor'] = None # Substituir por NaN e imputar com média/mediana
df['valor'] = df['valor'].fillna(df['valor'].median())

#Questão 7:
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})

df_linhas = pd.concat([df1, df2], axis=0, ignore_index=True)

df_colunas = pd.concat([df1, df2], axis=1)

#Questão 8:
import pandas as pd

df = pd.read_csv('arquivo.csv')
print(df.head())
print(df.head(10))

#Questão 9:
coluna = df['nome_coluna']

colunas = df[['coluna1', 'coluna2']]

filtrado = df[df['idade'] > 30]

filtrado2 = df[(df['idade'] > 30) & (df['cidade'] == 'Fortaleza')]

resultado = df.loc[df['idade'] > 30, ['nome', 'idade']]

#Questão 10:
df.isna().sum()
df_sem_nan = df.dropna()
df.dropna(how='all')
df.dropna(axis=1)

df['coluna'] = df['coluna'].fillna(0)

df['coluna'] = df['coluna'].fillna(df['coluna'].mean())
df['coluna'] = df['coluna'].fillna(df['coluna'].median())
df['coluna'] = df['coluna'].fillna(df['coluna'].mode()[0])

df['coluna'] = df['coluna'].fillna(method='ffill')
df['coluna'] = df['coluna'].fillna(method='bfill')
