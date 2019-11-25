from collections import defaultdict
seq1 = [-2,3,-2,3,5,3,7,1,4,-5,1,4,-5,1,4,-5]
seq2 = [1,2,3,4,5,6,0,1,2,3,4,5,6,1,2,3,1,2,3]

def find_recurrences_old(seq):
	dic = {}
	for p1 in range(len(seq)):
		for p2 in range(p1+1,len(seq)+1):
			dic.setdefault(tuple(seq[p1:p2]), []).append((p1,p2))
	def clean(dic):
		cleandic = {}
		for key, value in dic.items():
			if len(value) > 1:
				cleandic.setdefault(key,value)
		return cleandic
	cleandic = clean(dic)
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
	return clean(onlybigs)

def find_recurrences(seq):
    seq_size = len(seq)
    d = defaultdict(list)

    for i in range(0, seq_size):
        for j in range(i + 1, seq_size):
            d[tuple(seq[i:j])].append((i, j))

    d = dict(sorted(((k, v) for k, v in d.items() if len(v) > 1),
                    key=lambda x: len(x[0]), reverse=True))
    d_copy = d.copy()

    for k, v in d_copy.items():
        if k not in d:
            continue
        k_str = f" {' '.join(map(str, k))} "
        for k_ in d.keys() - set([k]):
            if f" {' '.join(map(str, k_))} " in k_str:
                del d[k_]
    return d

print(find_recurrences_old(seq2))
print(find_recurrences(seq2))