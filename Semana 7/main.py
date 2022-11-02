#Ejercicio clases

class Persona():
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class Redactor(Persona):
    def __init__(self, nombre, cedula, seccion):
        Persona.__init__(self, nombre, cedula)
        self.seccion = seccion

class Jefe(Redactor):
    def __init__(self, nombre, cedula, seccion, lista_redactores):
        Redactor.__init__(self, nombre, cedula, seccion)
        self.lista_redactores = lista_redactores

class Articulo():
    def __init__(self, titulo, resumen, cuerpo, imagenes, publicacion, creacion, redactor):
        self.titulo = titulo
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.imagenes = imagenes
        self.publicacion = publicacion
        self.creacion = creacion
        self. redactor = redactor
