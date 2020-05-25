import model
import bottle

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('index')

@bottle.get('/img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, root='img')

@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect(f'/igra/{id_igre}/')

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra', igra=igra, stanje=stanje, id_igre=id_igre, zmaga=model.ZMAGA, poraz=model.PORAZ)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/{id_igre}/')

bottle.run(reloader=True, debug=True)