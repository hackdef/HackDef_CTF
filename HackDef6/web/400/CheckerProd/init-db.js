db.createCollection('tickets')
ticket_admin = {'id': '47', 'title': 'Secretos ', 'details': 'hackdef{F0rm4t_Str1ng_Vuln_ll3g4_a_pyth0n_W3b!!!}',
                'type': 'priv', 'team': 'Admins'}

db.tickets.insertOne(ticket_admin)
