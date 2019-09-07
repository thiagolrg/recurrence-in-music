Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):print(i, a[i])
SyntaxError: multiple statements found while compiling a single statement
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> a
['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
	print(i, a[i])

	
0 Mary
1 had
2 a
3 little
4 lamb
>>> for i in range(len(a)):
	print(i, a[i,i+1])

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    print(i, a[i,i+1])
TypeError: list indices must be integers or slices, not tuple
>>> for i in range(len(a)):
	print(i, a[i]a[i+1])
	
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	print(i, a[i], [i+1])

	
0 Mary [1]
1 had [2]
2 a [3]
3 little [4]
4 lamb [5]
>>> for i in range(len(a)):
	print(i, a[i], a[i+1])

	
0 Mary had
1 had a
2 a little
3 little lamb
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    print(i, a[i], a[i+1])
IndexError: list index out of range
>>> for i in range(len(a)):
	print(i, a[i:i+1])

	
0 ['Mary']
1 ['had']
2 ['a']
3 ['little']
4 ['lamb']
>>> a
['Mary', 'had', 'a', 'little', 'lamb']
>>> a[1]
'had'
>>> a[0:0]
[]
>>> a[0:1]
['Mary']
>>> for i in range(len(a)):
	print(i, a[i:i+2])

	
0 ['Mary', 'had']
1 ['had', 'a']
2 ['a', 'little']
3 ['little', 'lamb']
4 ['lamb']
>>> teste = list()
>>> for i in range(len(a)):
	teste = teste + (i, a[i:i+2])

	
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    teste = teste + (i, a[i:i+2])
TypeError: can only concatenate list (not "tuple") to list
>>> for i in range(len(a)):
	teste = teste + a[i:i+2]

	
>>> teste
['Mary', 'had', 'had', 'a', 'a', 'little', 'little', 'lamb', 'lamb']
>>> for i in range(len(a)):
	print(a[i:i+2])

	
['Mary', 'had']
['had', 'a']
['a', 'little']
['little', 'lamb']
['lamb']
>>> lista = list(range(1,11))
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		print(lista[posição1:posição2)
		      
SyntaxError: invalid syntax
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		print(lista[posição1:posição2])

		
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
[]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[]
[]
[]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[]
[]
[]
[]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[]
[]
[]
[]
[]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[]
[]
[]
[]
[]
[]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[]
[]
[]
[]
[]
[]
[]
[7]
[7, 8]
[7, 8, 9]
[]
[]
[]
[]
[]
[]
[]
[]
[8]
[8, 9]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[9]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		print(lista[posição1:posição2+1])

		
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
[]
[]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9, 10]
[]
[]
[]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9, 10]
[]
[]
[]
[]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 10]
[]
[]
[]
[]
[]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[6, 7, 8, 9, 10]
[]
[]
[]
[]
[]
[]
[7]
[7, 8]
[7, 8, 9]
[7, 8, 9, 10]
[]
[]
[]
[]
[]
[]
[]
[8]
[8, 9]
[8, 9, 10]
[]
[]
[]
[]
[]
[]
[]
[]
[9]
[9, 10]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[10]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2> posição 1:
			print(lista[posição1:posição2+])
			
SyntaxError: invalid syntax
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 > posição1:
			print(lista[posição1:posição2+])
			
SyntaxError: invalid syntax
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 > posição1:
			print(lista[posição1:posição2])

			
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[7]
[7, 8]
[7, 8, 9]
[8]
[8, 9]
[9]
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 = posição1:
			print(lista[posição1:posição2])
			
SyntaxError: invalid syntax
>>> 
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 == posição1:
			print(lista[posição1:posição2])

			
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 >= posição1:
			print(lista[posição1:posição2])

			
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[]
[7]
[7, 8]
[7, 8, 9]
[]
[8]
[8, 9]
[]
[9]
[]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
			print(lista[posição1:posição2])

			
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
[]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[]
[]
[]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[]
[]
[]
[]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[]
[]
[]
[]
[]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[]
[]
[]
[]
[]
[]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[]
[]
[]
[]
[]
[]
[]
[7]
[7, 8]
[7, 8, 9]
[]
[]
[]
[]
[]
[]
[]
[]
[8]
[8, 9]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[9]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
>>> for posição1 in range(len(lista)):
	for posição2 in range(len(lista)):
		if posição2 >= posição1:
			print(lista[posição1:posição2+1])

			
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9, 10]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9, 10]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 10]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[6, 7, 8, 9, 10]
[7]
[7, 8]
[7, 8, 9]
[7, 8, 9, 10]
[8]
[8, 9]
[8, 9, 10]
[9]
[9, 10]
[10]
>>> for posição1 in range(len(lista)):
	for posição2 in range(posição1, len(lista)):
		print(lista[posição1:posição2+1])

		
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9, 10]
[4]
[4, 5]
[4, 5, 6]
[4, 5, 6, 7]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9, 10]
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 10]
[6]
[6, 7]
[6, 7, 8]
[6, 7, 8, 9]
[6, 7, 8, 9, 10]
[7]
[7, 8]
[7, 8, 9]
[7, 8, 9, 10]
[8]
[8, 9]
[8, 9, 10]
[9]
[9, 10]
[10]
>>> for nota in range(len(listanota)):
	lista[nota+1] - lista[nota]

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    for nota in range(len(listanota)):
NameError: name 'listanota' is not defined
>>> listanota = [56, 81, 64, 36]
>>> for nota in range(len(listanota)):
	lista[nota+1] - lista[nota]

	
