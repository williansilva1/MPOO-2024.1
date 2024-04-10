"1ª atividade referente a disciplina de MPOO-2024.1"
"Discente: Robson Willian da silva"

class Controle:
    def __init__(self):
        self.ligado = False
        self.volume = 0
        self.canal = 5
        
    def ligar(self):
        self.ligado = True
        print("Ligando o dispositivo")
    def desligar(self):
        self.ligado = False
        print("Desligando dispositivo")
    
    def aumentarVolume(self):
        if self.volume < 20:
            self.volume += 1
            print("Volume aumentado para -> ", self.volume)
        else:
            print("Volume máximo")
    
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuido para -> ", self.volume)
        else:
            print("Volume mínimo")

    
    def mudarCanal(self,numero):
        if self.ligado == True:
            if numero > 0 and numero <= 20:
                self.canal = numero
                print("Canal: ", self.canal)
            else:
                print("Canal inválido")
        else:
            print("Dispositivo desligado")
            
            


controleRemoto = Controle()
controleRemoto.ligar()
controleRemoto.aumentarVolume()
controleRemoto.diminuirVolume()
controleRemoto.mudarCanal(20)
controleRemoto.desligar()