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


#####################################################################################################


MOSTRAR TRABALHO SOR:
class Televisao:
    def __init__(self, marca, modeloTV):
     self.marca = marca
     self.modeloTV = modeloTV
     self.canal = None
     self.estado = 'Desligada'  # Estado inicial da tv está desligada
     self.volume = 0

    def ligar(self):
     self.estado = 'Ligada'
     print(f"A {self.marca} {self.modeloTV} está ligada")

    def desligar(self):
     self.estado = 'Desligada'
     print(f"A {self.marca} {self.modeloTV} está desligada")


    def aumentar_volume(self):
     if self.estado == 'Desligada':
      print("Você não pode aumentar o volume da tv porque ela está desligada")
     else:
      self.volume += 1
      print("Você aumentou +1 o volume da tv")


    def diminuir_volume(self):
     if self.estado == 'Desligada':
      print("Você não pode diminuir o volume da tv porque ela está desligada")
     else:
      self.volume -= 1
      print("Você diminuiu -1 o volume da tv")

    def definir_canal(self, canais):
        self.canal = canais

    def mostrar_informacoes(self):
         info = f'Marca: {self.marca}, Modelo: {self.modeloTV}, Canal Atual: {self.canal.canal}'

         print(info)



class Canais:
    def __init__(self, canalatual):
        self.canal = canalatual


tv1=Televisao('TCL', 'Smart TV 43 Full HD LED')
canais1=Canais('RBS TV')
canais2=Canais('Cazé TV')
canais3=Canais('Sportv')
canais4=Canais('Premiere')

tv1.definir_canal(canais1)
tv1.mostrar_informacoes()
tv1.definir_canal(canais4)
tv1.mostrar_informacoes()


#####################################################################################################
Trabalho para fazer
from datetime import datetime,timedelta


class Caminhao:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = 0
        self.motorista = None



    def carregar_peso(self):
       if self.capacidade_carga == 600:
        print("O caminhão está cheio!")
       else:
        print("O caminhão está com a quantidade de carga dentro do limite,poderá prosseguir!")


    def descarregar_peso(self):
      if self.capacidade_carga == 500:
       print("Você chegou no destino,pode descarregar a carga!")

    def associar_caminhoneiro(self, nome):
        self.motorista = nome

    def mostrar_informacoes(self):
      info = f'Marca: {self.modelo}, Placa: {self.placa}, Carga atual: {self.capacidade_carga}'



class Motorista:
    def __init__(self, nome, idade, CNH, data_validade):
        self.nome = nome
        self.idade = idade
        self.CNH = CNH
        self.data_validade = data_validade

    def dirigir_caminhao(self):
      self.estado_caminhao = 'Dirigindo'
      print(f"O motorista {self.nome} está dirigindo o caminhão!")


#def validar_cnh(data_emissao: str) -> bool:
     # try:
      #  data_emissao = datetime.strptime(data_emissao, '%d/%m/%Y')
      #except ValueError:
      #  return False
      #data_validade = data_emissao + timedelta(days=5 * 365)
     # return datetime.now() <= data_validade

#data_emissao = "20/09/2024"

#if validar_cnh(data_emissao):
 #print("A CNH é válido")
#else:
 #print("A CNH está vencida")

caminhao1 = Caminhao('Volvo', 'Fx')
caminhao1.mostrar_informacoes()