1
1
1
1
>>> lista = [56, 81, 64, 36]
>>> listanota = [56, 81, 64, 36]
>>> 
>>> lista = [56, 81, 64, 36]
>>> for nota in range(len(listanota)):
	lista[nota+1] - lista[nota]

	
25
-17
-28
Traceback (most recent call last):
  File "<pyshell#67>", line 2, in <module>
    lista[nota+1] - lista[nota]
IndexError: list index out of range
>>> listanota
[56, 81, 64, 36]
>>> lista = [56, 81, 64, 36],
>>> for nota in range(len(lista)):
	lista[nota+1] - lista[nota]

	
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    lista[nota+1] - lista[nota]
IndexError: tuple index out of range
>>> for posição in range(len(lista)):
	lista[posiçao+1] - lista[posição]

	
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    lista[posiçao+1] - lista[posição]
NameError: name 'posiçao' is not defined
>>> for posição in range(len(lista)):
	lista[posição+1] - lista[posição]

	
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    lista[posição+1] - lista[posição]
IndexError: tuple index out of range
>>> lista = [56, 81, 64, 36]
>>> for posição in range(len(lista)):
	lista[posição+1] - lista[posição]

	
25
-17
-28
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    lista[posição+1] - lista[posição]
IndexError: list index out of range
>>> for posição in range(len(lista)):
	if posição+1 =< len(lista):
		lista[posição+1] - lista[posição]
		
SyntaxError: invalid syntax
>>> 
>>> for posição in range(len(lista)):
	if posição+1 <= len(lista):
		lista[posição+1] - lista[posição]

		
25
-17
-28
Traceback (most recent call last):
  File "<pyshell#82>", line 3, in <module>
    lista[posição+1] - lista[posição]
IndexError: list index out of range
>>> for posição in range(len(lista)):
	if posição+1 < len(lista):
		lista[posição+1] - lista[posição]

		
25
-17
-28
>>> for posição in range(len(lista)):
	if posição+1 < len(lista):
		print(lista[posição+1))
		lista[posição+1] - lista[posição]
		
SyntaxError: invalid syntax
>>> 
>>> for posição in range(len(lista)):
	if posição+1 < len(lista):
		print(lista[posição+1])
		lista[posição+1] - lista[posição]

		
81
25
64
-17
36
-28
>>> for posição in range(len(lista)):
	print(posição)
	if posição+1 < len(lista):
		lista[posição+1] - lista[posição]

		
0
25
1
-17
2
-28
3
>>> for posição in range(len(lista)):
	print(posição)
	if posição = len(lista)-1:
		lista[posição+1] - lista[posição]
		
SyntaxError: invalid syntax
>>> for posição in range(len(lista)):
	print(posição)
	if posição == len(lista)-1:
		lista[posição+1] - lista[posição]

		
0
1
2
3
Traceback (most recent call last):
  File "<pyshell#93>", line 4, in <module>
    lista[posição+1] - lista[posição]
IndexError: list index out of range
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= len(lista)-1:
		lista[posição+1] - lista[posição]

		
0
25
1
-17
2
-28
3
Traceback (most recent call last):
  File "<pyshell#95>", line 4, in <module>
    lista[posição+1] - lista[posição]
IndexError: list index out of range
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= len((lista)-1):
		lista[posição+1] - lista[posição]

		
0
Traceback (most recent call last):
  File "<pyshell#97>", line 3, in <module>
    if posição <= len((lista)-1):
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= len(lista-1):
		lista[posição+1] - lista[posição]

		
0
Traceback (most recent call last):
  File "<pyshell#101>", line 3, in <module>
    if posição <= len(lista-1):
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= (len(lista)-1):
		lista[posição+1] - lista[posição]

		
