import json

#Diccionario con los espacios libres
disponibles = { "Piso1":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso2":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso3":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso4":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso5":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso6":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] }
#Matriz para usuarios ingresados
ingresados = []
#Conversion de tipo de vehiculo a valor numerico
def validarVehiculo(vehiculo):
    posibles = ["automovil" , "automovil electrico" , "motocicleta" , "discapacitado" , "autom??vil el??ctrico", "autom??vil"]
    while vehiculo.lower() not in posibles:
        print("\n    > El tipo de veh??culo ingresado no es v??lido. \n")
        vehiculo = input("   Ingrese el tipo de vehiculo: ")
    if vehiculo.lower() == "autom??vil" or vehiculo.lower() =="automovil":
        return 1
    elif vehiculo.lower() == "autom??vil el??ctrico" or vehiculo.lower() =="automovil electrico":
        return 2
    elif vehiculo.lower() == "motocicleta":
        return 3
    elif vehiculo.lower() == "discapacitado":
        return 4

#Verifica que el usuario no tenga mas de un vehiculo registrado
def registrar(dic, nombre, numero):
    encontro = False
    #Ciclo que recorre las listas de el usuarios.json
    for x in range(len(dic["usuarios"])):
        #Valida si el numero se encuentra dentro de la lista del indice x
        if numero in dic["usuarios"][x]:
            encontro = True
    if encontro:    
        print("\n    > NO SE PUEDE REGISTRAR M??S DE UN VEH??CULO POR USUARIO \n")

        return dic

    #Sube el registro al .json
    elif not encontro:
        datos = []
        datos.append(nombre)
        datos.append(numero)
        datos.append(str(input("   Ingrese qu?? tipo de usuario es (Estudiante, Profesor, Personal Administrativo): ")) )
        datos.append(str(input("   La placa del veh??culo: ")) )
        datos.append(str(input("   Ingrese el tipo de veh??culo que va a registrar (Automovil, Automovil Electrico, Motocicleta, Discapacitado): ")) )
        datos.append(str(input("   Ingrese el plan de pago que desea (Diario o Mensualidad): ")) )
        #Operacion que agrega la lista datos a la matriz dentro del diccionario bajo la llave de "usuarios".
        dic["usuarios"].append(datos)
        print ("\n     > SE HA REGISTRADO SU VEH??CULO EXITOSAMENTE \n")
        return dic

"""Funcion que valida el ingreso de los usuarios y agrega su informaci??n a la matriz ingresados. Toma como parametros el diccionario de usuarios ("resgistrados"),
el diccionario de pisos, donde se encuentran la cantidad de tipos de parqueaderos disponibles para cada tipo de vehiculo en cada
piso, y la placa del vehiculo que va a ingresar (str)  y retorna un valor booleano que representa si hay parqeuaderos.
"""

def ValidaParqueaderosDispo ( dic , placa , registrados):
    global ingresados

    for x in range(len(ingresados)):
        if placa.lower() == ingresados[x][3].lower():
            print("\n     >SU VEH??CULO YA HA SIDO INGRESADO. \n")
            return False

    encontro = False
    #Ciclo que reccorre la cantidad de listas que hay dentro de la llave usuarios en el diccionario usuarios 
    for x in range(len(registrados["usuarios"])):
        #Condicional que valida si placa esta en la lista x del diccionario registrados dentro de la llave usuarios
        if placa.lower() == registrados["usuarios"][x][3].lower():
            encontro=True
            break

    if encontro:
        tipovehiculo = validarVehiculo(registrados["usuarios"][x][4])

    elif not encontro:
        #se piden los datos del nuevo ingreso 
        datos = []
        datos.append("NombreVisitante")
        datos.append(eval(input("   Digite su numero de identificacion: ")))
        datos.append("Visitante")
        datos.append(placa)
        datos.append(str(input("   Ingrese el tipo de veh??culo va a registrar (Automovil, Automovil Electrico, Motocicleta, Discapacitado): ")) )
        datos.append("Diario")
        tipovehiculo = validarVehiculo(datos[4])
    n = 0
    espacio = False
    #Ciclo que llama a la funcion sumaParqueaderosDisponibles para mostrar los parqueaderos disponibles por piso
    for numeroPiso in(dic_pisos.keys()):
        n += 1
        numeroparqueaderos = SumaParqueaderosDisponibles(dic,  numeroPiso , tipovehiculo)
        print("   Parqueaderos disponibles en el piso ",n,"son: ", numeroparqueaderos)
        #Validacion de si hay parqueaderos disponibles
        if numeroparqueaderos > 0:
            espacio = True
    if not espacio:
        print("\n     > NO HAY PARQUEADEROS DISPONIBLES. \n")
        return espacio
     #Condicionales que agregan la informaci??n del nuevo ingreso a la matriz ingresados
    elif encontro:
        ingresados.append(registrados["usuarios"][x])
    elif not encontro:
        ingresados.append(datos)
    return espacio

#Funcion para la suma de cantidad de parqueaderos disponibles segun su tipo de veiculo
def SumaParqueaderosDisponibles (dic_tipo, piso , tipovehiculo):
    global disponibles
    suma=0
    #ciclos for que recorren la matriz dentro del diccionario de parqueaderos
    for x in range(len(dic_tipo[piso])):        
        for y in range (len(dic_tipo[piso][x])):
            #conidcionales que validan si hay parqueaderos disponibles para el tipo de veh??culo especificado en los par??metros
            if disponibles[piso][x][y] == "O":
                if tipovehiculo == 1:
                    if tipovehiculo == dic_tipo[piso][x][y]:
                        suma += 1
                elif tipovehiculo == 2:
                    if 2 == dic_tipo[piso][x][y] or 1 == dic_tipo[piso][x][y]:
                        suma += 1
                elif tipovehiculo == 3:
                    if tipovehiculo == dic_tipo[piso][x][y]:
                        suma += 1
                elif tipovehiculo == 4:
                    if 1 == dic_tipo[piso][x][y] or 4 == dic_tipo[piso][x][y]:
                        suma += 1
    return suma 

#Crear funcion para neuva matriz grafica donde nos deja ver los parqueaderos libres y ocupados 
def matrizTipos(disponibles, tipo, piso):
    global dic_pisos
    nueva = { "Piso1":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso2":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso3":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso4":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso5":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] , "Piso6":[  ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]  ] }
    #Recorrer el diccionario tipo de veh??culo
    for x in range(len(dic_pisos[piso])):
        #ciclo que recorre la matriz del diccionario en la llave x
        for y in range(len(dic_pisos[piso][x])):
            if disponibles[piso][x][y] == "O":
                #condicionales que valida el tipo de veh??uclo
                if tipo == 1:
                    #Validacion entre el tipo de veh??culo y su posici??n respectiva en el diccionario sean diferentes
                    if tipo != dic_pisos[piso][x][y]:
                        #Operaci??n que agrega una X en la posici??n donde el tipo de veh??culo no es compatibel con el parqeuadero
                        nueva[piso][x].insert(y, "X")
                        del nueva[piso][x][y+1]
                elif tipo == 2:
                    if 2 != dic_pisos[piso][x][y] and 1 != dic_pisos[piso][x][y]:
                        nueva[piso][x].insert(y, "X")
                        del nueva[piso][x][y+1]
                elif tipo == 3:
                    if tipo != dic_pisos[piso][x][y]:
                        nueva[piso][x].insert(y, "X")
                        del nueva[piso][x][y+1]
                elif tipo == 4:
                    if 1 != dic_pisos[piso][x][y] and 4 != dic_pisos[piso][x][y]:
                        nueva[piso][x].insert(y, "X")
                        del nueva[piso][x][y+1]
            elif disponibles[piso][x][y] == "X":
                nueva[piso][x].insert(y, "X")
                del nueva[piso][x][y+1]
    return nueva[piso]

