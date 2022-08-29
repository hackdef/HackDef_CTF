const express = require("express");
const PORT = 3006;
const bodyParser = require("body-parser");

const app = express();
app.set('view engine', 'ejs');
app.use(express.json());
app.use('/static', express.static('public'))

const MongoClient = require('mongodb').MongoClient;
const mongo_url = 'mongodb://mongo:27018/regextro';
const db_name = 'regextro';
const db_client = new MongoClient(mongo_url);

app.get('/', function (req, res) {
    res.render('home', {error: ""});
})
app.get('/login', function (req, res) {
    res.render('home', {error: ""});
})

app.post('/login', function (req, res) {
    const query = {
        username: req.body.username,
        password: req.body.password
    };

    db.collection('users').findOne(query, function (err, user) {
        if(typeof query.username === 'undefined'||typeof query.password === 'undefined'){
            res.render('home', {error: "¿Qué haces?!!!!!!!"});
        } else if (JSON.stringify(query.password).includes("*")||JSON.stringify(query.password).includes("^")) {
            res.render('home', {error: "Creo que no puedes usar esos caracteres."});
        } else if (!user) {
            res.render('home', {error: "Credenciales incorrectas"});
        } else {
            const pass = user.password;
            if (pass === req.body.password) {
                res.render('flag');
            } else {
                res.render('home', {error: "Esta no es la password del admin, largo de aquí"});
            }
        }
    });
});


app.listen(PORT, () => {
    db = db_client.db(db_name);
    console.log(` ${PORT}`);
});
