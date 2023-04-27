# 1. Leer dos (2) números y los imprima en forma ascendente.

""" try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
except ValueError:
    print("ERROR: No puedes ingresar una letra o caracter")
except:
    print("ERROR indefinido") """

# -------------------------------------------------------------------------------------------------------------------------


# 2. (Sentencia match) Diseñar un algoritmo que lea por teclado un número
# comprendido entre 1 y 10. Se desea visualizar si el número es par o impar. En primer
# lugar, se deberá
# detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
# si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”; si es 2, 4, 6, 8, 10, escribir
# un mensaje de “par”.

""" try:
    numero = int(input("Ingresa un numero: "))
    if numero >= 1 and numero <= 10:
        match numero:
            case numero if numero%2 == 0:
                print("Par")
            case numero if numero%2 != 0:
                print("Impar")

            # ↓↓↓ DE MANERA INDIVIDUAL ↓↓↓
            # case 1:
            #     print("Impar")
            # case 2:
            #     print("Par")
            # case 3:
            #     print("Impar")
            # case 4:
            #     print("Par")
            # case 5:
            #     print("Impar")
            # case 6:
            #     print("Par")
            # case 7:
            #     print("Impar")
            # case 8:
            #     print("Par")
            # case 9:
            #     print("Impar")
            # case 10:
            #     print("Par")
    else:
        print("ERROR: El numero debe estar en el rango de 1 a 10")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# -------------------------------------------------------------------------------------------------------------------------


# 3. (Sentencia match) Diseñar un algoritmo que lea un número entero entre 1 y 10, y
# nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído
# no está comprendido entre 1 y 10 mostrar un mensaje de error.

""" try:
    numero = int(input("Ingresa un numero: "))
    match numero:
        case 1:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("Tres")
        case 4:
            print("Cuatro")
        case 5:
            print("Cinco")
        case 6:
            print("Seis")
        case 7:
            print("Siete")
        case 8:
            print("Ocho")
        case 9:
            print("Nueve")
        case 10:
            print("Diez")
        case other:
            print("ERROR: El numero debe estar en el rango del 1 al 10")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# -------------------------------------------------------------------------------------------------------------------------


# 4. Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta
# lo siguiente:
# • toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
# • cada minuto adicional a partir de los tres primeros es un paso de contador y
# cuesta 100 pesos.

""" try:
    minutos = int(input("Duracion en minutos de la llamada: "))
    if minutos <= 0:
        print("ERROR: Debes ingresar un valor a partir de 1")
    elif minutos <= 3:
        print("El coste de la llamada es de $200 pesos")
    else:
        total = 200 + (minutos-3) * 100
        print(f"El coste de la llamada es de ${total} pesos")
except ValueError:
    print("ERROR: No puedes ingresar una letra o caracter")
except:
    print("ERROR indefinido")
 """

# -------------------------------------------------------------------------------------------------------------------------


# 5. En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros
# y Y conejos blancos. Hacer un algoritmo que:
# • Imprima la cantidad de conejos vendida
# • Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de
# los conejos negros, imprima el monto total de la venta.
# • Imprima el color de los conejos que se vendieron más.

