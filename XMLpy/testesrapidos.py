a = ['a','b','c','d']
b = ['a','b','c','d']

if all(b) in a:
    print(True)
else:
    print(False)

for e in a:
    if e in b:
        print(True)
    else:
        print(False)