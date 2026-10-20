import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tesoro.juego import Juego
from tesoro.records import guardar


class JuegoTests(unittest.TestCase):
    def test_ruta_ganadora(self):
        juego = Juego()
        juego.mover("este")
        juego.mover("norte")
        juego.explorar()
        self.assertTrue(juego.tiene_llave)
        juego.mover("norte")
        juego.explorar()
        self.assertTrue(juego.victoria)
        self.assertEqual(juego.puntos, 184)

    def test_cofre_necesita_llave(self):
        juego = Juego()
        for direccion in ("este", "norte", "norte"):
            juego.mover(direccion)
        juego.explorar()
        self.assertFalse(juego.victoria)

    def test_movimientos_invalidos_no_consumen_energia(self):
        juego = Juego()
        juego.mover("sur")
        juego.mover("volar")
        self.assertEqual((juego.posicion, juego.energia, juego.pasos), ((0, 0), 12, 0))

    def test_descanso_solo_en_laguna_y_una_vez(self):
        juego = Juego()
        juego.descansar()
        self.assertEqual(juego.energia, 12)
        juego.mover("norte")
        juego.descansar()
        juego.descansar()
        self.assertEqual(juego.energia, 15)

    def test_sin_energia_no_puede_actuar(self):
        juego = Juego()
        for _ in range(6):
            juego.mover("este")
            juego.mover("oeste")
        self.assertTrue(juego.terminado)
        juego.mover("norte")
        juego.descansar()
        juego.explorar()
        self.assertEqual((juego.posicion, juego.energia, juego.pasos), ((0, 0), 0, 12))
        self.assertEqual(juego.puntos, 0)

    def test_mapa_marca_visitas(self):
        juego = Juego()
        juego.mover("este")
        self.assertIn("+ @ ?", juego.mapa())

    def test_victoria_no_permite_seguir_moviendose(self):
        juego = Juego(posicion=(1, 2), tiene_llave=True)
        juego.explorar()
        juego.mover("sur")
        self.assertEqual(juego.posicion, (1, 2))


class RecordsTests(unittest.TestCase):
    def test_top_cinco_persistente(self):
        with TemporaryDirectory() as carpeta:
            archivo = Path(carpeta) / "records.json"
            for puntos in (40, 100, 20, 80, 60, 90):
                mejores = guardar(puntos, archivo)
            self.assertEqual(mejores, [100, 90, 80, 60, 40])
            self.assertEqual(json.loads(archivo.read_text()), mejores)

    def test_recupera_archivo_invalido(self):
        with TemporaryDirectory() as carpeta:
            archivo = Path(carpeta) / "records.json"
            for contenido in ('roto', '{}', '[true, -2, "hola", 20]'):
                archivo.write_text(contenido)
                mejores = guardar(50, archivo)
                self.assertEqual(mejores[0], 50)
                self.assertTrue(all(type(n) is int and n >= 0 for n in mejores))


if __name__ == "__main__":
    unittest.main()
