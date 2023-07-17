import core
import os
diccCliente = {"data":[]}

def LoadInfoCliente():
    global diccCliente
    if (core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    else:
        core.crearInfo("clientes.json",diccCliente)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        pass
    if (opcion == 2):
        pass
    if (opcion == 3):
        pass
    if (opcion == 4):
        pass
    if (opcion == 5):
        isCliRun=False
    if(isCliRun):
        MainMenu()
