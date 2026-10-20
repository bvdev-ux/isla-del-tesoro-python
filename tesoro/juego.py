"""Reglas del juego independientes de la entrada y salida."""

from dataclasses import dataclass, field

from .mundo import DIRECCIONES, INICIO, LAGUNA, LLAVE, LUGARES, TESORO


@dataclass
class Juego:
    posicion: tuple[int, int] = INICIO
    energia: int = 12
    pasos: int = 0
    tiene_llave: bool = False
    descanso_usado: bool = False
    victoria: bool = False
    visitados: set[tuple[int, int]] = field(default_factory=lambda: {INICIO})

    @property
    def terminado(self):
        return self.victoria or self.energia <= 0

    @property
    def puntos(self):
        return max(0, 100 + self.energia * 10 - self.pasos * 2) if self.victoria else 0

    def mirar(self):
        nombre, pista = LUGARES[self.posicion]
        return f"{nombre}: {pista}\nEnergia: {self.energia} | Pasos: {self.pasos}"

    def mover(self, direccion):
        if self.terminado:
            return "La partida ha terminado."
        if direccion not in DIRECCIONES:
            return "Direccion desconocida. Usa norte, sur, este u oeste."
        dx, dy = DIRECCIONES[direccion]
        destino = (self.posicion[0] + dx, self.posicion[1] + dy)
        if destino not in LUGARES:
            return "Solo hay mar por ese camino."
        self.posicion = destino
        self.visitados.add(destino)
        self.energia -= 1
        self.pasos += 1
        if self.energia == 0:
            return "Te has quedado sin energia. Fin de la aventura."
        return self.mirar()

    def explorar(self):
        if self.terminado:
            return "La partida ha terminado."
        if self.posicion == LLAVE and not self.tiene_llave:
            self.tiene_llave = True
            return "Has recogido la llave antigua."
        if self.posicion == TESORO:
            if not self.tiene_llave:
                return "El cofre esta cerrado. Busca la llave en las ruinas."
            self.victoria = True
            return f"Has encontrado el tesoro! Puntuacion: {self.puntos}"
        return "No encuentras objetos nuevos."

    def descansar(self):
        if self.terminado:
            return "La partida ha terminado."
        if self.posicion != LAGUNA:
            return "Solo puedes descansar en la laguna."
        if self.descanso_usado:
            return "Ya has descansado en esta partida."
        self.descanso_usado = True
        self.energia += 4
        return "Bebes agua fresca y recuperas 4 puntos de energia."

    def mapa(self):
        filas = []
        for y in range(2, -1, -1):
            filas.append(" ".join(
                "@" if (x, y) == self.posicion else "+" if (x, y) in self.visitados else "?"
                for x in range(3)
            ))
        return "Norte arriba\n" + "\n".join(filas) + "\n@ Tu posicion | + Visitado | ? Sin explorar"
