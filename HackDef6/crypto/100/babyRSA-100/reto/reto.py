from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from flag import FLAG
flag=FLAG

SECRET_KEY = RSA.generate(4096)
f=open("public_key","wb").write(SECRET_KEY.public_key().export_key())

ct=[]
for data in flag:
	result=pow(data,SECRET_KEY.e,SECRET_KEY.n)
	ct.append(result)

result=open("output.txt","w").write(str(ct))
