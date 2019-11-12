#Para declarar variáveis basta colocar o nome da variável e o seu valor

biscoito = "bolacha"
alunos = 41
media = 7.5
booleana = True
booleana2 = False

#lista
pedro = ["Drake", "Testemunha de Xiaomi", "RM", 22]
pedro.append("funk") #acrescenta um valor no final de uma lista
pedro.pop() #retira o último
len(pedro) #devolve o tamanho de uma lista ou string

#dicionario
lethicia = {"sobrenome": "Asevedo", "nome_do_meio":"Yara", "hobbie":"skate"}

#tupla é uma lista cujos valores não podem ser alterados
murilo = ("henrique", "henrique")

#input() recebe um valor digitado pelo usuário
#int() converte para inteiro
nome = input("Digite o seu nome").lower()
idade = int(input("Digite a sua idade"))

#ESTRUTURA IF ELSE
#if condição:
#   bloco de código if IDENTADO
# else:
#   bloco de codigo else IDENTADO
#
#se tiver um else if em python é
#elif condição:
#   bloco de código elif IDENTADO
#

if (nome == 'pedro' and idade == 22) or nome == 'drake':
    print("Salve Drake")
elif nome == 'murilo':
    print("Salve Henrique Henrique")
else:
    print("você não é o Drake")


#while condicao:
#   bloco IDENTADO de código
print("while")
numero = 0 
while numero < 5:
    print(numero)
    numero = numero + 1

lista = ['cubo magico', 'pagode japones', 'skate', 'manga com leite']

print("For in")
for item in lista:
    print(item)

#for i in range(inicio, parada, passo)
# - o inicio é o valor de inicio do i
# - parada é até onde o valor vai sem incluir ele 
# - passo é de quanto em quanto nosso valor vai mudar(ex: de um em um, de dois em dois, de menos um em menos um...) 

#se vc passar só um valor no range() ele passa de um em um partindo do zero
#se vc passar dois valores ele passa de um em um começando no primeiro número e parando no segundo
#se vc passar três valores ele passa de acordo com o ultimo numero começando do primeiro e parando no segundo

print("for in range 2 parametros")
for i in range(0, len(lista)):
    print(lista[i])

print("for in range 3 parametros")
for i in range(0, len(lista), 2):
    print(lista[i])

print("for in range 3 parametros e passo decrementando")
for i in range(len(lista)-1, 0, -2):
    print(lista[i])

print("for in range 1 parametro")
for i in range(len(lista)):
    print(lista[i])