class CuentaBancaria:
    def __init___(self):
        self.numero_cuenta=0
        self.propietarios=""
        self.balance=0
    def depositar(self):
        plata=0
        deposito=plata+self.balance
    def retirar(self):
        plata=0
        retiro=self.balance-plata
    def  aplicar_cuota_manejo(self):
        cuotamanejo=self.balance*0.02
    def  mostrar_detalles(self):
      print("Numero de cuenta: ",self.numero_cuenta)
      print("Propietario: ",self.propietarios)
      print("Balance: ",self.balance)
      