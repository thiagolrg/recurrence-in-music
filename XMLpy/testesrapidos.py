lista6 = [(1,6),(3,8),(10,16),(30,36),(20,26)]
lista3 = [(1,3),(3,5),(2,5),(4,7),(32,35),(20,23),(23,26)]
dicio = {(1,1,1,1,1,1):lista6,(1,1,1):lista3}
listachavevalor =[]

for chave in dicio:
	for valor in dicio[chave]:
		listachavevalor.append((chave,valor))

listasorted = sorted(listachavevalor, key=lambda listachavevalor: len(listachavevalor[0]), reverse=True)
listasorted = sorted(listasorted, key=lambda listasorted: listasorted[1][0])
debug = 0