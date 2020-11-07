import re
import names
import random
def crearMatriz(numParticipantes):
    """Funcion: Crea la matriz en base a la cantidad de participantes que le ingrese el usuario.
    Entradas: Tamaño de la matriz (Cantidad de participantes).
    Salidas: matriz lista para obtener datos."""
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
    """Funcion: Valida que la cantidad de participantes sea un número.
    Entradas: Tamaño de la matriz (Cantidad de participantes).
    Salidas: Booleano."""
    if re.match("^\d{1,}$",numParticipantes) and numParticipantes!='0':
        return True
    return False
def llenarMatriz(matriz):
    """Funcion: llena la matriz creada anteriormente con nombre, apellidos, datos de audio, estado de video y reacciones.
    Entradas: Matriz lista para obtener datos.
    Salidas: Matriz llena con los datos."""
    audio = [True, False]
    presencia = [1, 2, 3]
    reacciones = ["sn", "ap", "lv"]
    for pantalla in matriz:
        for fila in pantalla:
            for i in range(len(fila)):
                nombre = [[names.get_first_name(), names.get_last_name(), names.get_last_name()], random.choice(audio),
                          random.choice(presencia), random.choice(reacciones)]
                fila[i] = nombre
    return matriz
def reactivarAudio(matrizConCar):
    """Funcion: Recorre la matriz buscando el nombre de una persona con la intención de convertir su audio en True.
    Entradas: Matriz llena con los datos.
    Salidas: Matriz llena con los datos más el cambio."""
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
                if fila[0][0].upper()==nombre.upper():
                    print(fila[0][0].upper())
                    if fila[1]==True:
                        print("No se puede activar el audio porque ya está activo.")
                        return matrizConCar
                    elif fila[1]==False:
                        fila[1]=True
                        print("El usuario se encuentra en la pantalla:",varPantalla,"En la columna:",varColumna,"y en la fila:",varFila,".")
                        print("Su audio está siendo activado...")
                        return matrizConCar
    print("No se encontrò la persona que buscaba, volviendo al menu...")
    return matrizConCar
def renombrar(matrizConCar):
    """Funcion: Recorre la lista buscando un participante y le pide un nuevo nombre.
    Entradas: Matriz llena con los datos.
    Salidas: Si encuentra a la persona, la matriz llena de datos más el cambio realizado."""
    nombre=input("Ingrese el nombre de la persona: ")
    apellido1=input("Dijite su primer apellido: ")
    apellido2=input("Dijite su segundo apellido: ")
    varPantalla=0
    cont=0
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
    """Funcion: Recorre la lista e imprime cada participante con su información.
    Entradas: Matriz llena con los datos.
    Salidas: """
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                print("Pantalla nº: ",varPantalla)
                print("Fila Nº: ", varFila)
                print("Columna Nº: ",varColumna)
                print("Nombre: ",fila[0][0],fila[0][1],fila[0][2])
                print("-----------------------------------------")
    return ""
def mostrarParticipantesConVideo(matrizConCar):
    """Funcion: Recorre la lista e imprime cada participante y con su información, si tienen el video habilitado.
    Entradas: Matriz llena con los datos.
    Salidas: """
    varPantalla=0
    for pantalla in matrizConCar:
        varPantalla+=1
        varColumna=0
        for columna in pantalla:
            varColumna+=1
            varFila=0
            for fila in columna:
                varFila+=1
                if fila[2]==3:
                    print("pantalla nº: ",varPantalla)
                    print("Fila Nº: ", varFila)
                    print("Columna Nº: ",varColumna)
                    print("Nombre: ",fila[0][0],fila[0][1],fila[0][2])
                    print("-----------------------------------------")
    return ""
def buscarUnParticipante(matrizConCar):
    """Funcion: Recorre la lista e imprime cada participante que coincida con la entrada.
    Entradas: Matriz llena con los datos.
    Salidas: """
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
                    print("Pantalla nº: ",varPantalla)
                    print("Fila Nº: ", varFila)
                    print("Columna Nº: ",varColumna)
                    print("Nombre: ",fila[0][0],fila[0][1],fila[0][2])
                    print("-----------------------------------------")
    return ""
def participanteContiene(nombreCompleto,entrada):
    """Funcion: Comprueba si dentro de nombrecompleto existe alguna coincidencia con entrada.
    Entradas: Matriz con un nombre y 2 apellidos, entrada tipo str
    Salidas: Booleando indicando si existe o no coincidencia"""
    for elemento in nombreCompleto:
        if entrada.upper() in elemento.upper():
            return True
    else:
        return False