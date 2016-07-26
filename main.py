from rsa2 import *
p=primo()  #numero primo1
q=primo()  #numero primo2

print("p"), p
#print "********************************************"
print ("q") ,q
#print "********************************************"
n = pXq(p,q)
print ("modulo : "),n
#print "********************************************"
phi = euler(p,q)
print ("phi : "), phi
#print "********************************************"
#e= hallarE(phi)
e=37
print ("e : "),e
d=hallandoD(e,phi)
print ("d : "),d
print "********************************************"
"""
secreto = modulo (123,e,n)
print ("encriptar 123  : "),secreto 
print "********************************************"
desencriptar = modulo (secreto,d,n)
print ("desencriptando : "), desencriptar

palabra=Anumeros("hola")
print palabra
print ("palabra hola: "),palabra
palabrahola=encriptar(palabra,e,n)
print ("palabra encriptada: "),palabrahola
asd=encriptar(palabrahola,d,n)
print asd
"""
#print "hola"
archivo = open ("texto.txt")
xs =[]
print archivo.name
for i in archivo:
	for j in i:
		xs.append(ord(j))

palabra=encriptar(xs,e,n)
print palabra
despalabra=encriptar(palabra,d,n)
print despalabra
print Aletras(despalabra)

archivo.close


archivo2 = open	("encriptado.txt","w")

for i in despalabra:
	archivo2.write(str(chr(i)))

archivo2.close


