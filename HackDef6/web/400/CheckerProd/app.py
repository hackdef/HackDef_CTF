import uuid

import bcrypt
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex

app.config['MONGO_dbname'] = 'checker'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/checker'

mongo = PyMongo(app)

# Espero que esten todos
teams = ['Robotics_Republic', 'F3Society ', 'Axolt', 'Cypherpunks', 'ReconTeam', '0x1balbá', 'Alek1', 'PumaHat',
         'Dinohacks', 'ITC1412', 'Gerardo Muriel Ramos', 'Syst3mAuth0rity',
         'Emerald Code', 'Paranoid', 'w1ldc4t5_SR!', 'Riders', 'S0nofaB1t', '0xCr4ckers', 'watch_d0gs',
         '.codebreakers', 'Lučko', 'slither', 'Dungeons and Hacking', 'NFTeam',
         'Daicitos Atómicos', 'Piratas del Caribe', 'PumaL33t', 'ug0tpwn', 'Pwned', '4ndromed4dd', 'PHCT_22-2',
         'P0liH4cks', ' kronichiwa', 'Script Kiddies', 'M4r1hu4n0l3z', 'DoomHack', 'Rebeldes del malware', 'dpalme',
         'Kst0r', 'Cryptile', 'k3vzz', 'M4trix0verride', 'I dunno', 'StarPoint', 'Cosmic Opossum', ' Dungeon and Hack',
         'F3Society', 'Cypherpunks', 'Robotics_Republic', '3rick', 'Matrix13', '0xByt3s', 'HackBuap Fcc', 'Confiker',
         'dYNAM0', 'm4lmex', 'Kriptowires', 'D1ie3z', 'H3llst0rm', 'Synonymous', 'Kummerspeck', 'Jinetes 2', 'DarkSide',
         'ARP-Attackers', 'Revolver', 'Byt3c0d3', 'WWW\'s', 'sibaritas', 'Papitos Club', 'Dinamic',
         'ingenieros en tacos de canasta', 'R3N3G4D35', 'B1otme', 'matrix12', 'H4X0R', 'C3N71N3L4'
         ]
types = ["priv", "pub"]

randomString = uuid.uuid4().hex
admin_user = {'username': 'admin', 'password': bcrypt.hashpw(randomString.encode('utf-8'), bcrypt.gensalt(14)),
              'team': 'Admins'}
# Que bueno que no guarde así este registro, pero ahí esta en la DB así de esta forma
# ticket_admin = {'id': str(random.randint(0, 100)), 'title': 'Secretos ', 'details': os.getenv('FLAG'),
#                'type': 'priv', 'team': 'Admins'}
mongo.db.users.drop()
mongo.db.users.insert_one(admin_user)


# Manejemos bien los mensajes de error
class Message():
    def __init__(self, message):
        self.message = message


# La ruta principal
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return render_template("signin.html")


# Para que se registren los usuarios
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        signup_user = users.find_one({'username': request.form['username']})
        if signup_user:
            flash('El nombre de usuario ' + request.form['username'] + ' ya existe.')
            return render_template('signup.html', teamsList=teams)
        else:
            # Que no se registre alguien externo
            if request.form['team'] not in teams:
                flash('El nombre de equipo ' + request.form['team'] + ' no es valido')
                return render_template('signup.html', teamsList=teams)
            hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt(14))
            users.insert_one({'username': request.form['username'], 'password': hashed, 'team': request.form['team']})
            return redirect(url_for('signin'))
    return render_template('signup.html', teamsList=teams)


# Ruta para logearse en la aplicacion
@app.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Nada de hackearse el login ni inyecciones
        users = mongo.db.users
        signin_user = users.find_one({'username': request.form['username']})
        if signin_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), signin_user['password']) == signin_user[
                'password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        flash('Datos incorrectos.')
        return render_template('signin.html')
    return render_template('signin.html')


# El logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# Manejar los errores
@app.route('/error/<error>')
@app.route('/error/<error>/<base>')
def error_message(base='error.message', error='error'):
    if 'username' not in session:
        return render_template("signin.html")
    # Nada de inyectar cosas en el template
    # Nada de XSS
    err = Message(error)
    final_error = "Error: {" + base + "}"
    complete_error = final_error.format(error=err)
    return render_template('error.html', username=session['username'], error=complete_error)


# Para crear los tickets
@app.route('/new_ticket', methods=['POST', 'GET'])
def new_ticket():
    if 'username' not in session:
        return render_template("signin.html")
    if request.method == 'POST':
        tickets = mongo.db.tickets
        users = mongo.db.users
        user = users.find_one({'username': session['username']})
        # Validar que este lleno el formulario
        if len(request.form['title']) == 0 or len(request.form['details']) == 0 or len(request.form['type']) == 0:
            return redirect('/error/No se pueden tener campos vacíos')
        if request.form['type'] not in types:
            return redirect('/error/No se pueden tener campos vacíos')

        ticket_data = {
            'id': uuid.uuid4().hex,
            'title': request.form['title'],
            'details': request.form['details'],
            'type': request.form['type'],
            'team': user['team']
        }
        tickets.insert_one(ticket_data)
        return redirect(url_for('tickets'))
    return render_template('newticket.html', username=session['username'])


# Lista de los tickets
@app.route('/tickets')
def tickets():
    if 'username' not in session:
        return render_template("signin.html")
    reports = mongo.db.tickets
    # Si era asi?
    report_list = reports.find({'type': 'pub'}).sort([('_id', -1)]).limit(50)
    return render_template('tickets.html', username=session['username'], tickets=report_list)


# Ver el ticket por su ID
@app.route('/ticket/<id>')
def ticket(id):
    if 'username' not in session:
        return render_template("signin.html")
    tickets_list = mongo.db.tickets
    actual_ticket = tickets_list.find_one({'id': id})
    if actual_ticket['type'] == 'pub':
        return render_template('ticket.html', username=session['username'], ticket=actual_ticket)
    else:
        # Solo admin puede ver los privados
        if session['username'] != 'admin':
            return redirect('/error/No tienes permisos de admin')
        else:
            return render_template('ticket.html', username=session['username'], ticket=actual_ticket)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=4008)
