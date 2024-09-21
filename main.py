####################################################################################################


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
from sys import int_info


class Caminhao:
    def __init__(self, modelo, placa, capacidade_carga):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.motorista = None

    def carregar_peso(self):
       if self.capacidade_carga == 1000:
        print("O caminhão está cheio!")
       else:
        print("O caminhão está com a quantidade de carga dentro do limite,poderá prosseguir!")

    def descarregar_peso(self):
      if self.capacidade_carga == 500:
       print("Você chegou no destino,pode descarregar a carga!")

    def associar_caminhoneiro(self, nome):
        self.motorista = nome

    def mostrar_informacoes(self):
        info = (f"\nModelo: {self.modelo}"
                f"\nPlaca: {self.placa}")
        if self.motorista:
            info += f", \nProprietário: {self.motorista.nome}"
            info += f' \nIdade: {self.motorista.idade}'
            info += f'\nSituação do CNH: {self.motorista.verificar_cnh()}'
        print(info)



class Motorista:
    def __init__(self, nome, idade, CNH, data_validade):
        self.nome = nome
        self.idade = idade
        self.CNH = CNH
        self.data_validade = data_validade

    def dirigir_caminhao(self):
        info = f'{self.nome} está dirigindo o caminhão'   
        print(info)
        
    def frear_caminhao(self):
        info = f'{self.nome} está freando o caminhão!'
        print(info)

    def verificar_cnh(motorista):
     from datetime import datetime, timedelta
     data_validade = '2030-09-21'
     format = ("%Y-%m-%d")
     data_validade_dt = datetime.strptime(data_validade, format)

     hoje = datetime.now()

     if data_validade_dt < hoje:
            status = "vencida"
     elif data_validade_dt <= hoje + timedelta(days=30):
            status = "para vencer"
     else:
            status = "válida"

     if motorista  and (status == "vencida" or status == "para vencer"):
            return f"A CNH está {status}. É necessário renovar a CNH."
     else:
            return f"A carteira está válida e em dia!!"







caminhao1=Caminhao('Volvo FH', 'IHQ-1516', 500)
caminhao2=Caminhao('Volvo FMX', 'IQJ-7293', 1000)
caminhoneiro1=Motorista('Nickolas Leal Martins', 20, '42593965660', '20/09/2022')
caminhoneiro2=Motorista('James Duarte', 50, '95091643468', '20/09/2030')
caminhao1.associar_caminhoneiro(caminhoneiro1)
caminhao1.mostrar_informacoes()
caminhao1.motorista.estado_caminhao()
caminhao2.associar_caminhoneiro(caminhoneiro2)
caminhao2.mostrar_informacoes()
caminhao2.motorista.estado_caminhao()
