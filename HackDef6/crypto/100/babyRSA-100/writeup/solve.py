from Crypto.PublicKey import RSA
from Crypto.Util.number import *

key=RSA.import_key(open("public_key","r").read())
n=key.n
e=key.e
ct=open("output.txt","r").read()[1:-1].split(',')
flag=''
for c in ct:
	for i in range(256):
		r=pow(i,e,n)
		if(int(c)==r):
			flag+=chr(i)
			#print (chr(i))
print(flag)

