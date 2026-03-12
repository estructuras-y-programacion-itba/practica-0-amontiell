import random

def numeros():
    numero = random.randint(1, 6)
    return numero

def tiradas():
    cont = 0
    salida = []
    while cont < 5:
        salida.append(numeros())
        cont += 1
    return salida

def copy(salida):
    copia = salida[:]
    return copia

def ordenar(lista):
    copia = copy(lista)
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if copia[i] > copia[j]:
                aux = copia[i]
                copia[i] = copia[j]
                copia[j] = aux
    return copia

def unicos(salida):
    dados_unicos = []
    for i in range(len(salida)):
        if salida[i] not in dados_unicos:
            dados_unicos.append(salida[i])
    return dados_unicos

def contar_numero(salida, num):
    cont = 0
    for i in range(len(salida)):
        if salida[i] == num:
            cont += 1
    return cont

def escalera(salida):
    ordenada = ordenar(salida)
    if ordenada == [1,2,3,4,5] or ordenada == [2,3,4,5,6]:
        return True
    else:
        return False

def full(salida):
    dados_unicos = unicos(salida)
    if len(dados_unicos) != 2:
        return False
    c1 = contar_numero(salida, dados_unicos[0])
    c2 = contar_numero(salida, dados_unicos[1])
    if (c1 == 3 and c2 == 2) or (c1 == 2 and c2 == 3):
        return True
    else:
        return False

def poker(salida):
    dados_unicos = unicos(salida)
    i = 0
    while i < len(dados_unicos):
        cant = contar_numero(salida, dados_unicos[i])
        if cant == 4:
            return True
        i += 1
    return False

def generala(salida):
    if len(unicos(salida)) == 1:
        return True
    else:
        return False

def suma_numero(salida, num):
    suma = 0
    for i in range(len(salida)):
        if salida[i] == num:
            suma += salida[i]
    return suma

def mostrar_dados(salida):
    print("Dados:", salida)

def definir_tirada(salida):
    tiros = 2
    mostrar_dados(salida)

    while tiros > 0:
        pregunta = input("¿Desea seguir tirando? (SI/NO) ")
        while pregunta != "SI" and pregunta != "NO":
            pregunta = input("Ingrese SI o NO: ")

        if pregunta == "NO":
            return salida
        else:
            cuantos = input("Ingrese cuántos dados desea volver a tirar: ")
            while cuantos.isdigit() == False:
                cuantos = input("Ingrese un número válido: ")
            cuantos = int(cuantos)

            while cuantos < 1 or cuantos > 5:
                cuantos = input("Ingrese cuántos dados desea volver a tirar (1-5): ")
                while cuantos.isdigit() == False:
                    cuantos = input("Ingrese un número válido: ")
                cuantos = int(cuantos)

            usados = []
            while cuantos > 0:
                pos = input("Ingrese el dado que desea tirar nuevamente (1-5) ")
                while pos.isdigit() == False:
                    pos = input("Ingrese una posición válida (1-5): ")
                pos = int(pos)

                while pos < 1 or pos > 5 or pos in usados:
                    pos = input("Ingrese una posición válida no repetida (1-5): ")
                    while pos.isdigit() == False:
                        pos = input("Ingrese una posición válida (1-5): ")
                    pos = int(pos)

                usados.append(pos)
                salida[pos - 1] = numeros()
                cuantos -= 1

            mostrar_dados(salida)

        tiros -= 1

    return salida

def crear_planilla():
    planilla = []
    categorias = ["E","F","P","G","1","2","3","4","5","6"]
    i = 0
    while i < len(categorias):
        fila = [categorias[i], "", ""]
        planilla.append(fila)
        i += 1
    return planilla

def mostrar_planilla(planilla):
    print()
    print("PLANILLA")
    print("jugada   j1   j2")
    i = 0
    while i < len(planilla):
        print(str(planilla[i][0]) + ":", "    ", planilla[i][1], "  ", planilla[i][2])
        i += 1
    print()

def guardar_jugadas_csv(planilla):
    archivo = open("jugadas.csv", "w")
    archivo.write("jugada:,j1,j2\n")
    i = 0
    while i < len(planilla):
        jugada = str(planilla[i][0]) + ":"
        j1 = str(planilla[i][1])
        j2 = str(planilla[i][2])
        archivo.write(jugada + "," + j1 + "," + j2 + "\n")
        i += 1
    archivo.close()

def buscar_fila(planilla, categoria):
    i = 0
    while i < len(planilla):
        if planilla[i][0] == categoria:
            return i
        i += 1
    return -1

def categoria_disponible(planilla, jugador, categoria):
    fila = buscar_fila(planilla, categoria)
    if fila == -1:
        return False

    if jugador == 1:
        if planilla[fila][1] == "":
            return True
        else:
            return False
    else:
        if planilla[fila][2] == "":
            return True
        else:
            return False

