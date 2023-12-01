from app import app, BD
from flask import request

@app.get('/billerera/contactos')
def contactos():
    numero = request.args.minumero

    for cuenta in BD:
        if cuenta.user.telefono == numero:
            contactos = cuenta.contactos
            message = '<br>'.join(f'{x.user.telefono}: {x.user.nombre}' for x in contactos)
            return f"<div> {message}</div>"
        
    return "El usuario no existe"


@app.get('/billetera/pagar')
def pagar():

    numero = request.args.minumero
    destino = request.args.numerodestino
    valor = request.args.valor

    for i in range(len(BD)):
        if BD[i].user.telefono == numero:
            return BD[i].pagar(destino, valor)
                   
    return "El usuario no existe"


@app.get("/billetera/historial")
def historial():

    numero = request.args.minumero

    for cuenta in BD:
        if cuenta.user.telefono == numero:
            infohistorial = cuenta.historial()
            operaciones = "<br>".join(infohistorial['operaciones'])
            message = f"{infohistorial['saldo']} <br> {infohistorial['owner']} <br> {operaciones}"
            return f"<div> {message}</div>"
        
    return "El usuario no existe"
