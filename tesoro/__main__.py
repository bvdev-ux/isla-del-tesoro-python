"""Ejecuta la aventura con python -m tesoro."""

from .juego import Juego
from .mundo import DIRECCIONES

AYUDA = "Comandos: norte, sur, este, oeste, mirar, explorar, inventario, mapa, descansar, ayuda, salir"


def main():
    juego = Juego()
    print("ISLA DEL TESORO\nEncuentra la llave y abre el cofre antes de agotar tu energia.")
    print(AYUDA)
    print(juego.mirar())
    while not juego.terminado:
        try:
            comando = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nHasta la proxima aventura!")
            return
        if comando == "salir":
            print("Hasta la proxima aventura!")
            return
        if comando in DIRECCIONES:
            resultado = juego.mover(comando)
        elif comando == "explorar":
            resultado = juego.explorar()
        elif comando == "descansar":
            resultado = juego.descansar()
        elif comando == "mirar":
            resultado = juego.mirar()
        elif comando == "mapa":
            resultado = juego.mapa()
        elif comando == "inventario":
            resultado = "Inventario: " + ("llave antigua" if juego.tiene_llave else "vacio")
        elif comando == "ayuda":
            resultado = AYUDA
        else:
            resultado = "Comando desconocido. Escribe ayuda."
        print(resultado)


if __name__ == "__main__":
    main()