#Menu visible donde muestra parqueaderos disponibles usando como parametro el diccionario de los usuarios, su placa y el
#diccionario de sitios disponibles
def interfaz(dicUsuarios, placa, disponibles):
    global ingresados
    piso = int(input("   Ingrese el piso en el que desea parquear: "))
    #conversion del piso en un (int)
    if piso == 1:
        piso = "Piso1"
    elif piso == 2:
        piso = "Piso2"
    elif piso == 3:
        piso = "Piso3"
    elif piso == 4:
        piso = "Piso4"
    elif piso == 5:
        piso = "Piso5"
    elif piso == 6:
        piso = "Piso6"

    #Ciclo que ubica la lista que contiene la placa especificada en los par??metros y define el tipo de veh??culo a partir d
    #de dicha lista
    for x in range(len(ingresados)):
        if placa.lower() == ingresados[x][3].lower(): #Busca la placa en el diccionario de usuarios
            tipo = validarVehiculo(ingresados[x][4])  #empareja la placa con el tipo de vehiculo que tiene
    #retorna matrizTipos en una variable para ser impresa y utilizada como interfaz gr??fica        
    matrizDisponibles = matrizTipos(disponibles, tipo, piso)
    print("             ",piso)
    c = "      1    2    3    4    5    6    7    8    9    10" 
    print(c)
    n = 0
    for y in matrizDisponibles:
        n += 1
        if n == 10:
            print(n, "",y)
        else:
            print(n," ",y)
    print("")
    viable = True
    
    #Validacion de disponibilidad de las coordenadas dadas por el usuario
    while viable:
        fila = eval(input("   Ingrese la fila (horizontal) deseada: "))
        columna = eval(input("   Ingrese la columna (vertical) deseada: "))
        #Condicional para mantener a raya las limitaciones del parqueadero
        if ((columna > 10) or (columna < 0) or (fila > 10) or (fila < 0)) and piso != "Piso6":
            print("    El n??mero de fila o columna no es valido")
        elif ((columna > 10) or (columna < 0) or (fila > 5) or (fila < 0)) and piso == "Piso6":
            print("    El n??mero de fila o columna no es valido")

        #Verificacion que la fila y columna no est?? ocupada
        elif disponibles[piso][fila-1][columna-1] == "X" or matrizDisponibles[fila-1][columna-1] == "X":
            print("      El espacio que seleccion?? se encuentra ocupado y/o no es v??lido para su tipo de veh??culo.")
            print("    Por favor seleccione otro espacio para estacionar")
        else:
            #operaci??n que a??ade una X en la posici??n especificada
            disponibles[piso][fila-1].insert(columna-1, "X")
            del disponibles[piso][fila-1][columna]
            for x in range(len(ingresados)):
                if placa.lower() == ingresados[x][3].lower():
                    ingresados[x].append(fila-1)
                    ingresados[x].append(columna-1)
                    ingresados[x].append(piso)
            print("\n          SE HA INGRESADO SU VEHICULO EXITOSAMENTE.\n")
            viable = False

