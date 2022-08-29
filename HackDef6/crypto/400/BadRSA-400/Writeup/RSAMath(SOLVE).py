#
# RSAMath.py - Mathematics functions used in RSA and plaintext search
#
# Copyright (c) Microsoft Corporation. Licensed under the MIT license.
#

import time
import random
from Crypto.Util.number import *

def xgcd(x,y):
    if (x < y):
        (x,y) = (y,x)
    (a,b,g,u,v,w) = (1,0,x,0,1,y)
    while (w > 0):
        q = g//w
        (a,b,g,u,v,w) = (u,v,w,a-q*u,b-q*v,g-q*w)
    return (a,b,g)

def modinv(x,N):
    if (x >= N):
        x = x%N
    (a,b,g) = xgcd(N,x)
    if (1 != g):
        return None
    if (b < 0):
        b = (b + N) % N
    return b

def find_generator(a,b,N):
    g = 2
    found = False
    while ((g < 1000) and (~found)):
        (a_order_good,b_order_good) = (1 != pow(g,a,N),1 != pow(g,b,N))
        if (a_order_good and b_order_good):
            found = True;
            break;
        g = g + 1
    if (not found):
        print("ERROR: Unable to find a generator.")
        return None
    return g


def calculate_decrypt_exponent(p, q, e):
    phiN = (p-1)*(q-1)
    d = modinv(e, phiN)
    if (None == d):
        print("ERROR calculating decrypt exponent.")
    return d

def rsa_crt_precompute(p, q):
    N = p*q
    pinv = modinv(p,q)
    qinv = modinv(q,p)
    Mp = qinv*q % N
    Mq = pinv*p % N
    return (Mp, Mq)

def rsa_crt_mod_exp(x, a, p, q, Mp, Mq):
    N = p*q
    xp = x % p
    xq = x % q
    ap = a % (p-1)
    aq = a % (q-1)
    yp = pow(xp, ap, p)
    yq = pow(xq, aq, q)
    y = (yp*Mp + yq*Mq) % N
    return y
    

def fix_bad_rsa_encryption(p,q,e,ct):
    if (((2**16)+1) < e):
        print("ERROR: Supplied public exponent is larger than Fermat-4.")
        return None

    (bad_p,bad_q) = (0 == ((p-1)%e),0 == ((q-1)%e))

    if (bad_p and bad_q):
        print("ERROR: both p and q are divisible by the public exponent.")
        return None

    # Make p the bad prime
    if (bad_q):
        (p,q) = (q,p)

    if (0 == (p-1)%(e*e)):
        print("ERROR: bad prime is divisible by square of public exponent.")

    N = p*q
    phi_N = (p-1)*(q-1)
    phihat_N = phi_N//e
    print(phihat_N)
    d = modinv(e,phihat_N)
    print(phi_N)
    print(phi_N/e)
    print(xgcd(e,phihat_N))
    print(phihat_N % e)
    print("Searching for good generator...")
    g = find_generator(e,phihat_N,N)
    print("Good generator found in ")
    print(g)

    g_e_torsion = pow(g, phihat_N, N)
    z = pow(ct,d,N)
    print("non crt private key operations done")

    (Mp,Mq) = rsa_crt_precompute(p,q)
    g_e_torsion = rsa_crt_mod_exp(g, phihat_N, p, q, Mp, Mq)
    z = rsa_crt_mod_exp(ct, d, p, q, Mp, Mq)
    print("crt private key operations done ")

    print("g of e torsion group = " + str(g_e_torsion))

    print("Searching for plaintext...")
    i = 1
    ell = g_e_torsion
    while (i < e):
        pt_hat = ell*z % N
        if (b"hackdef" in long_to_bytes(pt_hat)):
            print("plaintext found.")
            break
        i = i + 1
        ell = ell*g_e_torsion % N
    print("Plaintext search finished")
    print(long_to_bytes(pt_hat))
    return pt_hat

e=107
p=12536147829913601201574658115660726604571988564101541766373941725058574740077270580054848278730428945635154272545537676807690738090529214174949207136493503
q=12083802684515504132977630065980248618286234470269942961916249367218791621688632405144257885834935485262696753929308883009177587343073204000098436636187131
ct=42385559044526029827350450605572796944455742180231563716778807858922428193394026710826897770661071283529445731155834952933978674979303514113985524783823912940303516954316731226489229811938473025024306709718264849129282145109472463556671691537380573875932190976082480521152130576996796529082908762210248272902

fix_bad_rsa_encryption(p,q,e,ct)

