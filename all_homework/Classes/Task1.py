class Animal:
    def __init__(self, type):
        self.type_animal = type
        self.voice = 'ГАВ!'
    def give_me_voice (self):
        print (self.voice)
Bim=Animal('dog')
Bim.give_me_voice()
