import re
from Funciones import *

def numParticipantes():
    numParti=input('Digite la cantidad de participantes: ')
    while not validarNumParticipantes((numParti)):
        print('Digite solamente números del 1 en adelante')
        numParti=input('Digite la cantidad de participantes: ')
    numParti=int(numParti)
    if numParti>100:
        return 'No pueden ser mas de 100 participantes'
    return numParti
def menu1():
    participantes=numParticipantes()       
    if type(participantes)==int:
        if participantes==1:
            print('Hay',participantes,'participante')
        else:
            print('Hay',participantes,'participantes')
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
        print('Hay',filas,'fila')
    else:
         print('Hay',filas,'filas')
    if len(matriz)==1:
        print('Hay',len(matriz),'pantalla')
        print()
    else:
         print('Hay',len(matriz),'pantallas')
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
    print('6. Salida')
    print('7. Salir de zoom')
    opcion=input('Digite una opción: ')
    if opcion=='1':
        reactivarAudio(matriz)
        menu()
    if opcion=='2':
        renombrar(matriz)
        menu()
    if opcion=='3':
        totalidadParticipantes(matriz)
        menu()
    if opcion=='4':
        participanteVideo(matriz)
        menu()
    if opcion=='5':
        participanteChat(matriz)
        menu()
    if opcion=='6':
        salida(matriz)
        menu()
    if opcion=='7':
        print('El anfitrión ha eliminado su participación de esta reunión. Saliendo en')
        return ''
    else:
        print('Digite una opción válida')
        menu()
menu()
