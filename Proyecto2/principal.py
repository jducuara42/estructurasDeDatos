from manejarJSON import *
from manejarJSON_UPZ import *

def main():
    print("\033[3;35m" + "          BIENVENIDO PROGRAMA ESTACIONES TRANSMILENIO")


    objetoJSON = ManejarJSON()
    print("\033[1;37m   | " + "Actualmente solo tenemos conexion entre las siguientes troncales: ")
    objetoJSON.leerRutas()
    objetoJSON.imprimirRutas()
    print("\033[1;33m" + "-------------------------------------------------------------")
    rutaElegida = int(input("\033[1;33m" + "Digite el numero de la ruta: "))
    print("\033[1;33m" + "-------------------------------------------------------------")
    objetoJSON.leerRuta(rutaElegida)
    objetoJSON.imprimirRuta()
    print("\033[1;33m" + "-------------------------------------------------------------")
    direccionElegida = input("\033[1;33m" + "Digite el numero de la direccion en que va: ")
    print("\033[1;33m" + "-------------------------------------------------------------")
    troncalLetraOrigen = objetoJSON.obtenerTroncalOrigen(direccionElegida)
    troncalLetraDestino = objetoJSON.obtenerTroncalDestino(direccionElegida)
    objetoJSON.leerEstaciones(troncalLetraOrigen)
    objetoJSON.imprimirEstaciones()
    print("\033[1;33m" + "-------------------------------------------------------------")
    estacionNumeroOrigen = int(input("\033[1;33m" + "Digite el # de la estacion de origen donde se encuentra: "))
    estacionNombreOrigen = objetoJSON.imprimirEstacion(estacionNumeroOrigen)
    print("\033[1;33m" + "-------------------------------------------------------------")
    objetoJSON.leerEstaciones(troncalLetraDestino)
    objetoJSON.imprimirEstaciones()
    print("\033[1;33m" + "------------------------------------------------------------")
    estacionNumeroDestino = int(input("\033[1;33m" + "Digite el # de la estacion de la estacion de destino: "))
    estacionNombreDestino = objetoJSON.imprimirEstacion(estacionNumeroDestino)
    print("\033[1;33m" + "------------------------------------------------------------")
    tuplaViaje = (estacionNumeroOrigen, estacionNumeroDestino, direccionElegida)

    print()
    print("\033[2;36m" + "Ud. viaja de la estacion " + estacionNombreOrigen + " a la estacion " + estacionNombreDestino)
    print("\033[6;34m" + "*** Iniciando trayecto...")
    objetoJSON.cargarListaEstaciones(troncalLetraOrigen, troncalLetraDestino, tuplaViaje)


    objetoUPZ = manejarJSON_UPZ()
    tabla_Hash = objetoUPZ.leerUPZ()
    print("\033[1;33m" + "-------------------------------------------------------------")
    UPZElegida = int(input("\033[1;33m" + "Digite el numero de la UPZ: "))
    print("\033[1;33m" + "-------------------------------------------------------------")
    objetoUPZ.buscarUPZ(UPZElegida, tabla_Hash)
    objetoJSON.leerTroncales()
main()