0
25
1
-17
2
-28
3
Traceback (most recent call last):
  File "<pyshell#103>", line 4, in <module>
    lista[posição+1] - lista[posição]
IndexError: list index out of range
>>> len(lista)
4
>>> lista
[56, 81, 64, 36]
>>> range(len(lista))
range(0, 4)
>>> list(range(len(lista)))
[0, 1, 2, 3]
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= (len(lista)-2):
		lista[posição+1] - lista[posição]

		
0
25
1
-17
2
-28
3
>>> len(lista)
4
>>> range(0,4)
range(0, 4)
>>> for n in range(0,4)
SyntaxError: invalid syntax
>>> for n in range(0,4):
	print(n)

	
0
1
2
3
>>> for posição in range(len(lista)):
	print(posição)
	if posição <= (len(lista)-2):
		lista[posição+1] - lista[posição]

		
0
25
1
-17
2
-28
3
>>> for posição in range(len(lista)):
	if posição <= (len(lista)-2):
		lista[posição+1] - lista[posição]

		
25
-17
-28
>>> lista = [13, 15, 18, 10, 8, 20, 14]
>>> for posição in range(len(lista)):
	if posição <= (len(lista)-2):			# para quando a posição é <= o
		lista[posição+1] - lista[posição]

		
2
3
-8
-2
12
-6
>>> listanota = [13, 15, 18, 10, 8, 20, 14]
>>> listaintervalo = list()
>>> for posição in range(len(lista)):
	if posição <= (len(lista)-2):			# para quando a posição é <= o
		listaintervalo.append(lista[posição+1] - lista[posição])

		
>>> listaintervalo
[2, 3, -8, -2, 12, -6]
>>> listasegint = list()
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		listasegint.append(lista[posição1:posição2+1])

		
>>> listasegint
[[13], [13, 15], [13, 15, 18], [13, 15, 18, 10], [13, 15, 18, 10, 8], [13, 15, 18, 10, 8, 20], [15], [15, 18], [15, 18, 10], [15, 18, 10, 8], [15, 18, 10, 8, 20], [18], [18, 10], [18, 10, 8], [18, 10, 8, 20], [10], [10, 8], [10, 8, 20], [8], [8, 20], [20]]
>>> listanota = [13, 15, 18, 10, 8, 20, 14]
>>> listaintervalo = list()
>>> for posição in range(len(lista)):
	if posição <= (len(lista)-2):			# para quando a posição é <= o
		listaintervalo.append(lista[posição+1] - lista[posição])

		
>>> listasegint = list()
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		listasegint.append(lista[posição1:posição2+1])

		
>>> listasegint
[[13], [13, 15], [13, 15, 18], [13, 15, 18, 10], [13, 15, 18, 10, 8], [13, 15, 18, 10, 8, 20], [15], [15, 18], [15, 18, 10], [15, 18, 10, 8], [15, 18, 10, 8, 20], [18], [18, 10], [18, 10, 8], [18, 10, 8, 20], [10], [10, 8], [10, 8, 20], [8], [8, 20], [20]]
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		listasegint.append(listaintervalo[posição1:posição2+1])

		
>>> listasegint
[[13], [13, 15], [13, 15, 18], [13, 15, 18, 10], [13, 15, 18, 10, 8], [13, 15, 18, 10, 8, 20], [15], [15, 18], [15, 18, 10], [15, 18, 10, 8], [15, 18, 10, 8, 20], [18], [18, 10], [18, 10, 8], [18, 10, 8, 20], [10], [10, 8], [10, 8, 20], [8], [8, 20], [20], [2], [2, 3], [2, 3, -8], [2, 3, -8, -2], [2, 3, -8, -2, 12], [2, 3, -8, -2, 12, -6], [3], [3, -8], [3, -8, -2], [3, -8, -2, 12], [3, -8, -2, 12, -6], [-8], [-8, -2], [-8, -2, 12], [-8, -2, 12, -6], [-2], [-2, 12], [-2, 12, -6], [12], [12, -6], [-6]]
>>> listasegint = list()
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		listasegint.append(listaintervalo[posição1:posição2+1])

		
>>> listasegint
[[2], [2, 3], [2, 3, -8], [2, 3, -8, -2], [2, 3, -8, -2, 12], [2, 3, -8, -2, 12, -6], [3], [3, -8], [3, -8, -2], [3, -8, -2, 12], [3, -8, -2, 12, -6], [-8], [-8, -2], [-8, -2, 12], [-8, -2, 12, -6], [-2], [-2, 12], [-2, 12, -6], [12], [12, -6], [-6]]
>>> 
>>> for posição1 in range(len(lista)):
	print(posição1)
	for posição2 in range(posição1, len(lista)):
		print(lista[posição1:posição2+1])

		
