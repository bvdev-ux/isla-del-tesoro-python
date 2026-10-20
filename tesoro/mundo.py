"""Mapa fijo: cada partida se puede resolver sin depender del azar."""

LUGARES = {
    (0, 0): ("Playa", "Las olas borran tus huellas. El bosque esta al este."),
    (1, 0): ("Bosque", "Un sendero conduce al norte, hacia las ruinas."),
    (2, 0): ("Mirador", "Ves una cueva al norte de las ruinas."),
    (0, 1): ("Laguna", "Agua cristalina: puedes descansar aqui una vez."),
    (1, 1): ("Ruinas", "Entre las piedras brilla una llave antigua."),
    (2, 1): ("Acantilado", "El viento trae ecos desde el oeste."),
    (0, 2): ("Palmeral", "Las palmeras susurran: busca en las ruinas."),
    (1, 2): ("Cueva", "Un cofre cerrado espera. Necesitas la llave."),
    (2, 2): ("Faro", "La luz ilumina la entrada de la cueva al oeste."),
}

DIRECCIONES = {"norte": (0, 1), "sur": (0, -1), "este": (1, 0), "oeste": (-1, 0)}
INICIO = (0, 0)
LAGUNA = (0, 1)
LLAVE = (1, 1)
TESORO = (1, 2)
