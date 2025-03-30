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
        """Implementa el algoritmo de Dijkstra para encontrar la mejor ruta entre dos estaciones."""
        if inicio not in self.grafo or destino not in self.grafo:
            return "No hay ruta disponible"

        prioridad = []
        heapq.heappush(prioridad, (0, inicio, []))
        costos = {nodo: float('inf') for nodo in self.grafo}
        costos[inicio] = 0

        while prioridad:
            costo_actual, estacion_actual, ruta = heapq.heappop(prioridad)

            if estacion_actual == destino:
                return ruta + [estacion_actual], costo_actual

            if costo_actual > costos[estacion_actual]:
                continue

            for vecino, costo in self.grafo[estacion_actual]:
                nuevo_costo = costo_actual + costo
                if nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    heapq.heappush(prioridad, (nuevo_costo, vecino, ruta + [estacion_actual]))

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
    resultado = sistema_transporte.buscar_ruta_optima(inicio, destino)
    
    if isinstance(resultado, tuple):
        mejor_ruta, costo_total = resultado
        print(f"Mejor ruta de {inicio} a {destino}: {mejor_ruta} con un costo total de {costo_total}")
    else:
        print(resultado)
