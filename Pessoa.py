class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        return self.idade + 1

    def engordar(self):
        return self.peso + 0.5

    def emagrecer(self):
        return self.peso - 0.5

    def crescer(self):
        if self.idade > 21:
            self.altura += 0.05
        return self.altura

    def __str__(self):
        return (f"O nome dele(a): é {self.nome} \n"
                f"ele(a) tem: {self.idade} anos \n"
                f"pesando: {self.peso}kg \n"
                f"e medindo: {self.altura:.2f} metros de altura \n")


Pessoa1 = Pessoa("Leandro",
                 23,
                 91.0,
                 1.75)

Pessoa2 = Pessoa("Adele",
                 36,
                 60.4,
                 1.76)

print(Pessoa1.crescer(), Pessoa1.__str__())
