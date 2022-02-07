# criando uma lista
# tipo de lista 1
minha_lista = ['a','b','c']
# print(minha_lista)

# tipo de lista 2
# usando a funcao lista
minha_7 = list('abc')
# print(minha_lista)

# lista
numeros_pares = [0,2,4,6,8,10]

# trocar valor de uma posicao
numeros_pares[1] = 9

# adicionar um valor no final, qualquer valor seja boleano, string, numero
numeros_pares.append('ameixa')
numeros_pares.append('1.3')

# valores boleano devem comecar com letra MAIUSCULAS (True, False)
numeros_pares.append(False)


# remover da lista o ultimo elemento
numeros_pares.pop()

# remover o primeiro elemento deeve colocar a posicao
numeros_pares.pop(2)

# verificando o numero removido
numeros_removidos = numeros_pares.pop()

# adicionar a posicao que eu escolher
numeros_pares.insert(2,'Pamonha')

# print(numeros_pares)
# print(numeros_removidos)

# ------------------------- aula 2 -------------------------------
# verificar o comprimento de uma lista
# print(len(numeros_pares))


# matrix = [
#     [1,2,3,4,5],
#     [1,2,3,4,5],
# ]

# for line in matrix:
#     for element in line:
      
   
#         # print(element)

# ---------------------verificando strings------------------------------------
# frase = 'Atirei o pau no gato'

# print(frase[4])
# print(len(frase))

# -------------------tranformando frases strings em lista------------------
frase = 'Atirei o pau no gato'

frase_as_list = list(frase)
# print(frase_as_list)


# verificando se existe um elemento na lista
minha_lista = [1, 2, 3, 4, 5]
lista_string = list('Ola mundo')

# print(1 in minha_lista)
# print('O' in lista_string)

# ------------------------listas e slicing----------------------------

numeros_impar = [1,3,5,7,9,11,13,15]


minha_string = 'Aqui um texto bem esperto'

# acessando um valor na lista
# primeiro valor = primeira posição => valor inicial
# segundo valor = ultima posição => valor final
# valor final sempre 1 a mais do que precisa
print(numeros_impar[0:2])
# [1, 3]

# escolhendo de quanto em quanto quero ver os numeros
print(numeros_impar[0:7:2])
# [1, 5, 9, 13]

# acessando posicao da string inteira(sem especificar valor final)
print(minha_string[0:])
# Aqui um texto bem esperto

# escolhendo o inicio da frase e o final dela
print(minha_string[4:-2])
# um texto bem esper

# mostrar text inverso na string
print(minha_string[-1:0:-1])
# otrepse meb otxet mu iuq

# --------------------------------------------

# lst = [1,-2,-4,1,5,7,-9]
# invertendo negativo para positivo
# def invert(lst):
#    print([numb * -1 for numb in lst])
# invert(lst)

# -------------------------------------------
arrays = [1,2,3,4]
number = 2
#  multiplicando todos elemento por um NUMERO
# def index(arrays, number):
#     print([n * number for n in arrays])

# index(arrays,number)

# achando o valor do array total
def total(array, number):
    array.append(8 ** number)
    # novo = len(array)-1
    # igual = novo * number
    print(array)
total(arrays,number)