""" try:
    conejos = int(input("Ingrese la cantidad de conejos: "))
    blancos = int(input("Ingrese la cantidad de conejos blancos: "))
    negros = int(input("Ingrese la cantidad de conejos negros: "))
    try:
        if blancos + negros == conejos:
            precio_b = float(input("Precio de venta de los conejos blancos: "))
            precio_n = float(input("Precio de venta de los conejos negros: "))
            try:
                vendidos_b = int(input("Cantidad de conejos blancos vendidos: "))
                vendidos_n = int(input("Cantidad de conejos negros vendidos: "))

                if (vendidos_b < 1 or vendidos_b > blancos) and (vendidos_n < 1 or vendidos_n > negros):
                    print("La cantidad de conejos vendidos de AMBOS colores supera o es menor a la cantidad disponible")
                elif vendidos_b < 1 or vendidos_b > blancos:
                    print("La cantidad de conejos vendidos del color BLANCO supera o es menor a la cantidad disponible")
                elif vendidos_n < 1 or vendidos_n > negros:
                    print("La cantidad de conejos vendidos del color NEGRO supera o es menor a la cantidad disponible")
                else:
                    total_vendidos = vendidos_n + vendidos_b
                    total_venta = (precio_b * vendidos_b) + (precio_n * vendidos_n)

                    print("\n---------Resultados Finales-----------")
                    print(f"La cantidad de conejos vendidos son: {total_vendidos}")
                    print(f"El total de la venta es de: ${total_venta}")
                    if vendidos_b > vendidos_n:
                        print("Los conejos de color blanco se vendieron mas")
                    else:
                        print("Los conejos de color negro se vendieron mas")
                    print("--------------------------------------\n")
            except ValueError:
                print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
        else:
            print("ERROR: Estas ingresando una cantidad erronea de conejos")
    except ValueError:
        print("ERROR: No puedes ingresar letras o caracteres")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# -------------------------------------------------------------------------------------------------------------------------


# 6. Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes,
# determinadas sobre las siguientes condiciones:
# • NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante
# tendrá 3 evaluaciones.
# • NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante
# presentara 2 trabajos.
# • NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
# • Nota mínima 1,0 nota máxima: 5,0

""" print("\nINGRESA SOLO NOTAS ENTERAS (EJEMPLO: si tienes una nota de 1.0 debes poner 10)\n")
try:
    nota_ev1 = int(input("Ingresa la nota de la primera evaluacion: "))
    nota_ev2 = int(input("Ingresa la nota de la segunda evaluacion: "))
    nota_ev3 = int(input("Ingresa la nota de la tercera evaluacion: "))

    if (nota_ev1 >= 10 and nota_ev1 <= 50) and (nota_ev2 >= 10 and nota_ev2 <= 50) and (nota_ev3 >= 10 and nota_ev3 <= 50):
        
        totalnota_evs = ((nota_ev1 + nota_ev2 + nota_ev3) / 3) * 0.6
        # mensaje de la nota si se quiere saber inmediatamente
        # print("La nota final del promedio de las evaluaciones por el 60% es: ", totalnota_evs)
        
        nota_tra1 = int(input("Ingresa la nota del primer trabajo: "))
        nota_tra2 = int(input("Ingresa la nota del segundo trabajo: "))

        if (nota_tra1 >= 10 and nota_tra1 <= 50) and (nota_tra2 >= 10 and nota_tra2 <= 50):
            
            totalnota_tra = ((nota_tra1 + nota_tra2) / 2) * 0.4
            # mensaje de la nota si se quiere saber inmediatamente
            # print("La nota final del promedio de los trabajos por el 40% es: ", totalnota_tra)
            notafinal = totalnota_evs + totalnota_tra
            print("\n---------Resultados Finales-----------")
            print("La nota final de las evaluaciones es: ", totalnota_evs)
            print("La nota final de los trabajos es: ", totalnota_tra)
            print("La nota final es: ", notafinal)
            print("--------------------------------------\n")
        else:
            print("ERROR: Alguna de las notas tiene un valor erroneo")
    else:
        print("ERROR: Alguna de las notas tiene un valor erroneo")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# -------------------------------------------------------------------------------------------------------------------------


# 7. Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,
# cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
# clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo
# existen dos claves).

