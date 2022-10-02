pontos_de_entrega = []
ponto_de_partida = ()
with open("entrada.txt") as arquivo:
    for i, linha in enumerate(arquivo):
        lista = linha.split()
        for j, element in enumerate(lista):
            if element != '0':
                if element == 'R':
                    ponto_de_partida = (i, j, element)
                else:
                    pontos_de_entrega.append((i, j, element))

def distancia_entre_pontos(tupla_1, tupla_2):
    return abs(tupla_1[0] - tupla_2[0]) + abs(tupla_1[1] - tupla_2[1])

def permutacoes(conjunto):
    if len(conjunto) == 1:
        yield conjunto
        return
    for p in permutacoes(conjunto[1:]):
        for i, _ in enumerate(conjunto):
            yield p[:i] + conjunto[0:1] + p[i:]
"""
def permutar(conjunto):
    if len(conjunto) == 1:
        return[conjunto]
    lista_auxiliar = []
    for item, elemento_atual in enumerate(conjunto):
        elementos_restantes = conjunto[:item] + conjunto[item+1:]
        for p in permutar(elementos_restantes):
            lista_auxiliar.append([elemento_atual] + p)
    return lista_auxiliar
"""
dist_min = 0
rot_min = []

for p in permutacoes(pontos_de_entrega):
    inicial_para_segundo = distancia_entre_pontos(ponto_de_partida, p[0])
    ultimo_para_inicial = distancia_entre_pontos(ponto_de_partida, p[-1])

    permut_dist = 0 
    for k, t in enumerate(p):
        if t != p[-1]:
            permut_dist += distancia_entre_pontos(t, p[k+1])

    perm_tot_dist = inicial_para_segundo + ultimo_para_inicial + permut_dist
    if perm_tot_dist < dist_min or dist_min == 0:
        dist_min = perm_tot_dist
        rot_min = p

print(dist_min)
for i in rot_min:
    print(i[2], end=" ")