#Funcion para sacar vehiculos solo con la lista de ingresados hasta el momento
def retirar(ingresados):
    global disponibles 
    placa = input("   Digite la placa del veh??culo que desea retirar: ")
    encontro = False
    while not encontro:
        #Valida si la placa esta dentro del parqueadero
        for x in range(len(ingresados)):
            if placa.lower() in ingresados[x][3].lower():
                #variable que permite terminar el ciclo
                encontro = True
                #Definici??n de variables que se usan luego
                tipoPago = ingresados[x][5]
                fila = ingresados[x][6]
                columna = ingresados[x][7]
                piso = ingresados[x][8]
                indice = x
        if encontro:
            #condicional que valida el tipo de pago
            if tipoPago.lower() == "mensualidad":      
                #Elimina la "X" de la posici??n ocupada y la deja abierta            
                disponibles[piso][fila].insert(columna, "O")
                del disponibles[piso][fila][columna+1]
                print("\n   DEBIDO A QUE SU TIPO DE PAGO ES MENSUAL, NO DEBE CANCELAR EN CAJA. \n")
                return indice
            elif tipoPago.lower() == "diario":
                numhoras = eval(input("   Ingrese el n??mero de horas que permaneci?? en el parqueadero: "))
                tipoUsuario = ingresados[indice][2]
                if numhoras>0 and numhoras<1:
                    numhoras = 1
                else:
                    entero = numhoras //1
                    decimal = numhoras % entero
                    if decimal != 0:
                        numhoras = entero + 1
                #Condicionales para ajusta el costo de la hora
                if tipoUsuario.lower() == "estudiante":
                    hora = 1000
                elif tipoUsuario.lower() == "profesor":
                    hora = 2000
                elif tipoUsuario.lower() == "personal administrativo":
                    hora = 1500
                elif tipoUsuario.lower() == "visitante":
                    hora = 3000
                cobro = numhoras * hora
                print("   Usted permaneci?? ",numhoras," horas en el parqueadero.")
                print("\n     El valor a pagar es ",cobro , "\n")
                #Elimina la "X" de la posici??n ocupada y la deja disponible
                disponibles[piso][fila].insert(columna, "O")
                del disponibles[piso][fila][columna+1]
                return indice
        elif not encontro:
            print("    >La placa ingresada no est?? registrada en el parqueadero.")
            placa = input("   Digite la placa del veh??culo que desea retirar: ")

#Funcion que indica cuantos hay de un mismo tipo de vehiculos dentro del parqueadero
def cantidadTipo(tipo , indice, ingresados):
    total = 0
    if tipo == "automovil" or tipo == "autom??vil":
        normal = "automovil"
        tilde = "autom??vil"
    elif tipo == "automovil electrico" or tipo == "autom??vil el??ctrico":
        normal = "automovil electrico"
        tilde = "autom??vil el??ctrico"
    else:
        tilde = tipo
        normal = tipo
    #ciclo que recorre la matriz ingresados y valida si cada usuario ingresado tiene el tipo de veh??culo especificado en los par??metros
    for x in range(len(ingresados)):
        if ingresados[x][indice].lower() == normal or ingresados[x][indice].lower() == tilde:
            total += 1
    return total

#Procedimiento que toma como par??metros el nombre del archivo y el n??mero que se va a introducir en ??l 

