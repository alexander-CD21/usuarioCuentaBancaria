from usuario import Usuario


Alexander=Usuario("alexander","alexander@dojo.com",3)
Aracelly=Usuario("aracelly","aracelly@dojo.com",4)

Alexander.hacerDeposito(5000).hacerDeposito(3000,1).mostrarBalanceUsuario()
Aracelly.hacerDeposito(2000).hacerDeposito(3000,2).mostrarBalanceUsuario()
Alexander.transferirDinero(1000,Aracelly,1,2)