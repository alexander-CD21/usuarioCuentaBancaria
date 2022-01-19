class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    cuenta=[]
    def __init__(self, tasaInteres=0.01, balance=0): 
        self.tasaInteres = tasaInteres
        self.balance = balance
        CuentaBancaria.cuenta.append(self)
# tu código aquí (recuerda, los atributos de instancia van aquí)
    # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def deposito(self, amount):
        self.balance+=amount
        return self
    def retiro(self, amount):
        self.balance-=amount
        return self
    def mostrarInfoCuenta(self):
        print(f"Tasa de interes: {self.tasaInteres}")
        print(f"Balance: {self.balance}")
        return self
    def generarInteres(self):
        self.balance=self.balance +(self.tasaInteres*self.balance)
        return self
    @classmethod
    def imprimirAll(cls):
        for x in cls.cuenta:
            x.mostrarInfoCuenta()