0
[13]
[13, 15]
[13, 15, 18]
[13, 15, 18, 10]
[13, 15, 18, 10, 8]
[13, 15, 18, 10, 8, 20]
[13, 15, 18, 10, 8, 20, 14]
1
[15]
[15, 18]
[15, 18, 10]
[15, 18, 10, 8]
[15, 18, 10, 8, 20]
[15, 18, 10, 8, 20, 14]
2
[18]
[18, 10]
[18, 10, 8]
[18, 10, 8, 20]
[18, 10, 8, 20, 14]
3
[10]
[10, 8]
[10, 8, 20]
[10, 8, 20, 14]
4
[8]
[8, 20]
[8, 20, 14]
5
[20]
[20, 14]
6
[14]
>>> for posição1 in range(len(lista)):
	print(posição1)
	for posição2 in range(posição1, len(lista)):
		print(posição2 - posição1
		print(lista[posição1:posição2+1])
		      
SyntaxError: invalid syntax
>>> for posição1 in range(len(lista)):
	print(posição1)
	for posição2 in range(posição1, len(lista)):
		print(posição2 - posição1)
		print(lista[posição1:posição2+1])

		
0
0
[13]
1
[13, 15]
2
[13, 15, 18]
3
[13, 15, 18, 10]
4
[13, 15, 18, 10, 8]
5
[13, 15, 18, 10, 8, 20]
6
[13, 15, 18, 10, 8, 20, 14]
1
0
[15]
1
[15, 18]
2
[15, 18, 10]
3
[15, 18, 10, 8]
4
[15, 18, 10, 8, 20]
5
[15, 18, 10, 8, 20, 14]
2
0
[18]
1
[18, 10]
2
[18, 10, 8]
3
[18, 10, 8, 20]
4
[18, 10, 8, 20, 14]
3
0
[10]
1
[10, 8]
2
[10, 8, 20]
3
[10, 8, 20, 14]
4
0
[8]
1
[8, 20]
2
[8, 20, 14]
5
0
[20]
1
[20, 14]
6
0
[14]
>>> for posição1 in range(len(lista)):
	print(posição1)
	for posição2 in range(posição1, len(lista)):
		print((posição2+1) - posição1)
		print(lista[posição1:posição2+1])

		
0
1
[13]
2
[13, 15]
3
[13, 15, 18]
4
[13, 15, 18, 10]
5
[13, 15, 18, 10, 8]
6
[13, 15, 18, 10, 8, 20]
7
[13, 15, 18, 10, 8, 20, 14]
1
1
[15]
2
[15, 18]
3
[15, 18, 10]
4
[15, 18, 10, 8]
5
[15, 18, 10, 8, 20]
6
[15, 18, 10, 8, 20, 14]
2
1
[18]
2
[18, 10]
3
[18, 10, 8]
4
[18, 10, 8, 20]
5
[18, 10, 8, 20, 14]
3
1
[10]
2
[10, 8]
3
[10, 8, 20]
4
[10, 8, 20, 14]
4
1
[8]
2
[8, 20]
3
[8, 20, 14]
5
1
[20]
2
[20, 14]
6
1
[14]
>>> for posição1 in range(len(lista)):
	for posição2 in range(posição1, len(lista)):
		print(posição 1, (posição2+1) - posição1, lista[posição1:posição2+1])
		
SyntaxError: invalid syntax
>>> for posição1 in range(len(lista)):
	for posição2 in range(posição1, len(lista)):
		print(posição1, (posição2+1) - posição1, lista[posição1:posição2+1])

		
0 1 [13]
0 2 [13, 15]
0 3 [13, 15, 18]
0 4 [13, 15, 18, 10]
0 5 [13, 15, 18, 10, 8]
0 6 [13, 15, 18, 10, 8, 20]
0 7 [13, 15, 18, 10, 8, 20, 14]
1 1 [15]
1 2 [15, 18]
1 3 [15, 18, 10]
1 4 [15, 18, 10, 8]
1 5 [15, 18, 10, 8, 20]
1 6 [15, 18, 10, 8, 20, 14]
2 1 [18]
2 2 [18, 10]
2 3 [18, 10, 8]
2 4 [18, 10, 8, 20]
2 5 [18, 10, 8, 20, 14]
3 1 [10]
3 2 [10, 8]
3 3 [10, 8, 20]
3 4 [10, 8, 20, 14]
4 1 [8]
4 2 [8, 20]
4 3 [8, 20, 14]
5 1 [20]
5 2 [20, 14]
6 1 [14]
>>> listalocalização = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]]
>>> listalocalização
[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]]
>>> listanotas
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    listanotas
NameError: name 'listanotas' is not defined
>>> listanota = lista
>>> listanota
[13, 15, 18, 10, 8, 20, 14]
>>> listaintervalo =
SyntaxError: invalid syntax
>>> listaintervalo = list()
>>> for posição in range(len(listanota)):
	if posição <= (len(listanota)-2):			
		listaintervalo.append(listanota[posição+1] - listanota[posição])

		
