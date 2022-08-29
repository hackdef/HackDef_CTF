import random
from Crypto.Util.number import *
from flag import FLAG

e=getPrime(7)
while(1):
    p=getPrime(512)
    q=getPrime(512)
    if(GCD((p-1)*(q-1),e)!=1):
        break
pt=bytes_to_long(FLAG)
ct=pow(pt,e,p*q)

f=open("output.txt","w")
f.write("e="+str(e)+"\n")
f.write("p="+str(p)+"\n")
f.write("q="+str(q)+"\n")
f.write("ct="+str(ct)+"\n")
f.close()