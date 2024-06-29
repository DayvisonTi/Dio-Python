import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args):
        print("Estou testando...")
        func(*args)
        return func(*args)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.title()

tecnologia = aprender("python")
print(tecnologia)
print(aprender.__name__)
        