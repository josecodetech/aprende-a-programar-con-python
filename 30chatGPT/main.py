import openai
from secret import CLAVE as key


openai.api_key = key
def guardar(archivo, texto):
    archivo = archivo+".txt"
    with open(archivo, 'w') as fichero:
        fichero.write(texto)
    print(f"\nFichero {archivo} guardado\n")
while True:
    pregunta = input("¿Que pregunamos a chatGPT? -> (o \"salir\")")
    if pregunta.upper() == "SALIR":
        print("\nSaliendo...")
        break
    try:
        respuesta = openai.Completion.create(engine='text-davinci-003',prompt=pregunta,max_tokens=2048)
        resp = respuesta.choices[0].text
        print(f"\n{resp}")
    except:
        print("Error en la peticion, vuelve a intentarlo")
    pregunta = input("¿Quieres guardar la respuesta ? -> (S o N)")
    if pregunta.upper()=="S":
        archivo = input("¿Dime el nombre del archivo ?")
        guardar(archivo, resp)
    else:
        print("\Continuamos...\n")
        