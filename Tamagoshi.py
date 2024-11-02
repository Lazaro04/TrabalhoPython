class Tamagoshi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarnome(self, nome):
        self.nome = nome

    def alterarfome(self, fome):
        self.fome = fome

    def alterarsaude(self, saude):
        self.saude = saude

    def alterarIdade(self, idade):
        self.idade = idade

    def __str__(self):
        return (f"Nome do Tamagoshi: {self.nome} \n"
                f"Nível de fome:  {self.fome} \n"
                f"Nível de saúde: {self.saude} \n"
                f"Idade: {self.idade} \n")


NovoTama1 = Tamagoshi("Goshi1",
                      0,
                      0,
                      0)


NovoTama2 = Tamagoshi("Goshi2",
                      0,
                      0,
                      0)

NovoTama1.alterarnome("Godin")
NovoTama1.alterarfome(4)
NovoTama1.alterarsaude(1)
NovoTama1.alterarIdade(8)

NovoTama2.alterarnome("Joelma")
NovoTama2.alterarfome(6)
NovoTama2.alterarsaude(8)
NovoTama2.alterarIdade(9)

print(NovoTama1.__str__())

print(NovoTama2.__str__())

