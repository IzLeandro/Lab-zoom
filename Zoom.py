#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 5/11/2020 :XXpm 
#Fecha de última Modificación: 6/11/2020 9:37pm
#Versión: 3.8.5
#Importacion de librerias 
import re
import time
from Funciones import validarNumParticipantes,crearMatriz,llenarMatriz,reactivarAudio,renombrar,mostrarTotalParticipante,mostrarParticipantesConVideo,buscarUnParticipante
#Funciones
def numParticipantes():
    """
    Funcionamiento: Guarda la cantidad de participantes que digita el usuario
    Entradas: participantes
    Salidas: cantidad de participantes o un mensaje de error
    """
    numParti=input('Digite la cantidad de participantes: ')
    while not validarNumParticipantes((numParti)):
        print('Digite solamente números del 1 en adelante')
        numParti=input('Digite la cantidad de participantes: ')
    numParti=int(numParti)
    if numParti>100:
        return 'No pueden ser mas de 100 participantes'
    return numParti
def menu1():
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Booleano que indica si el año es bisiesto o no
    """
    participantes=numParticipantes()       
    if type(participantes)==int:
        if participantes==1:
            print('a) Hay',participantes,'participante')
        else:
            print('a) Hay',participantes,'participantes')
    else:
        print(participantes)
        menu1()
        return''
    matriz=crearMatriz(participantes)
   
    matriz=llenarMatriz(matriz)
    filas=0
    for i in matriz:
        filas+=len(i)
    if filas==1:
        print('b) Hay',filas,'fila')
    else:
         print('b) Hay',filas,'filas')
    if len(matriz)==1:
        print('c) Hay',len(matriz),'pantalla')
        print()
    else:
         print('c) Hay',len(matriz),'pantallas')
         print()
    print(matriz)
    return matriz
matriz=menu1()
def menu():
    print()
    print('-----ZOOM-----')
    print()
    global matriz
    print('1. Reactivar mi audio')
    print('2. Renombrar')
    print('3. Mostrar totalidad de participantes')
    print('4. Mostrar participantes que tienen video')
    print('5. Buscar un participante en el chat')
    print('6. Salir de zoom')
    opcion=input('Digite una opción: ')
    if opcion=='1':
        reactivarAudio(matriz)
        input("Presione enter para continuar...")
    elif opcion=='2':
        renombrar(matriz)
        input("Presione enter para continuar...")
    elif opcion=='3':
        mostrarTotalParticipante(matriz)
        input("Presione enter para continuar...")
    elif opcion=='4':
        mostrarParticipantesConVideo(matriz)
        input("Presione enter para continuar...")
    elif opcion=='5':
        buscarUnParticipante(matriz)
        input("Presione enter para continuar...")
    elif opcion=='6':
        print('El anfitrión ha eliminado su participación de esta reunión. Saliendo en')
        print('5')
        time.sleep(5)
        print('4')
        time.sleep(5)
        print('3')
        time.sleep(5)
        print('2')
        time.sleep(5)
        print('1')
        time.sleep(5)
        return ""
    else:
        print('Digite una opción válida')
        input("Presione enter para continuar...")
        menu()
        return ''
    menu()
menu()
