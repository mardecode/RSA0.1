#print ord('C')
#print chr(98)

def toNumeros(palabra):
	xs = []
	for i in palabra:
		xs.append(ord(i))

	return xs

def toLetras(xs):
	letras = []
	for i in xs:
		letras.append(chr(i))
	return letras

def primo(n):
	xs = [7,13,17,19,23,29,31,37]
	print "Se eligio, ", xs[n]
	return xs[n]

def euler(p,q):
	return (p-1)*(q-1)

def mcd(a,b):
	while (b!=0):
		at = a
		a = b
		b = at % b
	return a

def coprimo(a,b):
	if (mcd(a,b)==1):
		return True
	else:
		return False

def hallarE(phi):
	c = 0
	for i in range(2,phi):
		if coprimo(i,phi):
			c+=1
			if c==3:
				return i


def hallarD(e,phi):
	for i in range(e+1,phi):
		if ( (e*i - 1 ) % phi ==  0):
			return i

def encriptar(pal,n,x):
	xs = []
	for i in pal:
		xs.append(funcion(i,n,x))
	return xs

def funcion(letra, n,x):
	return letra**x % n
