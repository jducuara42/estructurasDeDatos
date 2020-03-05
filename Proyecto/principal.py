from manejarXML import *

def main():
    print("\033[3;35m" + "      BIENVENIDO PROGRAMA ESTACIONES TRANSMILENIO")
    troncalLetraOrigen = ""
    troncalLetraDestino = ""
    objetoXML = ManejarXML()
    #objetoXML.leerTroncales()
    #print("\033[3;34m" + "  Listado de troncales:")
    #objetoXML.imprimirTroncales()
    print("\033[1;37m | " + "Actualmente solo tenemos conexion entre las siguientes troncales: ")
    objetoXML.leerRutas()
    objetoXML.imprimirRutas()
    rutaElegida = input("\033[1;33m" + " Digite el numero de la ruta: ")
    objetoXML.leerRuta(rutaElegida)
    objetoXML.imprimirRuta()
    troncalLetraOrigen = objetoXML.obtenerTroncalOrigen(1)
    troncalLetraDestino = objetoXML.obtenerTroncalDestino(1)
    print(" troncalLetraOrigen: " + troncalLetraOrigen)
    print(" troncalLetraDestino: " + troncalLetraDestino)
    objetoXML.leerEstaciones(troncalLetraOrigen)
    objetoXML.imprimirEstaciones()
    print("-------------------------------------------------------")
    objetoXML.leerEstaciones(troncalLetraDestino)
    objetoXML.imprimirEstaciones()


    direccionElegida = input("\033[1;33m" + " Digite el numero de la direccion en que va: ")

    print("\033[3;34m" + "  Listado de estaciones:")


    troncalLetraOrigen = objetoXML.obtenerTroncalOrigen(direccionElegida)
    troncalLetraDestino = objetoXML.obtenerTroncalDestino(direccionElegida)





    """
    objetoXML.leerEstaciones("A")
    print("\033[3;34m" + "  Listado de estaciones:")
    objetoXML.imprimirEstaciones()

    troncalLetraOrigen = input("\033[1;33m" + " Digite la letra de la troncal de origen donde se encuentra: ")
    troncalLetraDestino = input("\033[1;33m" + " Digite la letra de la troncal de destino a donde va: ")
    troncalNombreOrigen = objetoXML.imprimirTroncal(troncalLetraOrigen.upper())
    troncalNombreDestino = objetoXML.imprimirTroncal(troncalLetraDestino.upper())
    print(" Ud. viaja De troncal " + troncalNombreOrigen + " a troncal " + troncalNombreDestino)

    objetoXML.leerEstaciones(troncalLetraOrigen)
    print("\033[3;34m" + "  Listado de estaciones de Origen:")
    objetoXML.imprimirEstaciones()
    estacionNumeroOrigen = input("\033[1;33m" + " Digite el # de la estacion de origen donde se encuentra: ")
    estacionNombreOrigen = objetoXML.imprimirEstacion(estacionNumeroOrigen)

    objetoXML.leerEstaciones(troncalLetraDestino)
    print("\033[3;34m" + "  Listado de estaciones de Destino:")
    objetoXML.imprimirEstaciones()
    estacionNumeroDestino = input("\033[1;33m" + " Digite el # de la estacion de la estacion de destino: ")
    estacionNombreDestino = objetoXML.imprimirEstacion(estacionNumeroDestino)

    print(" Ud. viaja de la estacion " + estacionNombreOrigen + " a la estacion " + estacionNombreDestino)
    """

    """"
    troncalLetraOrigen = "B"
    troncalLetraDestino = "E"
    objetoXML.cargarListaEstaciones(troncalLetraOrigen, troncalLetraDestino)
    """
    print("Iniciando trayecto...")

main()