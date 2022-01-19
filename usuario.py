from Bank import CuentaBancaria
class Usuario:

    def __init__(self,nombre,email,numCuentas=1):
        self.nombre=nombre
        self.email=email
        self.cuenta=[]
        for i in range(numCuentas):
            self.cuenta.append(CuentaBancaria(0.01,0))

    def hacerDeposito(self,amount,num=0):
        self.cuenta[num].deposito(amount)
        #self.balance=self.balance+amount
        return self
    def hacerRetiro(self,amount,num=0):
        self.cuenta[num].retiro(amount)
        #self.balance=self.balance - amount
        return self
    def mostrarBalanceUsuario(self):
        print("********************")
        print(f"Usuario: {self.nombre}")
        print(f"Email: {self.email}")
        for i in range(len(self.cuenta)):
            self.cuenta[i].mostrarInfoCuenta()
        return self
    def transferirDinero(self,amount1,user,numCuentaUser1=0,numCuentaUser2=0):
        self.cuenta[numCuentaUser1].retiro(amount1)
        user.cuenta[numCuentaUser2].deposito(amount1)
        self.mostrarBalanceUsuario()
        user.mostrarBalanceUsuario()
        return self
