seq = [-2,3,-2,3,5,3,7,1,4,-5,1,4,-5,1,4,-5]

'''
I want to get all the sequential recurrences and where it happens,
I feel the way I'm doing its too brute force and in reality
I want this for several lists of len 300ish
'''

dic = {}
for p1 in range(len(seq)):
    for p2 in range(p1+1,len(seq)):
        dic.setdefault(tuple(seq[p1:p2]), []).append((p1,p2))
'''
which results in all unique sequences of numbers as keys
and their positions as values, for example:
-2,3: [(0,2),(2,4)]


But also results in a lot of entries that occur only once 
that don't interest me, I'm 'cleaning' these after by taking 
only values that have more than 1 entry:
'''
def clean(dic):
	cleandic = {}
	for key, value in dic.items():
		if len(value) > 1:
			cleandic.setdefault(key,value)
	return cleandic
	
cleandic = clean(dic)
'''
Now for the last step I'm trying to get rid of the ocorrences
that happens inside the bigger ones,
so I sorted the dict by reverse len of keys (bigger keys comes first)
for exemple:
(1,4,-5,1,4,-5) : ([7,13),(10,16)]
...
(1,4,-5) : [(7,10),(10,13)]

The best I came up with to takeout the small ones:
'''
sorteddic = dict(sorted(cleandic.items(), key=lambda item: len(item[0]), reverse=True))

onlybigs = {}
while len(sorteddic) > 0:
	for key1, values1 in sorteddic.items():
		for key2, values2 in sorteddic.copy().items():
			if len(key2) == len(key1):
				continue
			for value1 in values1:     #ex: (7,13)
				for value2 in values2: #ex: (7,10)
					if value2[0] >= value1[0] and value2[1] <= value1[1]:
						sorteddic[key2].pop(sorteddic[key2].index(value2))
		onlybigs.setdefault(key1, sorteddic.pop(key1))
		break

readydic = clean(onlybigs)

print(cleandic)
'''
This last step especially is taking to long because it compares each
value for each key and my guess is the whole process can be
done more efficiently somehow, any insights?
'''