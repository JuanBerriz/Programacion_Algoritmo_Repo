class Equipo:
    lista_equipos = []

    def __init__(self, pais, codigo, grupo, id):
        self.pais = pais
        self.codigo = codigo
        self.grupo = grupo
        self.id = id

    def mostrar_equipos(self):
        print(f"Pais: {self.pais}")
        print(f"Codigo FIFA: {self.codigo}")
        print("\n")

    def buscar_pais(pais):
        for team in Equipo.lista_equipos:
            if team.pais == pais:
                return team
    
    def prueba(self):
        print(type(self.pais))
        print(type(self.codigo))
        print(type(self.grupo))
        print(type(self.id))

    def buscar_codigo(code):
        for team in Equipo.lista_equipos:
            if team.codigo == code:
                return team