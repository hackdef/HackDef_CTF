from flask import Flask, make_response, render_template, request, redirect, url_for
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA
import os
from binascii import unhexlify,hexlify


app = Flask(__name__)

SECRET_KEY = RSA.generate(2048)
FLAG = os.environ.get('FLAG')

def encrypt(plaintext):
    m = bytes_to_long(plaintext)
    s = pow(m, SECRET_KEY.d, SECRET_KEY.n)
    return long_to_bytes(s)

def decrypt(ciphertext):
    s = bytes_to_long(ciphertext)
    m = pow(s, SECRET_KEY.e, SECRET_KEY.n)
    return long_to_bytes(m)

@app.route('/public_key', methods=['GET'])
def public_key():
    return SECRET_KEY.public_key().export_key()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not(request.args.get('username')):
            return render_template('login.html')
    try:
        username = unhexlify(request.args.get('username').encode())
    except:
        return 'Cadena invalida'
    if b'admin' in username:
        return '<h3>Nop, definitivamente tu no eres el Admin ;)</h3>'
    print("Login:", username)
    sessid = encrypt(username).hex()
    resp = make_response(redirect('/'))
    resp.set_cookie('sessid', sessid)
    return resp
    try:
        username =username
    except:
        return 'Bad username'
    return render_template('login.html')


@app.route('/', methods=['GET'])
def index():
    try:
        sessid = request.cookies.get('sessid')
        username = decrypt(bytes.fromhex(sessid)).decode()
        print ("Decode cookie:",username)
    except:
        username = None
    if username is None:
        return ('<h1>Que onda! guest! mmmm... Sorry, No hay flag para ti...</h1>')
    if username == 'admin':
        return (f'<h1>Congrats! Aqui tiense su flag Sr. flag: {FLAG}</h1>')
    return (f'<h1>Que tranza {username}! echale ganas, apoco no puedes iniciar sesión? </h1>')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

