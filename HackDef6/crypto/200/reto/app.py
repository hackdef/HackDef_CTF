from flask import Flask, make_response, render_template, request, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(16)
FLAG = os.environ.get('FLAG')


def encrypt(plaintext):
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 16))


def decrypt(ciphertext):
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 16)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not(request.args.get('username')):
            return render_template('login.html')
    try:
        username = request.args.get('username').encode()
    except:
        return 'Cadena invalida'
    if b'admin' == username:
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
    app.run(debug=True, host='0.0.0.0')
