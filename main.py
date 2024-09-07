class AnimalEstimacao:
    def __init__(self, nome, especie, idade):
     self.nome = nome
     self.especie = especie
     self.idade = idade
     self.estado = 'Dormindo'

    def comer(self):
     self.estado = 'Comendo'
     print(f"O {self.nome} está comendo!")

    def dormir(self):
     self.estado = 'Dormindo'
     print(f"O {self.nome} continua dormindo!")

    def brincar(self):
     self.estado = 'Brincando'
     print(f"O {self.nome} está brincando!")

    def listar(self):
     return (f"Nome: {self.nome}, Espécie: {self.especie}, Idade: {self.idade}, Estado: {self.estado}")

    def latir(self):
      if self.especie.lower == 'cachorro':
       self.estado = 'Latindo'
       print(f"O {self.especie} chamado {self.nome} está latindo!")
      else:
        print("Ops!,você digitou errado,gatos não latem!")

    def miar(self):
      if self.especie.lower == 'gato':
       self.estado = 'Miando'
       print(f"O {self.especie} chamado {self.nome} está miando!")
      else:
          print("Ops!,você digitou errado,cachorros não miam!")

    def nadar(self):
      if self.especie.lower == 'peixe':
       self.estado = 'Nadando'
       print(f"O {self.especie} chamado {self.nome} está nadando!")
      else:
          print("Ops!,você digitou errado,cachorros e gatos não respiram embaixo d´água!")



animal1 = AnimalEstimacao('Duque', 'cachorro', 5)
animal2 = AnimalEstimacao('Théo', 'gato', 3)
animal3 = AnimalEstimacao('Garry', 'peixe', 2)

print(animal1.listar())
print(animal2.listar())
print(animal3.listar())





