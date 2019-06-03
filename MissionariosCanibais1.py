    # Posição 0 - 3 Missionarios do lado esquerdo
    # Posição 1 - 3 Canibais do lado esquerdo
    # Posição 2 - 0 Missionarios do lado direito
    # Posição 3 - 0 Canibais do lado direito
    # Posição 4 - Lado da Canoa 0 - Esquerdo -- 1 - Direito

estadoInicial = [3,3,0,0,0]

    # Operadores
    # (1,0) Atravessar um missionario no barco
    # (2,0) Atravessar dois missionario no barco
    # (0,1) Atravessar um canibal no barco
    # (0,2) Atravessar dois canibais no barco
    # (1,1) Atravessar um missionario e um canibal no barco

operadores = [(1,0),(1,1),(2,0),(0,2),(0,1)]

fronteira = []
visitados = []

# Direção da canoa 0 ou 1
def deslocarCanoa(estadoAtual,numeroMissionarios=0,numeroCanibais=0):

    if (numeroCanibais + numeroMissionarios) > 2:
    	return

    if estadoAtual[-1]==0:
    	missionarioOrigem = 0
    	canibalOrigem = 1
    	missionarioDestino = 2
    	canibalDestino = 3
    else:
    	missionarioOrigem = 2
    	canibalOrigem = 3
    	missionarioDestino = 0
    	canibalDestino = 1
    # Se não há o que transportar
    if estadoAtual[missionarioOrigem] == 0 and estadoAtual[canibalOrigem] == 0:
    	return

    # Atualizando a posição da canoa
    estadoAtual[-1] = 1 - estadoAtual[-1]

    #Transportando os missionarios
    for i in range(min(numeroMissionarios,estadoAtual[missionarioOrigem])):
    	estadoAtual[missionarioOrigem] = estadoAtual[missionarioOrigem] - 1
    	estadoAtual[missionarioDestino] = estadoAtual[missionarioDestino] + 1

    #Transportando os canibais
    for i in range(min(numeroCanibais,estadoAtual[canibalOrigem])):
    	estadoAtual[canibalOrigem] = estadoAtual[canibalOrigem] - 1
    	estadoAtual[canibalDestino] = estadoAtual[canibalDestino] + 1

    return estadoAtual

# Calcula os nós de estados possiveis validos
def sucessores(estado):
    sucessores = []
    for (i,j) in operadores:
    	s = deslocarCanoa(estado[:],i,j)
    	if s == None:
    		continue
    	if ((s[0]<s[1] and s[0]>0) or (s[2]<s[3] and s[2]>0)):
    		continue
    	if s in visitados:
    		continue
    	sucessores.append(s)
    return sucessores

# Obtem o nó adjacente não visitado para a busca
def adjacenteNaoVisitado(elementoAnalisar):
    l = sucessores(elementoAnalisar)
    if len(l) > 0:
    	return l[0]
    else:
    	return -1

# Verifica se todos os missionarios e canibais estão do outro lado
def estadoFinal(estado):
    if estado[2] >= 3 and estado[3] >= 3:
    	return True
    else:
    	return False

def busca(estadoInicial):
    fronteira.append(estadoInicial)
    while len(fronteira) != 0:
    	elementoAnalisar = fronteira[len(fronteira) - 1]
    	if estadoFinal(elementoAnalisar):
    		break
    	v = adjacenteNaoVisitado(elementoAnalisar)
    	if v == -1:
    		fronteira.pop()
    	else:
    		visitados.append(v)
    		fronteira.append(v)
    else:
    	print("Busca sem sucesso!")
    return fronteira

#print(Busca(estadoInicial))
teste = busca(estadoInicial)
print(teste)

