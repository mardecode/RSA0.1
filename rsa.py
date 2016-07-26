from rsa1 import *
#asndandamd
p = 57#primo(3)
q = 17#primo(6)
print "p y q ",p , q
n = p * q
print "n ",n
phi = euler(p,q)
print "Phi",phi

e = hallarE(phi) #Publico
print "e ",e


d = hallarD(e,phi) #Privado
print "d ",d

secreto = encriptar([123],n,e)

print "Secreto",secreto

des = encriptar(secreto,n,d)
print "Desencriptado", des


# e < phi and coprimo(e,phi)
