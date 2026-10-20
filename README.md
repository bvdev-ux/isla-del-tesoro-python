# Isla del tesoro

Una aventura de terminal escrita en Python, sin dependencias externas.

Explora una isla de nueve lugares, encuentra una llave antigua y abre el cofre
antes de quedarte sin energía. Incluye un mapa de zonas visitadas y un registro
local de las cinco mejores puntuaciones.

## Requisitos y ejecución

Instala Python 3.10 o superior. Desde la carpeta del proyecto ejecuta:

```sh
python -m tesoro
```

En Windows también puedes usar `py -m tesoro` si tienes el lanzador instalado.
No necesitas instalar paquetes con pip.

## Cómo jugar

| Comando | Acción |
| --- | --- |
| `norte`, `sur`, `este`, `oeste` | Moverte por la isla |
| `mirar` | Leer la pista del lugar y consultar tu energía |
| `explorar` | Recoger la llave o abrir el cofre |
| `inventario` | Consultar si tienes la llave |
| `mapa` | Ver tu posición y lugares visitados; el norte está arriba |
| `descansar` | Recuperar 4 puntos de energía en la laguna, una sola vez |
| `ayuda` | Mostrar los comandos |
| `salir` | Terminar la partida |

Comienzas con 12 puntos de energía. Cada movimiento válido consume uno.
Si llegas a cero, pierdes. Mirar, explorar y los comandos inválidos no consumen energía.
Al ganar recibes `100 + energía restante × 10 − pasos × 2` puntos.
Las puntuaciones se guardan en `records.json`, junto a la carpeta `tesoro`.
El archivo queda excluido de Git. Cada ejecución inicia una aventura nueva.

<details>
<summary>Ver una ruta ganadora</summary>

```text
este
norte
explorar
norte
explorar
```

Esta ruta obtiene 184 puntos. ¡Puedes mejorarla aprovechando la laguna!
</details>

## Pruebas

```sh
python -m unittest discover -s tests -v
```

Las nueve pruebas verifican la victoria, la llave, los límites del mapa,
la energía, el descanso, las visitas y la persistencia de puntuaciones.
GitHub Actions también ejecuta las pruebas al subir cambios.

## Estructura

```text
tesoro/
  __main__.py   # Interfaz de terminal
  juego.py      # Estado y reglas
  mundo.py      # Mapa y pistas
  records.py    # Puntuaciones locales
tests/
  test_juego.py
```