def categorias_pendientes(planilla, jugador):
    pendientes = []
    i = 0
    while i < len(planilla):
        if jugador == 1:
            if planilla[i][1] == "":
                pendientes.append(planilla[i][0])
        else:
            if planilla[i][2] == "":
                pendientes.append(planilla[i][0])
        i += 1
    return pendientes

def anotar_en_planilla(planilla, jugador, categoria, puntaje):
    fila = buscar_fila(planilla, categoria)
    if jugador == 1:
        planilla[fila][1] = puntaje
    else:
        planilla[fila][2] = puntaje

def puntaje_categoria(salida, categoria, primera_tirada):
    if categoria == "E":
        if escalera(salida) == True:
            puntaje = 20
            if escalera(primera_tirada) == True:
                puntaje += 5
            return puntaje
        else:
            return 0

    elif categoria == "F":
        if full(salida) == True:
            puntaje = 30
            if full(primera_tirada) == True:
                puntaje += 5
            return puntaje
        else:
            return 0

    elif categoria == "P":
        if poker(salida) == True:
            puntaje = 40
            if poker(primera_tirada) == True:
                puntaje += 5
            return puntaje
        else:
            return 0

    elif categoria == "G":
        if generala(salida) == True:
            return 50
        else:
            return 0

    else:
        numero = int(categoria)
        return suma_numero(salida, numero)

def elegir_categoria(planilla, jugador):
    pendientes = categorias_pendientes(planilla, jugador)
    print("Categorías disponibles:", pendientes)

    categoria = input("Elija una categoría para anotar: ")
    while categoria_disponible(planilla, jugador, categoria) == False:
        categoria = input("Categoría inválida o ya usada. Elija otra: ")

    return categoria

def suma_total_jugador(planilla, jugador):
    suma = 0
    i = 0
    while i < len(planilla):
        if jugador == 1:
            if planilla[i][1] != "":
                suma += planilla[i][1]
        else:
            if planilla[i][2] != "":
                suma += planilla[i][2]
        i += 1
    return suma

def planilla_completa(planilla):
    i = 0
    while i < len(planilla):
        if planilla[i][1] == "" or planilla[i][2] == "":
            return False
        i += 1
    return True

def que_anoto(salida, primera_tirada):
    print("Con esta tirada se puede anotar:")

    if generala(salida) == True:
        if generala(primera_tirada) == True:
            print("- G (Generala Real)")
        else:
            print("- G (Generala)")

    if poker(salida) == True:
        if poker(primera_tirada) == True:
            print("- P (Poker servido)")
        else:
            print("- P (Poker)")

    if full(salida) == True:
        if full(primera_tirada) == True:
            print("- F (Full servido)")
        else:
            print("- F (Full)")

    if escalera(salida) == True:
        if escalera(primera_tirada) == True:
            print("- E (Escalera servida)")
        else:
            print("- E (Escalera)")

    print("- 1, 2, 3, 4, 5, 6")

def turno_jugador(planilla, jugador):
    print()
    print("Turno del jugador", jugador)

    salida = tiradas()
    primera_tirada = copy(salida)

    if generala(primera_tirada) == True:
        print("¡GENERALA REAL!")
        anotar_en_planilla(planilla, jugador, "G", 80)
        guardar_jugadas_csv(planilla)
        return True

    salida = definir_tirada(salida)

    que_anoto(salida, primera_tirada)

    categoria = elegir_categoria(planilla, jugador)
    puntaje = puntaje_categoria(salida, categoria, primera_tirada)

    anotar_en_planilla(planilla, jugador, categoria, puntaje)
    guardar_jugadas_csv(planilla)

    print("Se anotaron", puntaje, "puntos en", categoria)
    return False

def informar_ganador(planilla):
    total1 = suma_total_jugador(planilla, 1)
    total2 = suma_total_jugador(planilla, 2)

    print()
    print("PUNTAJE FINAL")
    print("Jugador 1:", total1)
    print("Jugador 2:", total2)

    if total1 > total2:
        print("Ganó el Jugador 1")
    elif total2 > total1:
        print("Ganó el Jugador 2")
    else:
        print("Empate")

def juego():
    planilla = crear_planilla()
    guardar_jugadas_csv(planilla)

    fin = False
    while fin == False:
       

        real = turno_jugador(planilla, 1)
        if real == True:
            
            print("El Jugador 1 ganó por Generala Real")
            return

        if planilla_completa(planilla) == True:
            fin = True
        else:
            

            real = turno_jugador(planilla, 2)
            if real == True:
                
                print("El Jugador 2 ganó por Generala Real")
                return

            if planilla_completa(planilla) == True:
                fin = True

    
    informar_ganador(planilla)

juego()