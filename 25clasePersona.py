class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        dato = f'Nombre: {self.__nombre}\nEdad: {self.__edad}'
        return dato

    @property
    # getter
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def hablar(self):
        print("Estoy hablando")

    @edad.setter
    def edad(self, nueva):
        # setter
        self.__edad = nueva
        print("Edad modificada")


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.__asignatura = asignatura

    @property
    def asignatura(self):
        return self.__asignatura

    @asignatura.setter
    def asignatura(self, nueva):
        print("Asignatura modificada")
        self.__asignatura = nueva


class Alumno(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nueva):
        print("Nota modificada")
        self.__nota = nueva

    def calificacion(self):
        if self.__nota >= 5:
            print("Aprobado")
        else:
            print("Suspenso")


if __name__ == '__main__':
    Jose = Persona('Jose', 50)
    print(Jose)
    Jose.hablar()
    print(Jose.edad)
    Jose.edad = 40
    print(Jose.edad)
    Mar = Profesor('Mar', 48, 'Biologia')
    Mar.hablar()
    print(Mar)
    print(Mar.edad)
    print(Mar.asignatura)
    Mar.asignatura = 'Matematicas'
    print(Mar.asignatura)
    Lucia = Alumno('Lucia', 13, 9)
    print(Lucia)
    print(Lucia.nota)
    Lucia.nota = 10
    print(Lucia.nota)
    Lucia.calificacion()
    Lucia.hablar()