""" try:
    nombre_art = input("Ingrese el nombre del articulo: ")
    clave = int(input("Ingrese la clave: "))

    if clave == 1 or clave == 2:
        try:
            precio_ori = float(input("Ingrese el precio del articulo: "))
            try:
                cantidad = int(input("Ingrese la cantidad a comprar: "))

                if precio_ori and cantidad > 0:
                    if clave == 1:
                        desc_clave = 10
                        precio_total = precio_ori * cantidad
                        descuento = precio_total - (precio_total * (desc_clave/100))

                    else:
                        desc_clave = 20
                        precio_total = precio_ori * cantidad
                        descuento = precio_total - (precio_total * (desc_clave/100))

                    print("\n---------Resultados Finales-----------")
                    print(f"Articulo: {nombre_art}")
                    print(f"Clave: {clave}")
                    print(f"Precio unidad: ${precio_ori}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Precio original: ${precio_total}")
                    print(f"Precio con descuento del {desc_clave}%: ${descuento}")
                    print("--------------------------------------\n")
                else:
                    print("ERROR: No puedes poner valores menores o iguales a 0")
            except ValueError:
                print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
        except ValueError:
            print("ERROR: No puedes ingresar letras o caracteres")
    else:
        print("ERROR: La clave ingresada es incorrecta")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# -------------------------------------------------------------------------------------------------------------------------


# 8. En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología.
# El presupuesto anual del hospital se reparte a estas tres (3) áreas; usted
# debe realizar un algoritmo que permita ingresar el valor del presupuesto
# anual, ingresar el porcentaje correspondiente a cada área, realizar el
# cálculo del presupuesto que corresponde a cada área, si la suma de los
# porcentajes no corresponde al 100% debe mostrar un mensaje de error.
# Mostrar el porcentaje asignado a cada área y el presupuesto obtenido.

""" try:
    presupuesto = float(input("Ingrese el presupuesto anual: "))

    if presupuesto > 0:
        porc_psi = float(input("Ingrese el porcentaje correspondiente al area de Psiquiatría: "))
        porc_ped = float(input("Ingrese el porcentaje correspondiente al area de Pediatría: "))
        porc_tra = float(input("Ingrese el porcentaje correspondiente al area de Traumatología: "))

        if porc_psi + porc_ped + porc_tra == 100:
            presu_psi = presupuesto * (porc_psi/100)
            presu_ped = presupuesto * (porc_ped/100)
            presu_tra = presupuesto * (porc_tra/100)

            print("\n---------Resultados Finales-----------")
            print(f"Area Psiquiatría\nPorcentaje asignado: {porc_psi}%\nPresupuesto obtenido: ${presu_psi}\n")
            print(f"Area Pediatría\nPorcentaje asignado: {porc_ped}%\nPresupuesto obtenido: ${presu_ped}\n")
            print(f"Area Traumatología\nPorcentaje asignado: {porc_tra}%\nPresupuesto obtenido: ${presu_tra}")
            print("--------------------------------------\n")
        else:
            print("ERROR: La suma de los porcentajes no equivalen al 100% del presupuesto")
    else:
        print("ERROR: No puedes ingresar un presupuesto menor o igual a $0")
except ValueError:
    print("ERROR: No puedes ingresar letras o caracteres")
except:
    print("ERROR indefinido") """

# -------------------------------------------------------------------------------------------------------------------------


# 9. Diseñar un algoritmo para determinar el precio del tiquete de ida y vuelta en avión,
# conociendo la distancia a recorrer, sabiendo que si el número de días de estancia es
# superior o igual a 7 y la distancia superior a 800 km el billete tiene una reducción del
# 30%. El precio por km es de $2,5 dólares.

""" try:
    dias = int(input("Ingresa la cantidad de dias de estancia: "))
    try:
        distancia = float(input("Ingresa la distancia total en km: "))

        if dias and distancia > 0:
            if dias >= 7 and distancia > 800:
                precio = (distancia * 2.5) - ((distancia * 2.5) * 0.3)
            else:
                precio = distancia * 2.5

            print("\n---------Resultados Finales-----------")
            print(f"El precio del tiquete es de: ${precio} dolares")
            print("--------------------------------------\n")
        else:
            print("ERROR: Debes ingresar valores superiores a 0")
    except ValueError:
        print("ERROR: No puedes ingresar letras o caracteres")
except ValueError:
    print("ERROR: No puedes ingresar letras, caracteres o numeros decimales")
except:
    print("ERROR indefinido") """


# CODED BY: juan torra
