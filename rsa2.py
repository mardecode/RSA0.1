import random
#------------------------------------------------------
'''
def funcion(letra,n,x):
	return letra**x%n
'''
'''
def mcd(a,b):
	while (b!=0):
		varA = a
		a = b
		b= varA % b
	return a
def coprimo(a,b):
	if (mcd(a,b)==1):
		return True
	else:
		return False
'''
#--------------------------------------------------------

def Anumeros(palabra):
	xs=[]
	for i in palabra:
		xs.append(ord(i))
	return xs

def Aletras(palabra):
	xs=[]
	for i in palabra:
		xs.append(chr(i))
	return xs

#print Aletras([97])
#-----------------------------------------------------

def pXq(p,q):
	return p*q

def euler(p,q):#phi
	return (p-1)*(q-1)
	
def hallarE(phi):
	p = primo()
	while (p>phi):
		p=primo()
	return p

def hallandoD(e,phi):
	g=[phi,e]
	u=[1,0]
	v=[0,1]
	i=1
	while (g[i] != 0 ):
		y=g[i-1]//g[i]
		g.append(g[i-1] - y*g[i])
		u.append(u[i-1] - y*u[i])
		v.append(v[i-1] - y*v[i])
		i+=1
	if (v[i-1]<0):
		v[i-1] = v[i -1] + phi
	return v[i-1]

		

def primo():
	xs=[2,3,5,7,11,13,17,19,23,29, 	31,37,41,43,47,53,59,61,67,71,	73,79,83,89,97,101,103,107,109,113,	127,131,137,139,149,151,157,163,167,173,	179,181,191,193,197,199,211,223,227,229,	233,239,241,251,257,263,269,271,277,281,
	283,293,307,311,313,317,331,337,347,349,
	353,359,367,373,379,383,389,397,401,409,
	419,421,431,433,439,443,449,457,461,463,
	467,479,487,491,499,503,509,521,523,541,
	547,557,563,569,571,577]

	aleatorio=random.randint(0,len(xs))
	#numero=2**xs[aleatorio-1]-1
	numero =xs[aleatorio-1]
	return numero


def modulo(a,b,c): # a .. elevado a b .... modulo c
	binar="{0:b}".format(b)
	#print "binario",binar
	xs = []
	i=1
	while (i<=b):
		d = a % c
		xs.append(d)
		a=d*d 
		i=i*2
#	print xs ## toda la lista
	ultimo= len (binar)-1
	respuesta = 1

	for i in range(0,len(binar)):
		if (binar[len(binar)-i-1]=="1"):
			respuesta = respuesta * xs[i]
	#print "esta es la respuesta",respuesta%c
	return respuesta%c
		
def encriptar(pal,n,x):
	xs=[]
	for i in pal:
		xs.append(modulo(i,n,x))
	return xs

#encriptado=modulo(123, 17, 3233)
#print "encriptando 123  ---->>>",encriptado
#desencriptando = modulo(encriptado, 2753, 3233)
#print "desencriptando ------>>>", desencriptando

#print 2**43-1
#modulo (123, 17, 3233)
#modulo(855, 2753, 3233)
#print primo()
#modulo (739721312827123456789012345678978877172345678767678909876549723729, 237234567897777498273973123456982793, 73672)