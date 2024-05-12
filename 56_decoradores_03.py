usuario_autenticado = True
def autenticacion(funcion):
    def envolver(*args, **kwargs):
        if not usuario_autenticado:
            raise PermissionError("Usuario no autenticado")
        return funcion(*args,**kwargs)
    return envolver

@autenticacion
def acceder():
    print("Accediendo a la cuenta")
    
acceder()
# simulamos no autenticado
usuario_autenticado = False
acceder()