def crearArchivos(nombre , numero ):
    archivo = open(nombre + ".txt","w" , encoding = "utf-8")

    if nombre == "automovil electrico" or nombre == "autom??viles el??ctrico" :
        nombre = "autom??viles el??ctrico"
    elif nombre == "automovil"  or nombre == "autom??vil":
        nombre = "autom??vile"
    elif nombre == "profesor":
        nombre = "profesore"

    cuerpo = "La cantidad de " + nombre +"s ingresados es " + str(numero)
    archivo.write(cuerpo)
    archivo.close

#Usa el diccionario de ingresados junto la de los pisos para crear el archivo.txt diciendo el % de ocupamiento
def porcentajes(ingresados, dic_pisos):
    archivo = open("PorcentajePisos.txt","w")
    porcentajeTotal = ( ( len(ingresados))/550 ) * 100
    archivo.write("El parqueadero esta ocupado en un "+str(porcentajeTotal)+"%"+"\n")
    #ciclo que recorre el diccionario de ingresados y valida c??antas personas hay por piso
    for y in dic_pisos.keys():
        porcentaje = 0
        for x in range ( len(ingresados)):
            if ingresados[x][8] == y:
                porcentaje += 1
        if y == "Piso6":
            porcentaje = porcentaje * 2


        cuerpo = ("El porcentaje del " + y +" es " + str(porcentaje)+str("%")+"\n")

        archivo.write(cuerpo)

    archivo.close

#APERTURA DE LOS .JSON
archivoUsuarios= open("usuarios.json", "r", encoding="utf-8")
dic_usuarios = json.load(archivoUsuarios)

archivoPisos = open("tiposParqueaderos.json","r")
dic_pisos = json.load(archivoPisos)


orden = ""

while orden.lower() != "salir":
    
    print("\nSELECCIONE UNA DE LAS SIGUIENTES ACCIONES: \n" + 
    "\nREGISTRAR      Para registrar un veh??culo en la base de datos del parqueadero" + 
    "\nINGRESAR       Si  necesita ingresar al parqueadero" + 
    "\nRETIRAR        Si desea retirar su veh??culo del parqueadero" + 
    "\nUSUARIO        Para crear un reporte de la cantidad de veh??culos estacionados seg??n el tipo de usuario" + 
    "\nVEHICULO       Para crear un reporte de la cantidad de veh??culos estacionados seg??n el tipo de veh??culo" + 
    "\nPORCENTAJE     Para crear un reporte que indique el porcentaje de ocupaci??n del parqueadero")
    orden = str(input("     >"))


    if orden.lower() == "registrar":                                        
        nombre = str(input("   Ingrese su nombre y apellidos: "))
        numero = int(input("   Ingrese su n??mero de identificaci??n: "))


        nueva = registrar(dic_usuarios,nombre,numero)

        with open("usuarios.json","w") as file:
            json.dump(nueva , file)

    elif orden.lower() == "ingresar":                                         
        placa = input("   Ingrese la placa del vehiculo: ")
        #llamado a la funcion que valida el ingreso de los vehiculos
        viable = ValidaParqueaderosDispo(dic_pisos , placa , dic_usuarios)
        if viable:
            interfaz(dic_usuarios , placa, disponibles)

    elif orden.lower() == "retirar":
        #Borra de la matriz ingresados el indice retornado por la funci??n.
        del ingresados[retirar(ingresados)]
    
    elif  orden.lower() == "usuario":
        opciones = ["estudiante" , "profesor" , "personal administrativo" , "visitante"]
        tipoUsuario = ""
        while tipoUsuario.lower() not in opciones:
            tipoUsuario = input("   Ingrese el tipo de usuario deseado (estudiante, profesor, personal administrativo , visitante): ").lower()
            if tipoUsuario not in opciones:
                print("     El usuario que escogi?? no es v??lido.")
        indice = 2
        cantidad = cantidadTipo(tipoUsuario , indice , ingresados)
        #llama a la funci??n que crea.txt
        crearArchivos(tipoUsuario , cantidad)
        
    elif  orden.lower() == "vehiculo":
        opciones = ["automovil" , "automovil electrico" , "motocicleta" , "discapacitado", "autom??vil el??ctrico", "autom??vil"]
        tipoUsuario = ""
        while tipoUsuario.lower() not in opciones:
            tipoUsuario = input("   Ingrese el tipo de veh??culo deseado (automovil, automovil electrico, motocicleta, discapacitado): ").lower()
            if tipoUsuario not in opciones:
                print("     El veh??culo que escogi?? no es v??lido.")
        indice = 4
        cantidad = cantidadTipo(tipoUsuario , indice , ingresados)
        #llamado a la funci??n que crea el .txt
        crearArchivos(tipoUsuario , cantidad)

    elif  orden.lower() == "porcentaje":
        porcentajes(ingresados, dic_pisos)
