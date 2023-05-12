class animal:

    def __init__(self, raca, altura, comprimento, peso):

        self.raca = raca
        self.altura = altura
        self.comprimento = comprimento
        self.peso = peso

    def pular(self):
        alturaPulo = self.altura * 2
        print("O cachorro pulou "+str(alturaPulo)+" cm!")

    def comer(self):
        print("O cachorro comeu", self.peso/4, "quilos de comida")

    def beber(self):
        print("O cachorro bebeu", self.peso/2, "litros de água")


toto = animal("Vira-lata", 30, 100, 5)

toto.pular()
toto.comer()
toto.beber()
