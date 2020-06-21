#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from random import random, randint, choice


# Exibe graficamente um mapa
def exibe_mapa(mapa):
    cidades = len(mapa)
    G = nx.DiGraph()
    for i in range(cidades):
        G.add_node(i)
    for i in range(cidades):
        for j in range(cidades):
            if mapa[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='#CCCCCC')
    plt.show()


# Realiza uma "busca em largura" a partir de uma cidade_inicial.
# Devolve uma lista de origens, onde cada posição i contém um valor j,
# que significa que a cidade i foi alcançada a partir da cidade j. Um
# valor -1 em uma posição i significa que a cidade i não pode ser
# alcançada a partir de cidade_inicial.
def busca_em_largura(mapa, cidade_inicial):
    cidades = len(mapa)  # a quantidade de cidades
    visitadas = [cidade_inicial]  # quais cidades já foram visitadas
    fila = [cidade_inicial]  # uma fila usada no algoritmo de busca em largura
    origens = [-1] * cidades  # a partir de qual cidade as cidades foram visitadas
    origens[cidade_inicial] = cidade_inicial

    while fila:
        cidade = fila.pop(0)

        for cidade_vizinha in range(cidades):
            if mapa[cidade][cidade_vizinha] == 1 and cidade_vizinha not in visitadas:
                visitadas.append(cidade_vizinha)  # marcamos a cidade vizinha como visitada
                origens[cidade_vizinha] = cidade  # salvamos de onde chegamos na cidade vizinha
                fila.append(cidade_vizinha)  # colocamos a cidade vizinha na fila
    return origens


###############################
# PARTE PRINCIPAL DO PROGRAMA #
###############################

# Podemos definir o mapa estaticamente
# mapa = [ [1,1,1,1], [1,1,0,0], [1,1,1,0], [1,0,1,1] ]
# cidades = len(mapa)

# Podemos definir o mapa pela leitura do teclado
# cidades = int(input())
# mapa = []
# for i in range(cidades):
#    mapa.append( [ int(v) for v in input().split() ] )

# Podemos definir o mapa aleatóriamente
PROB_ESTRADA = 0.15  # 15% de chance de ter uma estrada de uma cidade para outra
cidades = 10  # quantidade de cidades
mapa = []
for i in range(cidades):
    mapa.append([0] * cidades)
for i in range(cidades):
    for j in range(cidades):
        if i == j:
            mapa[i][j] = 1  # sempre podemos chegar de uma cidade a ela mesma
        elif random() < PROB_ESTRADA:
            mapa[i][j] = 1  # há uma estrada da cidade i para a cidade j (depende da probabilidade)

# Escrevemos o mapa
for i in range(cidades):
    print(mapa[i])
quantidade_saidas = 0
# AQUI FAREMOS A IMPLEMENTAÇÃO
k = int(input("Digite a cidade: "))
print("----(a)----")
quantidades_saidas = -1
quantidades_entradas = 0
for i in range(cidades):
    for j in range(cidades):
        if mapa[i][j] == 1 and i == k:
            quantidades_saidas += 1
for i in range(cidades):
    if mapa[i][k] == 1 and k != i:
        quantidades_entradas += 1
print("quantidade de cidades que chegam: ", quantidades_entradas)
print("quantidade de cidades que saem: ", quantidades_saidas)
print("----(b)----")
maior_numero_cidades = []
resp_cidade = []
cont = 0
for i in range(cidades):
    for j in range(cidades):
        if mapa[i][j] == 1:
            cont += 1
    maior_numero_cidades.append(cont)
    cont = 0
for i in range(len(maior_numero_cidades)):
    for j in range(len(maior_numero_cidades)):
        if maior_numero_cidades[i] > maior_numero_cidades[j]:
            resp_cidade.append(i)
print("a(s) cidade(s) que chega(m) ao maior numero de cidades são: ", end='')
for i in range(len(resp_cidade)):
    print(resp_cidade[i], end=' ')
print()
print("----(c)----")
cidades_mao_dupla, qtd_saida = 0,0
for j in range(cidades):
    if (mapa[k][j] == 1) and (k != j):
        qtd_saida += 1
        #cidades_diretas.append(j)
        #for k in range(cidades):
        if mapa[j][k] == 1:
            cidades_mao_dupla += 1
if cidades_mao_dupla == qtd_saida:
    print("Todas as ligações diretas são mão dupla.")
else:
    print("Nem todas as ligações são de mão dupla.")
print("(d)")
estrada_direta = []
for i in range(cidades):
    if (mapa[i][k] == 1) and (k != i):
        estrada_direta.append(i)
print("As cidades com ligação direta são:", end=' ')
for j in estrada_direta:
    print(j, end=' ')
    
print("(e)")

quantidades_saidas = 0
quantidades_entradas = 0
lista_saidas = []
lista_entradas = []
lista_isoladas = []
lista_apenas_entrada = []
lista_apenas_saida = []
for i in range(cidades):
    for j in range(cidades):
        if mapa[i][j] == 1 and i != j:
            quantidades_saidas += 1
    if quantidades_saidas > 0:
        lista_saidas.append(1)
        quantidades_saidas = 0
    else:
        lista_saidas.append(0)
        quantidades_saidas = 0
for pos in range(cidades):
    for i in range(cidades):
        if mapa[i][pos] == 1 and pos != i:
            quantidades_entradas += 1
    if quantidades_entradas > 0:
        lista_entradas.append(1)
        quantidades_entradas = 0
    else:
        lista_entradas.append(0)
        quantidades_entradas = 0

for i in range(cidades):
    if lista_entradas[i] == 0 and lista_saidas[i] == 0:
        lista_isoladas.append(i)
    if lista_entradas[i] == 1 and lista_saidas[i] == 0:
        lista_apenas_entrada.append(i)
    if lista_entradas[i] == 0 and lista_saidas[i] == 1:
        lista_apenas_saida.append(i)

print('A(s) cidade(s) isolada(s) é(são): {}' .format(lista_isoladas))
print('A(s) cidade(s) com apenas entrada(s) é(são): {}' .format(lista_apenas_entrada))
print('A(s) cidade(s) com apenas saida(s) é(são): {}' . format(lista_apenas_saida))


print("(f)")


m = [int(v) for v in input().split()]
elevai = 0
for i in range(len(m)-1):
    if mapa[m[i]][m[i+1]] == 1:
        elevai += 1
if elevai == (len(m)-1):
    print('Essa sequencia é possivel')
else:
    print('Essa sequencia não é possivel')

print("(g)")
# Por exemplo, identificamos onde podemos chegar a partir da cidade 0 (você na verdade deverá ler k e p)
origens = busca_em_largura(mapa, 0)
print(origens)

# Mostra o mapa (bloqueia o programa até o mapa ser fechado)
exibe_mapa(mapa)
