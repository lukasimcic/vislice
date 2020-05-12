STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo.lower()
        self.crke = [crka.lower() for crka in crke]

    def napacne_crke(self):
        napacne = [crka for crka in self.crke if crka not in self.geslo]
        return napacne

    def pravilne_crke(self):
        pravilne = [crka for crka in self.crke if crka in self.geslo]
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.lower()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA
            
import random

with open('besede.txt', encoding='utf-8') as dat:  
    bazen_besed = dat.read().split('\n')

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda) 