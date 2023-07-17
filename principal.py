import os

if __name__=="__main__":
    os.system('cls')
    isAddCitas=True
    while(isAddCitas):
        print('+','-'*55,'+')
        print("|{:^10}{}{:^10}|".format('','ADMINISTRADOR DE CITAS',''))
        print('+','-'*55,'+')
        print("1.Agregar cita")
        print("2.Agregar cita")
        print("3.Agregar cita")
        print("4.Agregar cita")
        print("5.Agregar cita")
        opcion=int(input("Ingresa opción: "))
        if(opcion==1):
            pass
        if(opcion==2):
            pass
        if(opcion==3):
            pass
        if(opcion==4):
            pass
        if(opcion==5):
            pass
        if(opcion==6):
            isAddCitas=False
        else:
            print("Opción no validad.. Por favor ingresa nuevamente")
            os.system('pause')