>>> listaintervalo
[2, 3, -8, -2, 12, -6]
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		print(listalocalização[posição1], (posição2+1) - posição1, lista[posição1:posição2+1])

		
[1, 1] 1 [13]
[1, 1] 2 [13, 15]
[1, 1] 3 [13, 15, 18]
[1, 1] 4 [13, 15, 18, 10]
[1, 1] 5 [13, 15, 18, 10, 8]
[1, 1] 6 [13, 15, 18, 10, 8, 20]
[1, 2] 1 [15]
[1, 2] 2 [15, 18]
[1, 2] 3 [15, 18, 10]
[1, 2] 4 [15, 18, 10, 8]
[1, 2] 5 [15, 18, 10, 8, 20]
[1, 3] 1 [18]
[1, 3] 2 [18, 10]
[1, 3] 3 [18, 10, 8]
[1, 3] 4 [18, 10, 8, 20]
[1, 4] 1 [10]
[1, 4] 2 [10, 8]
[1, 4] 3 [10, 8, 20]
[2, 1] 1 [8]
[2, 1] 2 [8, 20]
[2, 2] 1 [20]
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		print(listalocalização[posição1], (posição2+1) - posição1, listaintervalo[posição1:posição2+1])

		
[1, 1] 1 [2]
[1, 1] 2 [2, 3]
[1, 1] 3 [2, 3, -8]
[1, 1] 4 [2, 3, -8, -2]
[1, 1] 5 [2, 3, -8, -2, 12]
[1, 1] 6 [2, 3, -8, -2, 12, -6]
[1, 2] 1 [3]
[1, 2] 2 [3, -8]
[1, 2] 3 [3, -8, -2]
[1, 2] 4 [3, -8, -2, 12]
[1, 2] 5 [3, -8, -2, 12, -6]
[1, 3] 1 [-8]
[1, 3] 2 [-8, -2]
[1, 3] 3 [-8, -2, 12]
[1, 3] 4 [-8, -2, 12, -6]
[1, 4] 1 [-2]
[1, 4] 2 [-2, 12]
[1, 4] 3 [-2, 12, -6]
[2, 1] 1 [12]
[2, 1] 2 [12, -6]
[2, 2] 1 [-6]
>>> listalocalização = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]]
>>> listanota = [13, 15, 18, 10, 8, 20, 14]
>>> lista intervalo = list()
SyntaxError: invalid syntax
>>> listaintervalo = list()
>>> for posição in range(len(listanota)):
	if posição <= (len(listanota)-2):			
		listaintervalo.append(listanota[posição+1] - listanota[posição])

		
>>> listaintervalo
[2, 3, -8, -2, 12, -6]
>>> for posição1 in range(len(listaintervalo)):
	for posição2 in range(posição1, len(listaintervalo)):
		print(listalocalização[posição1], (posição2+1) - posição1, listaintervalo[posição1:posição2+1])

		
[1, 1] 1 [2]
[1, 1] 2 [2, 3]
[1, 1] 3 [2, 3, -8]
[1, 1] 4 [2, 3, -8, -2]
[1, 1] 5 [2, 3, -8, -2, 12]
[1, 1] 6 [2, 3, -8, -2, 12, -6]
[1, 2] 1 [3]
[1, 2] 2 [3, -8]
[1, 2] 3 [3, -8, -2]
[1, 2] 4 [3, -8, -2, 12]
[1, 2] 5 [3, -8, -2, 12, -6]
[1, 3] 1 [-8]
[1, 3] 2 [-8, -2]
[1, 3] 3 [-8, -2, 12]
[1, 3] 4 [-8, -2, 12, -6]
[1, 4] 1 [-2]
[1, 4] 2 [-2, 12]
[1, 4] 3 [-2, 12, -6]
[2, 1] 1 [12]
[2, 1] 2 [12, -6]
[2, 2] 1 [-6]
>>> 
