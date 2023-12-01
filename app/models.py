class Usuario():
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Cuenta():

    def __init__(self, user: Usuario, saldo, contactos: list):
        self.user = user
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones: list[Operacion] = []

    def historial(self):
        return {
            "saldo": f"Saldo de {self.user.nombre}: {self.saldo}",
            "owner": self.user.nombre,
            "operaciones": [x.getOperacion() for x in self.operaciones]
        }

    def exist_telefono(self, numerodestino, contacto):
        return numerodestino == contacto.user.telefono
    
    def find_contactocuenta_telefono(self, telefono):
        for cont in self.contactos:
            if cont.user.telefono == telefono:
                return True
        return False
    
    def get_contactocuenta_telefono(self, telefono):
        for cont in self.contactos:
            if cont.user.telefono == telefono:
                return cont
        return None

    def pagar(self, numerodestino, valor):
        for i in range(len(self.contactos)):
            if self.exist_telefono(numerodestino, self.contactos[i]) and self.saldo - valor > 0:
                self.saldo -= valor
                self.contactos[i].saldo += valor
                self.operaciones.append(Operacion(
                    self.get_contactocuenta_telefono(numerodestino), 
                    "11/07/2023",
                    valor)
                )

                return "Realizado en 17/03/2023"
        return "El destinatario no existe"

class Operacion():
    def __init__(self, destinatario: Cuenta, fecha, valor):
        self.destinatario = destinatario
        self.fecha = fecha
        self.valor = valor

    def getOperacion(self):
        return f"Pago recibido de {self.valor} de {self.destinatario.user.nombre}"