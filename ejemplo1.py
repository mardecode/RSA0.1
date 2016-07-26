palabra = [14,1,13,1]
#amsnans,as

def cifrar2(pal,n,x):
	for i in palabra:
		print cifrar(i,n,x)

def cifrar(letra, n,x):
	return letra**x % n

#print cifrar2(palabra,33,3)
print cifrar(855,3233,2753)
print ("hola")

"""
2,3,5,6

11
12
17
6
"""