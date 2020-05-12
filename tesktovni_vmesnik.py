import model

def izpis_poraza(igra):
    return f'Žal si izgubil :( geslo je bilo {igra.geslo}'

def izpis_zmage(igra):
    return f'Bravo! Uganil si geslo {igra.geslo} v le {len(igra.crke)} ugibih'

def izpis_igre(igra):
    besedilo = f"""Geslo: {igra.pravilni_del_gesla()}
Nepravilne črke: {igra.nepravilni_ugibi()}
Zmotiš se lahko še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} krat"""
    return besedilo

def zahtevaj_vnos():
    vnos = input("Ugibaj: ")
    if len(vnos) == 1 and vnos.isalpha():
        return vnos
    else:
        return None

def pozeni_vmesnik():
    igra = model.nova_igra()
    
    while True:
        print(izpis_igre(igra))

        crka = zahtevaj_vnos()
        while crka is None:
            print('Napiši le eno črko, prosim.')
            crka = zahtevaj_vnos()

        stanje = igra.ugibaj(crka)

        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
    
    print('Bi želeli še eno igro?')

pozeni_vmesnik()