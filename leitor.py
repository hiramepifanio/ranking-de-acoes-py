import csv

def findIndexDoTitulo(tituloAlvo, titulos):
	index = -1
	for i, titulo in enumerate(titulos):
		if titulo == tituloAlvo:
			index = i
			break
	if index < 0:
		raise Exception("Título inexistente: \"" + tituloAlvo + '\"')
	
	return index
	
def printDadosFiltrandoItens(items, titulos, dados):
	for row in dados:
		for item in items:
			print(row[findIndexDoTitulo(item, titulos)], end = '\t')
		print()
	for item in items:
		print(item, end = '\t')
	
def orderDadosByItemDesc(item, titulos, dados):
	rank = rankEmpresasByItemDesc(item, titulos, dados)
	
	orderedDados = []
	for i in range(len(dados)):
		newLine = []
		for itemAux in dados[rank[i]]:
			newLine.append(itemAux)
		orderedDados.append(newLine)
		
	return orderedDados
	
def orderDadosByItem(item, titulos, dados):
	rank = rankEmpresasByItem(item, titulos, dados)
	
	orderedDados = []
	for i in range(len(dados)):
		newLine = []
		for itemAux in dados[rank[i]]:
			newLine.append(itemAux)
		orderedDados.append(newLine)
		
	return orderedDados
	

def rankEmpresasByItemDesc(item, titulos, dados):
	dadosNegativo = []
	for row in dados:
		newRow = []
		for itemAux in row:
			newRow.append(itemAux)
		dadosNegativo.append(newRow)
		
	col = findIndexDoTitulo(item, titulos)
	for i in range(len(dados)):
		dadosNegativo[i][col] = - dadosNegativo[i][col]
		
	return rankEmpresasByItem(item, titulos, dadosNegativo)

def rankEmpresasByItemPositivofirst(item, titulos, dados):
	rank = rankEmpresasByItem(item, titulos, dados)
	
	firstPositivo = 0
	for i in range(len(rank)):
		if dados[rank[i]][findIndexDoTitulo(item, titulos)] > 0:
			firstPositivo = i
			break
			
	rankPositivoFirst = []
	for i in range(firstPositivo, len(rank)):
		rankPositivoFirst.append(rank[i])
	for i in range(firstPositivo - 1, -1, -1):
		rankPositivoFirst.append(rank[i])
	
	return rankPositivoFirst
	
def rankEmpresasByItem(item, titulos, dados):
	col = findIndexDoTitulo(item, titulos)
	rank = []
	for i, empresa in enumerate(dados):
		rank.append(i)
	for i in range(len(dados)):
		indexMin = i
		for j in range(i + 1, len(dados)):
			if dados[rank[j]][col] < dados[rank[indexMin]][col]:
				indexMin = j
		rank[i], rank[indexMin] = rank[indexMin], rank[i]
		
	return rank

def addColumnSomaDeItems(tituloNewColumn, items, titulos, dados):
	titulos.append(tituloNewColumn)
	for i in range(len(dados)):
		value = 0
		for item in items:
			value += dados[i][findIndexDoTitulo(item, titulos)]
		dados[i].append(value)

def importTitulosAndDadosFromFundamentus(fileFromFundamentus):
	titulos = []
	dados = []
	with open(fileFromFundamentus, newline = '') as csvFile:
		spamReader = csv.reader(csvFile, delimiter = '\t')
		primeiraLinha = True;
		for row in spamReader:
			if primeiraLinha:
				for titulo in row:
					titulos.append(titulo)
				primeiraLinha = False;
			else:
				newRow = []
				primeiroItem = True
				for item in row:
					if primeiroItem:
						newRow.append(item)
						primeiroItem = False
					else:
						itemTratado = item
						itemTratado = itemTratado.replace('%', '')
						itemTratado = itemTratado.replace('.', '')
						itemTratado = itemTratado.replace(',', '.')
						newRow.append(float(itemTratado))
				dados.append(newRow)
	return titulos, dados

def addRank(tituloRank, rank, titulos, dados):
	titulos.append(tituloRank)
	for i in range(len(dados)):
		dados[rank[i]].append(i + 1)

def filterEmpresasByItemGE(item, value, titulos, dados):
	filteredDados = []
	col = findIndexDoTitulo(item, titulos)
	for row in dados:
		if row[col] >= value:
			filteredDados.append(row)
	return filteredDados
	
def filterEmpresasByItemGT(item, value, titulos, dados):
	filteredDados = []
	col = findIndexDoTitulo(item, titulos)
	for row in dados:
		if row[col] > value:
			filteredDados.append(row)
	return filteredDados

titulos = []
dados = []
titulos, dados = importTitulosAndDadosFromFundamentus("empresas.csv")

dados = filterEmpresasByItemGE("Patrim. Líq", 1e9, titulos, dados)
dados = filterEmpresasByItemGT("P/L", 0, titulos, dados)
dados = filterEmpresasByItemGT("ROIC", 0, titulos, dados)

rankPL = rankEmpresasByItemPositivofirst("P/L", titulos, dados)
addRank("Rk PL", rankPL, titulos, dados)

rankROIC = rankEmpresasByItemDesc("ROIC", titulos, dados)
addRank("Rk ROIC", rankROIC, titulos, dados)

rank = rankEmpresasByItemDesc("ROE", titulos, dados)
addRank("Rk ROE", rank, titulos, dados)

addColumnSomaDeItems("Soma", ["Rk PL", "Rk ROIC", "Rk ROE"], titulos, dados)
rankJGB = rankEmpresasByItem("Soma", titulos, dados)
addRank("Rk JGB", rankJGB, titulos, dados)

printDadosFiltrandoItens(["Rk JGB", "Papel", "Cotação", "P/L", "Rk PL", "ROIC", "Rk ROIC", "ROE", "Rk ROE"], titulos, orderDadosByItemDesc("Rk JGB", titulos, dados))

