class Partido:
    lista_partidos = []
    def __init__(self, local, visitante, fecha, hora, estadio, id):
        self.local = local
        self.visitante = visitante
        self.fecha = fecha
        self.hora = hora
        self.estadio = estadio
        self.id = id

    def mostrar(self):
        print(f"{self.local} VS {self.visitante}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"ID Estadio: {self.estadio}")
        print(f"ID del partido: {self.id}")
        print("\n")

    def mostrar_compra():
        for match in Partido.lista_partidos:
            print(f"{match.local} VS {match.visitante}")
            print(f"Fecha: {match.fecha}")
            print(f"Hora: {match.hora}")
            print(f"ID Estadio: {match.estadio}")
            print(f"ID del partido: {match.id}")
            print("\n")
        
    def titulo(self):
       return self.local+ "  VS  " + self.visitante
    
    def buscar_id(id):
        for match in Partido.lista_partidos:
            if match.id == id:
                return match

