import heapq

class TransporteInteligente:
    def __init__(self):
        self.grafo = {}

    def agregar_conexion(self, inicio, destino, costo):
        """Agrega una conexión bidireccional entre dos estaciones con un costo."""
        if inicio not in self.grafo:
            self.grafo[inicio] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[inicio].append((destino, costo))
        self.grafo[destino].append((inicio, costo))  # Suponemos que es bidireccional

    def buscar_ruta_optima(self, inicio, destino):
        """Implementa el algoritmo A* para encontrar la mejor ruta entre dos estaciones."""
        if inicio not in self.grafo or destino not in self.grafo:
            return "No hay ruta disponible"

        prioridad = []
        heapq.heappush(prioridad, (0, inicio, []))
        visitados = set()

        while prioridad:
            costo_actual, estacion_actual, ruta = heapq.heappop(prioridad)

            if estacion_actual in visitados:
                continue
            visitados.add(estacion_actual)
            ruta = ruta + [estacion_actual]

            if estacion_actual == destino:
                return ruta

            for vecino, costo in self.grafo[estacion_actual]:
                if vecino not in visitados:
                    heapq.heappush(prioridad, (costo_actual + costo, vecino, ruta))

        return "No hay ruta disponible"

# Ejemplo de uso
if __name__ == "__main__":
    sistema_transporte = TransporteInteligente()
    sistema_transporte.agregar_conexion("A", "B", 1)
    sistema_transporte.agregar_conexion("A", "C", 4)
    sistema_transporte.agregar_conexion("B", "C", 2)
    sistema_transporte.agregar_conexion("B", "D", 5)
    sistema_transporte.agregar_conexion("C", "D", 1)
    sistema_transporte.agregar_conexion("D", "E", 3)

    inicio, destino = "A", "E"
    mejor_ruta = sistema_transporte.buscar_ruta_optima(inicio, destino)
    print(f"Mejor ruta de {inicio} a {destino}: {mejor_ruta}")
