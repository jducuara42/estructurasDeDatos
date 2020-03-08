from manejarXML import *

def main():
    """
    lat2 = math.radians(9.366429043)
    lon2 = math.radians(-67.9766140)
    lat1 = math.radians(9.483648265)
    lon1 = math.radians(-67.4801781)
    print("lat2: ", lat2, " lat1: ", lat1)
    print("lon2: ", lon2, " lon1: ", lon1)

    #lat2, lon2, lat1, lon1 = map(radians, [lat2, lon2, lat1, lon1])
    latitudTotal = lat2 - lat1
    lontitudTotal = lon2 - lon1

    resultado = (sin(latitudTotal / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lontitudTotal / 2) ** 2)
    resultadoFinal = 2 * 6367 * atan(sqrt(resultado))
    #km = 2 * 6367 * resultadoFinal
    print(resultadoFinal)
    """


    print("\033[3;35m" + "          BIENVENIDO PROGRAMA ESTACIONES TRANSMILENIO")
    troncalLetraOrigen = ""
    troncalLetraDestino = ""
    objetoXML = ManejarXML()
    #objetoXML.leerTroncales()
    #print("\033[3;34m" + "  Listado de troncales:")
    #objetoXML.imprimirTroncales()
    print("\033[1;37m   | " + "Actualmente solo tenemos conexion entre las siguientes troncales: ")
    objetoXML.leerRutas()
    objetoXML.imprimirRutas()
    print("\033[1;33m" + "-------------------------------------------------------------")
    rutaElegida = input("\033[1;33m" + "Digite el numero de la ruta: ")
    print("\033[1;33m" + "-------------------------------------------------------------")
    objetoXML.leerRuta(rutaElegida)
    objetoXML.imprimirRuta()
    print("\033[1;33m" + "-------------------------------------------------------------")
    direccionElegida = input("\033[1;33m" + "Digite el numero de la direccion en que va: ")
    print("\033[1;33m" + "-------------------------------------------------------------")
    troncalLetraOrigen = objetoXML.obtenerTroncalOrigen(direccionElegida)
    troncalLetraDestino = objetoXML.obtenerTroncalDestino(direccionElegida)
    """
    print(" troncalLetraOrigen: " + troncalLetraOrigen)
    print(" troncalLetraDestino: " + troncalLetraDestino)
    """
    objetoXML.leerEstaciones(troncalLetraOrigen)
    objetoXML.imprimirEstaciones()
    print("\033[1;33m" + "-------------------------------------------------------------")
    estacionNumeroOrigen = input("\033[1;33m" + "Digite el # de la estacion de origen donde se encuentra: ")
    estacionNombreOrigen = objetoXML.imprimirEstacion(estacionNumeroOrigen)
    print("\033[1;33m" + "-------------------------------------------------------------")
    objetoXML.leerEstaciones(troncalLetraDestino)
    objetoXML.imprimirEstaciones()
    print("\033[1;33m" + "------------------------------------------------------------")
    estacionNumeroDestino = input("\033[1;33m" + "Digite el # de la estacion de la estacion de destino: ")
    estacionNombreDestino = objetoXML.imprimirEstacion(estacionNumeroDestino)
    print("\033[1;33m" + "------------------------------------------------------------")
    #print ("origen: " + estacionNumeroOrigen + "Destino: " + estacionNumeroDestino)
    tuplaViaje = (estacionNumeroOrigen, estacionNumeroDestino, direccionElegida)

    print()
    print("\033[2;36m" + "Ud. viaja de la estacion " + estacionNombreOrigen + " a la estacion " + estacionNombreDestino)
    print("\033[6;34m" + "*** Iniciando trayecto...")
    objetoXML.cargarListaEstaciones(troncalLetraOrigen, troncalLetraDestino, tuplaViaje)


main()