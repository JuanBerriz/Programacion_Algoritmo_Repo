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
        print(f"{(self.local).pais} VS {(self.visitante).pais}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Estadio: {(self.estadio).nombre}")
        print(f"ID del partido: {self.id}")
        print("\n")

    def mostrar_compra():
        for match in Partido.lista_partidos:
            print(f"{(match.local).pais} VS {(match.visitante).pais}")
            print(f"Fecha: {match.fecha}")
            print(f"Hora: {match.hora}")
            print(f"Estadio: {(match.estadio).nombre}")
            print(f"ID del partido: {match.id}")
            print("\n")
        
    def titulo(self):
       return (self.local).pais + "  VS  " + (self.visitante).pais
    
    def buscar_id(id):
        for match in Partido.lista_partidos:
            if match.id == id:
                return match