import re
import names
import random
def crearMatriz(numParticipantes):
    matrizPequena=[]
    matriz=[]
    if numParticipantes>25:
        while numParticipantes!=0:
            while len(matrizPequena)!=5 and numParticipantes!=0:
                if numParticipantes>=5:
                    matrizPequena+=[5*[[]]]
                    numParticipantes-=5
                else:
                    matrizPequena+=[numParticipantes*[[]]]
                    numParticipantes-= numParticipantes
            matriz+=[matrizPequena]
            matrizPequena=[]
    else:
        while numParticipantes!=0:
            if numParticipantes>=5:
                matrizPequena+=[5*[[]]]
                numParticipantes-=5
            else:
                matrizPequena+=[numParticipantes*[[]]]
                numParticipantes-= numParticipantes
        matriz+=[matrizPequena]
    return matriz
        
def validarNumParticipantes(numParticipantes):
    if re.match("^\d{1,}$",numParticipantes) and numParticipantes!='0':
        return True
    return False
def llenarMatriz(matriz):
    audio = [True, False]
    presencia = [1, 2, 3]
    reacciones = ["sn", "ap", "lv"]
    for pantalla in matriz:
        for fila in pantalla:
            cont = 0
            for participante in fila:
                nombre = [[names.get_first_name(), names.get_last_name(), names.get_last_name()], random.choice(audio),
                          random.choice(presencia), random.choice(reacciones)]
                fila[cont] = nombre
                cont+=1
    return matriz
def reactivarAudio(matrizConCar):
    nombre=input("Ingrese el nombre de la persona: ")
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                print(fila[0][0].upper())
                if fila[0][0].upper()==nombre.upper():
                    if fila[1]==True:
                        print("No se puede activar el audio porque ya està activo.")
                        return matrizConCar
                    elif fila[1]==False:
                        fila[1]=True
                        print("El usuario se encuentra en la pantalla:",varPantalla,"En la columna:",varColumna,"y en la fila:",varFila,".")
                        print("Su audio està siendo activado...")
                        return matrizConCar
    print("No se encontrò la persona que buscaba, volviendo al menu...")
    return ""
def renombrar(matrizConCar):
    nombre=input("Ingrese el nombre de la persona: ")
    apellido1=input("Dijite su primer apellido: ")
    apellido2=input("Dijite su segundo apellido: ")
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                cont+=1
                if fila[0][0].upper()==nombre.upper() and fila[0][1].upper()==apellido1.upper() and fila[0][0].upper()==nombre.upper() and fila[0][2].upper()==apellido2.upper():
                    print("Se ha encontrado el usuario...")
                    nuevoNombre=input("Dijite el nuevo nombre: ")
                    fila[0]=[nuevoNombre,apellido1,apellido2]
                    print("¡Nombre cambiado satisfactoriamente!")
                    print("El usuario se encuentra en la pantalla:",varPantalla,"En la columna:",varColumna,"y en la fila:",varFila,".")
                    return matrizConCar
    print("No se encontrò la persona que buscaba, volviendo al menu...")
    return matrizConCar
def mostrarTotalParticipante(matrizConCar):
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                print("pantalla nº: ",varPantalla)
                print("Fila Nº: ", varFila)
                print("Columna Nº: ",varColumna)
                print("Nombre: ",fila[0][0],fila[0][1],fila[0][2])
                print("-----------------------------------------")
    return ""

def buscarUnParticipante(matrizConCar):
    entrada=input("Enviar a: ")
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                if participanteContiene(fila[0],entrada):
                    print("pantalla nº: ",varPantalla)
                    print("Fila Nº: ", varFila)
                    print("Columna Nº: ",varColumna)
                    print("Nombre: ",fila[0][0],fila[0][1],fila[0][2])
                    print("-----------------------------------------")
    return ""
def participanteContiene(nombreCompleto,entrada):
    for elemento in nombreCompleto:
        if entrada.upper() in elemento.upper():
            return True
    else:
        return False