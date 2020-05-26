import model
import bottle

vislice = model.Vislice()

SECRET = 'vislice'

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('index')

@bottle.get('/img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, root='img')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret=SECRET)
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SECRET)
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra', igra=igra, stanje=stanje, id_igre=id_igre, zmaga=model.ZMAGA, poraz=model.PORAZ)

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SECRET)
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/')

bottle.run(reloader=True, debug=True)